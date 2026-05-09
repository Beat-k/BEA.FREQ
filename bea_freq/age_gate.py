"""
BEA.FREQ — AgeGate
===================
Profile-based signal filtering and substitution.

Core rule: signals are never blocked — they are rerouted to a compatible frequency.

  G  → passes through for all profiles
  M  → OWNER / USER: passes through
       CHILD:         rerouted to nearest G-rated equivalent
       GUEST:         stripped (None returned)
  R  → OWNER (r_unlocked=True): passes through
       CHILD:         rerouted to silence (s.i.lence)
       all others:    stripped (None returned)

Copyright (c) 2026 Jeremy F. Jackson, BEATEK Holdings LLC. All Rights Reserved.
"""

from __future__ import annotations

from typing import List, Optional

from .schema import (
    CHILD_SUBSTITUTION,
    ContentRating,
    FreqSignal,
    ProfileType,
    SIGNAL_VOCAB,
)

# The G-rated silence signal used when an R-rated signal hits a CHILD profile
_SILENCE_SIGNAL: Optional[FreqSignal] = SIGNAL_VOCAB.get("silence")


class AgeGate:
    """
    Filters and substitutes BEA.FREQ signals based on the active UserProfile type.

    Usage::

        gate = AgeGate(ProfileType.CHILD)
        safe_signal = gate.filter(signal)   # None if stripped, substitute if rerouted

        safe_list = gate.filter_all(signals)
    """

    def __init__(
        self,
        profile_type: ProfileType,
        r_unlocked: bool = False,
    ) -> None:
        """
        Args:
            profile_type: the active session profile (OWNER / USER / CHILD / GUEST)
            r_unlocked:   OWNER-only flag — must be True for R-rated signals to pass
        """
        self.profile_type = profile_type
        self.r_unlocked = r_unlocked

    # ── Main filter ───────────────────────────────────────────────────────────

    def filter(self, signal: FreqSignal) -> Optional[FreqSignal]:
        """
        Apply age gate to a single signal.

        Returns:
          - The original signal if it passes through
          - A substitute signal if rerouted (signal never None in CHILD path)
          - None if the signal is stripped
        """
        if signal.rating == ContentRating.G:
            return signal

        if signal.rating == ContentRating.M:
            return self._handle_m(signal)

        if signal.rating == ContentRating.R:
            return self._handle_r(signal)

        # Unknown rating — pass through
        return signal

    def filter_all(self, signals: List[FreqSignal]) -> List[FreqSignal]:
        """
        Apply age gate to a list of signals.

        Returns only signals that pass or are substituted (stripped signals excluded).
        """
        result: List[FreqSignal] = []
        for s in signals:
            out = self.filter(s)
            if out is not None:
                result.append(out)
        return result

    # ── Private helpers ───────────────────────────────────────────────────────

    def _handle_m(self, signal: FreqSignal) -> Optional[FreqSignal]:
        if self.profile_type in (ProfileType.OWNER, ProfileType.USER):
            return signal

        if self.profile_type == ProfileType.CHILD:
            substitute_word = CHILD_SUBSTITUTION.get(signal.word.lower())
            if substitute_word:
                sub = SIGNAL_VOCAB.get(substitute_word)
                return sub if sub is not None else _SILENCE_SIGNAL
            # No substitute defined — fall back to silence
            return _SILENCE_SIGNAL

        # GUEST — strip M signals
        return None

    def _handle_r(self, signal: FreqSignal) -> Optional[FreqSignal]:
        if self.profile_type == ProfileType.OWNER and self.r_unlocked:
            return signal

        if self.profile_type == ProfileType.CHILD:
            # R stripped → silence (signal is not passed through at all)
            return _SILENCE_SIGNAL

        # USER / GUEST / OWNER without unlock — strip
        return None

    # ── Convenience ───────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"AgeGate(profile={self.profile_type.value} "
            f"r_unlocked={self.r_unlocked})"
        )
