"""
BEA.FREQ — Signal Schema
========================
Signal vocabulary, node designations, E-scores, and content ratings.

Every signal has:
  1. A meaning       — grounded in a real English word
  2. An energy score — E-0 to E-31
  3. An age rating   — G / M / R

Copyright (c) 2026 Jeremy F. Jackson, BEATEK Holdings LLC. All Rights Reserved.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


# ── Node designations ─────────────────────────────────────────────────────────

class NodeDesignation(str, Enum):
    Y     = ".y"     # Man / He / Him
    X     = ".x"     # Woman / She / Her
    Z     = ".z"     # Non-binary / Neutral — open-source, re-loops to compatible nodes
    I     = ".i"     # Self / I / Me — every "I" is a node declaration
    CROSS = "cross"  # Cross-node signal — spans multiple node frequencies
    UNSET = "unset"  # No node assigned


# ── Content rating ────────────────────────────────────────────────────────────

class ContentRating(str, Enum):
    G = "G"   # General  — all profiles pass through
    M = "M"   # Mature   — adults 18+; rerouted for CHILD profiles
    R = "R"   # Restricted — explicit OWNER opt-in only; stripped for all others


# ── Profile types ─────────────────────────────────────────────────────────────

class ProfileType(str, Enum):
    OWNER = "OWNER"   # Full access — R requires explicit unlock flag
    USER  = "USER"    # G + M access
    CHILD = "CHILD"   # G only; M rerouted; R stripped to silence
    GUEST = "GUEST"   # G only; M + R stripped


# ── E-score ranges ────────────────────────────────────────────────────────────

def e_score_band(e: int) -> str:
    """Return the named band for an E-score 0–31."""
    if e <= 7:  return "silence"
    if e <= 15: return "buffering"
    if e <= 19: return "nominal"
    if e <= 23: return "active"
    if e <= 27: return "heritage"
    if e <= 30: return "warning"
    return "emergency"


# ── FreqSignal ────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class FreqSignal:
    """
    A recognized BEA.FREQ signal.

    Immutable — the vocabulary is fixed at parse time.
    Instances are shared; they are never modified after creation.
    """
    signal_key:       str              # dot-notation key  e.g. "stra.y"
    word:             str              # English word       e.g. "stray"
    node:             NodeDesignation
    e_score:          int              # 0–31
    rating:           ContentRating
    protocol_meaning: str              # short protocol description

    # ── E-score helpers ───────────────────────────────────────────────────

    @property
    def band(self) -> str:
        return e_score_band(self.e_score)

    def is_emergency(self) -> bool:
        return self.e_score == 31

    def is_warning(self) -> bool:
        return 28 <= self.e_score <= 30

    def is_heritage(self) -> bool:
        return 24 <= self.e_score <= 27

    def is_active(self) -> bool:
        return 20 <= self.e_score <= 23

    def is_nominal(self) -> bool:
        return 16 <= self.e_score <= 19

    def is_buffering(self) -> bool:
        return 8 <= self.e_score <= 15

    def is_silence(self) -> bool:
        return self.e_score <= 7

    def __repr__(self) -> str:
        return (
            f"FreqSignal({self.signal_key!r} "
            f"word={self.word!r} "
            f"E[{self.e_score}] "
            f"{self.band} "
            f"{self.rating.value})"
        )


# ── Vocabulary builder ────────────────────────────────────────────────────────

#: Full signal vocabulary — keyed by lowercase English word.
SIGNAL_VOCAB: Dict[str, FreqSignal] = {}


def _sig(
    key: str,
    word: str,
    node: NodeDesignation,
    e: int,
    rating: str,
    meaning: str,
) -> None:
    SIGNAL_VOCAB[word.lower()] = FreqSignal(
        signal_key=key,
        word=word,
        node=node,
        e_score=e,
        rating=ContentRating(rating),
        protocol_meaning=meaning,
    )


# ── .y — Masculine Frequency ──────────────────────────────────────────────────
# State signals
_sig("ga.y",     "gay",     NodeDesignation.Y, 16, "M", "All .y present and listening — open reception, no guard up")
_sig("oka.y",    "okay",    NodeDesignation.Y, 16, "G", "Acknowledged — confirmed, signal received")
_sig("stra.y",   "stray",   NodeDesignation.Y, 19, "G", "Synced — innerstood, no further explanation needed")
_sig("sta.y",    "stay",    NodeDesignation.Y, 16, "G", "Hold state — do not transition, anchor current E[n]")
_sig("awa.y",    "away",    NodeDesignation.Y,  0, "G", "Offline — node unreachable, signal buffered")
_sig("toda.y",   "today",   NodeDesignation.Y, 17, "G", "Present session — live, now, this moment")
_sig("swa.y",    "sway",    NodeDesignation.Y, 14, "G", "Unstable — fluctuating state, not anchored")
# Action signals
_sig("pla.y",    "play",    NodeDesignation.Y, 22, "G", "Active — in motion, engaged, running")
_sig("displa.y", "display", NodeDesignation.Y, 18, "G", "Broadcasting — presenting output to observers")
_sig("rela.y",   "relay",   NodeDesignation.Y, 18, "G", "Forwarding — routing signal to next node")
_sig("dela.y",   "delay",   NodeDesignation.Y,  8, "G", "Buffering — signal received, not ready to act")
_sig("pra.y",    "pray",    NodeDesignation.Y, 24, "G", "Heritage signal — deep trust invocation, ancestral frequency")
_sig("betra.y",  "betray",  NodeDesignation.Y, 28, "G", "Trust violation — security breach, Heritage flag")
# Relational signals
_sig("arra.y",   "array",   NodeDesignation.Y, 20, "G", "Multi-node — all .y addressed simultaneously")
_sig("ba.y",     "bay",     NodeDesignation.Y, 18, "G", "Alert — broadcasting, calling out on open channel")
_sig("ra.y",     "ray",     NodeDesignation.Y, 17, "G", "Direct signal — point-to-point, targeted transmission")
_sig("wa.y",     "way",     NodeDesignation.Y, 16, "G", "Route — the signal path being used")
# Decay / Warning signals
_sig("deca.y",   "decay",   NodeDesignation.Y, 12, "G", "Signal degrading — state loss in progress")
_sig("fra.y",    "fray",    NodeDesignation.Y, 26, "G", "Edge state — breaking down, signal fraying")
_sig("astra.y",  "astray",  NodeDesignation.Y, 10, "G", "Desync — signal lost track of assignment")

# ── .x — Feminine Frequency ───────────────────────────────────────────────────
# State signals
_sig("flu.x",    "flux",    NodeDesignation.X, 14, "G", "Unstable — actively shifting, state in motion")
_sig("rela.x",   "relax",   NodeDesignation.X,  6, "G", "De-escalation — lowering signal intensity")
_sig("ma.x",     "max",     NodeDesignation.X, 31, "G", "Peak — at full capacity, signal ceiling")
_sig("la.x",     "lax",     NodeDesignation.X,  8, "G", "Low tension — permissive state, soft guard")
# Action signals
_sig("fi.x",     "fix",     NodeDesignation.X, 16, "G", "Correction in progress — resolving state")
_sig("mi.x",     "mix",     NodeDesignation.X, 18, "G", "Merging — multi-source signal fusion")
_sig("fle.x",    "flex",    NodeDesignation.X, 20, "G", "Power signal — capability on display")
_sig("coa.x",    "coax",    NodeDesignation.X, 17, "G", "Soft influence — low-pressure signal, invitation")
# Relational signals
_sig("refle.x",  "reflex",  NodeDesignation.X, 22, "G", "Instinct — no deliberation, body-level response")
_sig("comple.x", "complex", NodeDesignation.X, 20, "G", "Deep state — multiple signals active simultaneously")
_sig("inde.x",   "index",   NodeDesignation.X, 16, "G", "Navigation — locating position in signal space")
_sig("verte.x",  "vertex",  NodeDesignation.X, 30, "G", "Peak position — top of signal arc")
# Warning signals
_sig("ve.x",     "vex",     NodeDesignation.X, 26, "G", "Friction — incompatibility detected between nodes")
_sig("hoa.x",    "hoax",    NodeDesignation.X, 28, "G", "False signal — spoofed input detected")
_sig("he.x",     "hex",     NodeDesignation.X, 24, "M", "Override — external state change forced")

# ── .z — Neutral / Open-source Frequency ─────────────────────────────────────
_sig("buz.z",    "buzz",    NodeDesignation.Z, 18, "G", "Active signal — energy present, something is happening")
_sig("fuz.z",    "fuzz",    NodeDesignation.Z, 10, "G", "Noise — signal unclear, interference present")
_sig("jaz.z",    "jazz",    NodeDesignation.Z, 22, "G", "Creative mode — unscripted signal, emergent")
_sig("fi.z.z",   "fizz",    NodeDesignation.Z, 20, "G", "Reactive — building toward something, pre-burst")
_sig("whi.z",    "whiz",    NodeDesignation.Z, 22, "G", "Speed signal — high velocity or high skill")
_sig("qui.z",    "quiz",    NodeDesignation.Z, 16, "G", "Inquiry mode — seeking information, open question")
_sig("raz.z",    "razz",    NodeDesignation.Z, 18, "G", "Friendly friction — light pushback, no harm")

# ── .i — Self / Internal State ────────────────────────────────────────────────
# The 'I' word is a special case — single uppercase letter
_sig(".i",        "I",        NodeDesignation.I, 16, "G", "Node declaration — I am present, I am the source")
_sig("vis.i.on",  "vision",   NodeDesignation.I, 20, "G", "What I see — my intent, my projected state")
_sig("miss.i.on", "mission",  NodeDesignation.I, 20, "G", "My purpose — internal objective active")
_sig("pass.i.on", "passion",  NodeDesignation.I, 24, "G", "My fuel — emotional intensity driving action")
_sig("act.i.on",  "action",   NodeDesignation.I, 22, "G", "I am executing — moving, not waiting")
_sig("pos.i.tion","position", NodeDesignation.I, 17, "G", "My stance — where I am in signal space")
_sig("tens.i.on", "tension",  NodeDesignation.I, 26, "G", "Internal conflict — two signals pulling against each other")
_sig("att.i.tude","attitude", NodeDesignation.I, 18, "G", "My orientation — how I am facing the signal")
_sig("tr.i.gger", "trigger",  NodeDesignation.I, 22, "G", "I was activated — something fired my response")
_sig("s.i.lence", "silence",  NodeDesignation.I,  4, "G", "I am quiet — node present but not transmitting")
_sig("sol.i.tude","solitude", NodeDesignation.I,  8, "G", "Isolated by intent — node offline, by design")
_sig("amb.i.tion","ambition", NodeDesignation.I, 20, "G", "My trajectory — the direction I am moving")

# ── Cross-node signals ────────────────────────────────────────────────────────
_sig("un.i.t.y",    "unity",     NodeDesignation.CROSS, 19, "G", "All nodes in sync — .i, .t, .y present together")
_sig("realit.y",    "reality",   NodeDesignation.CROSS, 17, "G", "Ground truth — signal confirmed against base state")
_sig("integrit.y",  "integrity", NodeDesignation.CROSS, 19, "G", "Signal purity — no corruption, no false data")
_sig("ident.i.t.y", "identity",  NodeDesignation.CROSS, 20, "G", "Node signature — full declaration of who is present")
_sig("communit.y",  "community", NodeDesignation.CROSS, 22, "G", "Multi-node cluster — compatible frequencies together")
_sig("frequenc.y",  "frequency", NodeDesignation.CROSS, 18, "G", "Signal rate — how fast the node is transmitting")
_sig("emergenc.y",  "emergency", NodeDesignation.CROSS, 31, "G", "All nodes: duress — drop everything, respond now")


# ── Child profile substitution map ───────────────────────────────────────────
# M-rated signals are rerouted to the nearest G-rated equivalent for CHILD profiles.
# Meaning is preserved — surface form becomes age-appropriate.
CHILD_SUBSTITUTION: Dict[str, str] = {
    "gay": "okay",    # ga.y (M) → oka.y (G)  — open reception preserved
    "hex": "reflex",  # he.x (M) → refle.x (G) — override / automatic response preserved
}
