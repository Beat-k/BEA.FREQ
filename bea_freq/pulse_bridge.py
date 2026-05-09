"""
BEA.FREQ — FreqPulseBridge
===========================
Converts detected FreqSignals into BEA_Pulse PulseEvents.

  Output : SignalEvent → BEA_Pulse
  Pillar : coral.dot_signal_classifier
  Lane   : coral
  Source : coral (Dual Edge TPU)

Payload fields emitted on every PulseEvent:
  source_node      — NodeDesignation value (.y / .x / .z / .i / cross)
  signal_word      — English word e.g. "stray"
  signal_key       — dot-notation key e.g. "stra.y"
  e_score          — 0–31
  content_rating   — G / M / R
  protocol_meaning — short description

BEA_Pulse is imported lazily — the bridge degrades gracefully when
BEA_Pulse is not installed (returns None from emit()).

Copyright (c) 2026 Jeremy F. Jackson, BEATEK Holdings LLC. All Rights Reserved.
"""

from __future__ import annotations

import os
import sys
from typing import Optional

from .schema import FreqSignal

# ── Optional BEA_Pulse import ─────────────────────────────────────────────────
# Try to locate BEA_Pulse relative to this package (../../BEA_Pulse)
_pkg_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_pulse_path = os.path.join(_pkg_dir, "..", "BEA_Pulse")
if os.path.isdir(_pulse_path) and _pulse_path not in sys.path:
    sys.path.insert(0, _pulse_path)

try:
    from event import (  # type: ignore[import]
        BEAOperator,
        EventPriority,
        LaneName,
        PulseEvent,
        SourceType,
    )
    _PULSE_AVAILABLE = True
except ImportError:
    _PULSE_AVAILABLE = False

SOURCE_PILLAR = "coral.dot_signal_classifier"


# ── Signal → operator + priority mapping ─────────────────────────────────────

def _operator_for(signal: FreqSignal) -> str:
    """Map E-score band to the most semantically appropriate BEA operator."""
    e = signal.e_score
    if e >= 28:  return BEAOperator.FIRE      # ⊕  warning/emergency — emergent new state
    if e >= 24:  return BEAOperator.SOLAR     # ⨀  heritage — stable deep signal
    if e >= 20:  return BEAOperator.AIR       # ◴  active — transition in progress
    if e >= 8:   return BEAOperator.TEMPORAL  # ⧖  nominal/buffering — resonating in place
    return BEAOperator.WATER                  # ⊖  silence — de-escalation


def _priority_for(signal: FreqSignal) -> "EventPriority":
    """Map E-score to PulseEvent priority."""
    if signal.e_score == 31:  return EventPriority.CRITICAL
    if signal.e_score >= 28:  return EventPriority.HIGH
    return EventPriority.NORMAL


# ── Standalone converter ──────────────────────────────────────────────────────

def to_pulse_event(
    signal: FreqSignal,
    e_state_from: int = 0,
) -> Optional["PulseEvent"]:
    """
    Convert a single FreqSignal to a PulseEvent.

    Args:
        signal:       the detected BEA.FREQ signal
        e_state_from: the E-state before this signal fired (default 0)

    Returns:
        PulseEvent if BEA_Pulse is available, else None.
    """
    if not _PULSE_AVAILABLE:
        return None

    return PulseEvent(
        source_pillar=SOURCE_PILLAR,
        e_state_from=e_state_from,
        e_state_to=signal.e_score,
        operator=_operator_for(signal),
        priority=_priority_for(signal),
        source_type=SourceType.CORAL.value,
        lane=LaneName.CORAL.value,
        payload={
            "source_node":      signal.node.value,
            "signal_word":      signal.word,
            "signal_key":       signal.signal_key,
            "e_score":          signal.e_score,
            "content_rating":   signal.rating.value,
            "protocol_meaning": signal.protocol_meaning,
        },
    )


# ── Stateful bridge ───────────────────────────────────────────────────────────

class FreqPulseBridge:
    """
    Stateful bridge: tracks current E-state so each emitted PulseEvent
    records a meaningful E[from → to] transition rather than always 0 → n.

    One instance per session is the intended pattern.

    Usage::

        bridge = FreqPulseBridge()
        event  = bridge.emit(signal)   # PulseEvent or None
    """

    def __init__(self) -> None:
        self._current_e: int = 0

    @property
    def current_e_state(self) -> int:
        return self._current_e

    def emit(self, signal: FreqSignal) -> Optional["PulseEvent"]:
        """
        Convert signal → PulseEvent and advance internal E-state.

        Returns None when BEA_Pulse is not available.
        """
        event = to_pulse_event(signal, e_state_from=self._current_e)
        self._current_e = signal.e_score
        return event

    def reset(self) -> None:
        """Reset internal E-state to 0 (start of session)."""
        self._current_e = 0

    def pulse_available(self) -> bool:
        """True if BEA_Pulse is importable and PulseEvents can be created."""
        return _PULSE_AVAILABLE

    def __repr__(self) -> str:
        return f"FreqPulseBridge(e_state={self._current_e} pulse={_PULSE_AVAILABLE})"
