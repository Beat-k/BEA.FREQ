"""
BEA.FREQ™ — Tuned Signal Communication for Compatible Nodes
=============================================================
BEATEK Holdings, LLC
Co-developed: Jaxxon (Jeremy F. Jackson) & Claude AI (Anthropic)

BEA.FREQ is a signal vocabulary and content rating framework for the BEATEK
ecosystem. It gives people and systems a shared language for broadcasting
state — without over-explaining.

Every signal has three things:
  1. A meaning       — grounded in a real English word
  2. An energy score — E-0 to E-31
  3. An age rating   — G / M / R

Quick start::

    from bea_freq import DotSignalClassifier, AgeGate, ProfileType

    clf  = DotSignalClassifier()
    gate = AgeGate(ProfileType.USER)

    signals = clf.classify("let's play and relay the mission")
    safe    = gate.filter_all(signals)

Copyright (c) 2026 Jeremy F. Jackson, BEATEK Holdings LLC. All Rights Reserved.
"""

from .schema import (
    CHILD_SUBSTITUTION,
    ContentRating,
    FreqSignal,
    NodeDesignation,
    ProfileType,
    SIGNAL_VOCAB,
    e_score_band,
)
from .classifier import DotSignalClassifier
from .age_gate import AgeGate
from .pulse_bridge import FreqPulseBridge, to_pulse_event

__version__ = "0.1.0"

__all__ = [
    # schema
    "NodeDesignation",
    "ContentRating",
    "ProfileType",
    "FreqSignal",
    "SIGNAL_VOCAB",
    "CHILD_SUBSTITUTION",
    "e_score_band",
    # classifier
    "DotSignalClassifier",
    # age gate
    "AgeGate",
    # pulse bridge
    "FreqPulseBridge",
    "to_pulse_event",
]
