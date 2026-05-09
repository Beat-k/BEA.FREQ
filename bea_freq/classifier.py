"""
BEA.FREQ — DotSignalClassifier
================================
Coral TPU Secretary role — dot_signal_classifier (13th role)

Scans text streams for BEA.FREQ signal words and returns FreqSignal matches.

  TOPS budget : ~1%  (~0.08 TOPS)
  Cycle slot  : 50ms
  Input       : text stream — voice transcript, chat, script
  Output      : list[FreqSignal] → FreqPulseBridge → BEA_Pulse

The pattern is pre-compiled once at import time.
Classification is O(n) over input length — suitable for 50ms timeslice.
CPU fallback is fully functional when running off-chip.

Copyright (c) 2026 Jeremy F. Jackson, BEATEK Holdings LLC. All Rights Reserved.
"""

from __future__ import annotations

import re
from typing import List, Optional

from .schema import FreqSignal, SIGNAL_VOCAB


# ── Pre-compiled vocabulary pattern ──────────────────────────────────────────
# Sort longest-first so "stray" matches before "ray", "astray" before "stray", etc.
_VOCAB_WORDS: List[str] = sorted(SIGNAL_VOCAB.keys(), key=len, reverse=True)

# Special case: "I" (the .i node declaration) must match standalone — not as a
# substring inside other words. The \b word-boundary handles this for most words,
# but "I" needs case-sensitive standalone matching.
_VOCAB_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(w) for w in _VOCAB_WORDS) + r")\b",
    re.IGNORECASE,
)

# Standalone "I" — whole word, case-sensitive (only uppercase I is the node declaration)
_I_NODE_PATTERN = re.compile(r"(?<!\w)I(?!\w)")


# ── Classifier ────────────────────────────────────────────────────────────────

class DotSignalClassifier:
    """
    Lightweight text classifier — identifies BEA.FREQ signals in a text stream.

    Designed to run in a 50ms Coral TPU timeslice (dot_signal_classifier role).

    Usage::

        classifier = DotSignalClassifier()
        signals = classifier.classify("let's play and relay the mission")
        # → [FreqSignal(pla.y ...), FreqSignal(rela.y ...), FreqSignal(miss.i.on ...)]
    """

    def classify(self, text: str) -> List[FreqSignal]:
        """
        Scan *text* and return all recognized BEA.FREQ signals in order of appearance.

        - Vocabulary words are matched case-insensitively as whole words.
        - The standalone capital "I" is detected as the .i node declaration.
        - A single occurrence of a word returns a single signal (not deduplicated —
          if "play" appears twice, two FreqSignal entries are returned).
        """
        results: List[FreqSignal] = []

        # Track character positions where "I" node fires so we don't double-count
        i_node_positions: set[int] = set()
        i_signal = SIGNAL_VOCAB.get("i")
        if i_signal is not None:
            for m in _I_NODE_PATTERN.finditer(text):
                i_node_positions.add(m.start())

        # Main vocabulary scan
        for m in _VOCAB_PATTERN.finditer(text):
            word_lower = m.group(1).lower()
            signal = SIGNAL_VOCAB.get(word_lower)
            if signal is None:
                continue
            # Skip lowercase "i" matches that are not standalone-I positions
            if word_lower == "i" and m.start() not in i_node_positions:
                continue
            results.append(signal)

        # Inject standalone-I signals at correct sorted position
        # (they were skipped above if the word was lowercase "i")
        if i_signal is not None and i_node_positions:
            # Already captured above if the regex matched uppercase I — no extra work
            pass

        return results

    def classify_first(self, text: str) -> Optional[FreqSignal]:
        """Return only the first recognized signal in the text, or None."""
        signals = self.classify(text)
        return signals[0] if signals else None

    def highest_e_score(self, text: str) -> Optional[FreqSignal]:
        """Return the signal with the highest E-score found in the text."""
        signals = self.classify(text)
        if not signals:
            return None
        return max(signals, key=lambda s: s.e_score)

    def filter_by_node(self, text: str, node_value: str) -> List[FreqSignal]:
        """
        Return only signals matching the given node designation string.

        Args:
            text: input text to scan
            node_value: one of ".y", ".x", ".z", ".i", "cross"
        """
        return [s for s in self.classify(text) if s.node.value == node_value]

    def summary(self, text: str) -> dict:
        """
        Return a summary dict for a text scan — useful for BEA_Pulse payload.

        Keys: signals (list of dicts), count, max_e_score, has_emergency
        """
        signals = self.classify(text)
        if not signals:
            return {"signals": [], "count": 0, "max_e_score": None, "has_emergency": False}
        return {
            "signals": [
                {
                    "signal_key":  s.signal_key,
                    "word":        s.word,
                    "node":        s.node.value,
                    "e_score":     s.e_score,
                    "band":        s.band,
                    "rating":      s.rating.value,
                    "meaning":     s.protocol_meaning,
                }
                for s in signals
            ],
            "count":         len(signals),
            "max_e_score":   max(s.e_score for s in signals),
            "has_emergency": any(s.is_emergency() for s in signals),
        }
