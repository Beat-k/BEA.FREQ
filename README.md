# BEA.FREQ™ v0.1.0

**Tuned Signal Communication for Compatible Nodes**

> BEATEK Holdings LLC | Jeremy F. Jackson (Jaxxon) & Claude AI (Anthropic)
> Part of [BEA_Aura_CDE_OS](../)

---

## What It Is

BEA.FREQ™ is a signal vocabulary and content rating framework for the BEATEK ecosystem. It gives people and systems a shared language for broadcasting state — without over-explaining.

Every signal has three things:

1. **A meaning** — grounded in a real English word
2. **An energy score** — how much weight the signal carries (E-0 to E-31)
3. **An age rating** — who the signal is appropriate for (G / M / R)

The name comes from the core principle: compatible nodes share a frequency. You either resonate or you don't. The signal finds its audience.

---

## Signal Anatomy

A signal is a **real English word** that contains the node letter in a meaningful position. The word must exist in the dictionary. The meaning must resonate naturally — you cannot force it.

```
[stem].[node]         standard format
  stra.y              "stray"  → synced, innerstood
  flu.x               "flux"   → unstable, shifting
  buz.z               "buzz"   → active, energy present

[stem].i.[stem]       .i node — internal position
  vis.i.on            "vision"  → what I see, my intent
  miss.i.on           "mission" → my purpose, active
  s.i.lence           "silence" → present, not transmitting

cross-node signals    multiple node letters in one word
  un.i.t.y            "unity"     → .i + .t + .y — all nodes in sync
  emergenc.y          "emergency" → E[31] — all nodes, drop everything
```

---

## Node Map

| Node | Identity | Status |
|------|----------|--------|
| `.y` | Man / He / Him | Active — origin node |
| `.x` | Woman / She / Her | Active — open for `.x` to develop |
| `.z` | Non-binary / Neutral | Active — open-source, re-loops to compatible nodes |
| `.i` | Self / I / Me | Active — every "I" is a node declaration |
| `.t` | Time | Reserved |
| `.e` | Emotion / Energy | Reserved |
| `.u` | You / Other | Reserved |
| `.a` | Awareness / Aura | Reserved |

Undefined nodes are intentionally blank. Nothing is forced before its time.

---

## E-Score

Every signal carries an energy score from **E-0** (silence) to **E-31** (emergency).

| Range | State | Character |
|-------|-------|-----------|
| E-0 to E-7 | Silence | Offline, away, not transmitting |
| E-8 to E-15 | Buffering | Low tension, receptive, holding |
| E-16 to E-19 | Nominal | Present, acknowledged, synced |
| E-20 to E-23 | Active | In motion, executing, creative |
| E-24 to E-27 | Heritage | Deep signals, ancestral frequency |
| E-28 to E-30 | Warning | Trust violation, deception, friction |
| E-31 | Emergency | All nodes — drop everything, respond now |

E-31 is reserved. `emergenc.y` holds it. It means what it says.

---

## Age Rating

| Rating | Audience | Rule |
|--------|----------|------|
| **G** | General — all users | Passes through for all profiles |
| **M** | Mature — adults 18+ | Rerouted for CHILD profiles |
| **R** | Restricted — explicit opt-in | OWNER only with explicit unlock |

Signals are never blocked — they are rerouted to a compatible frequency.

---

## Module Architecture

```
BEA.FREQ/
├── README.md                      — This file
├── LICENSE                        — MIT + commercial + trademark notice
├── CONTRIBUTING.md                — Contributor guide · grammar and vocabulary rules
├── README_BEA_FREQ.md             — Vision document · full spec · TCS canonical
├── DOT_PROTOCOL_LANGUAGE_SHEET.md — Full signal vocabulary · all nodes · all signals
├── BEA_FREQ_Language_Rating.xlsx  — Signal vocabulary with E-scores and G/M/R ratings
│
└── bea_freq/                      — Python package
    ├── __init__.py                — Package entry point · exports all public types
    ├── schema.py                  — NodeDesignation · ContentRating · ProfileType
    │                                FreqSignal · SIGNAL_VOCAB · CHILD_SUBSTITUTION
    ├── classifier.py              — DotSignalClassifier · O(n) regex scan
    │                                Coral TPU role: dot_signal_classifier
    ├── age_gate.py                — AgeGate · profile-based signal filtering
    │                                never-block guarantee · reroute, not strip
    ├── pulse_bridge.py            — FreqPulseBridge · FreqSignal → PulseEvent
    │                                stateful E-state tracker
    ├── pyproject.toml
    └── tests/
        ├── test_classifier.py     — 27 tests · detection · node · E-score · coverage
        └── test_age_gate.py       — 19 tests · all profiles · M/R routing · guarantees
```

---

## Quick Start

```python
from bea_freq import DotSignalClassifier, AgeGate, ProfileType

clf  = DotSignalClassifier()
gate = AgeGate(ProfileType.USER)

# Classify text
signals = clf.classify("let's play and relay the mission")
# → [FreqSignal(pla.y E[22] active G),
#    FreqSignal(rela.y E[18] nominal G),
#    FreqSignal(miss.i.on E[20] active G)]

# Filter by profile
safe = gate.filter_all(signals)

# Highest urgency signal in a text
top = clf.highest_e_score("the system is in flux — emergency protocol")
# → FreqSignal(emergenc.y E[31] emergency G)

# Summary dict — ready for BEA_Pulse payload
summary = clf.summary("play relay mission")
# → {"count": 3, "max_e_score": 22, "has_emergency": False, "signals": [...]}
```

---

## Signal Vocabulary — Quick Reference

### `.y` — Masculine Frequency

| Signal | Word | E[n] | Rating | Protocol Meaning |
|--------|------|------|--------|-----------------|
| `awa.y` | away | E[0] | G | Offline — node unreachable |
| `dela.y` | delay | E[8] | G | Buffering — not ready to act |
| `deca.y` | decay | E[12] | G | Signal degrading |
| `swa.y` | sway | E[14] | G | Unstable state |
| `oka.y` | okay | E[16] | G | Acknowledged |
| `sta.y` | stay | E[16] | G | Hold state |
| `wa.y` | way | E[16] | G | Route |
| `ga.y` | gay | E[16] | **M** | All .y open reception |
| `ra.y` | ray | E[17] | G | Direct signal |
| `toda.y` | today | E[17] | G | Present session |
| `displa.y` | display | E[18] | G | Broadcasting |
| `rela.y` | relay | E[18] | G | Forwarding |
| `ba.y` | bay | E[18] | G | Alert |
| `stra.y` | stray | E[19] | G | Synced — innerstood |
| `arra.y` | array | E[20] | G | Multi-node |
| `pla.y` | play | E[22] | G | Active — in motion |
| `pra.y` | pray | E[24] | G | Heritage signal |
| `fra.y` | fray | E[26] | G | Edge state |
| `betra.y` | betray | E[28] | G | Trust violation |

### `.x` — Feminine Frequency

| Signal | Word | E[n] | Rating | Protocol Meaning |
|--------|------|------|--------|-----------------|
| `rela.x` | relax | E[6] | G | De-escalation |
| `la.x` | lax | E[8] | G | Low tension |
| `flu.x` | flux | E[14] | G | Unstable |
| `fi.x` | fix | E[16] | G | Correction |
| `inde.x` | index | E[16] | G | Navigation |
| `coa.x` | coax | E[17] | G | Soft influence |
| `mi.x` | mix | E[18] | G | Merging |
| `comple.x` | complex | E[20] | G | Deep state |
| `fle.x` | flex | E[20] | G | Power signal |
| `refle.x` | reflex | E[22] | G | Instinct |
| `he.x` | hex | E[24] | **M** | Override |
| `ve.x` | vex | E[26] | G | Friction |
| `hoa.x` | hoax | E[28] | G | False signal |
| `verte.x` | vertex | E[30] | G | Peak position |
| `ma.x` | max | E[31] | G | Peak capacity |

### `.z` — Neutral / Open-source Frequency

| Signal | Word | E[n] | Rating | Protocol Meaning |
|--------|------|------|--------|-----------------|
| `fuz.z` | fuzz | E[10] | G | Noise |
| `qui.z` | quiz | E[16] | G | Inquiry mode |
| `buz.z` | buzz | E[18] | G | Active signal |
| `raz.z` | razz | E[18] | G | Friendly friction |
| `fi.z.z` | fizz | E[20] | G | Reactive |
| `jaz.z` | jazz | E[22] | G | Creative mode |
| `whi.z` | whiz | E[22] | G | Speed signal |

### `.i` — Self / Internal State

| Signal | Word | E[n] | Rating | Protocol Meaning |
|--------|------|------|--------|-----------------|
| `s.i.lence` | silence | E[4] | G | Not transmitting |
| `sol.i.tude` | solitude | E[8] | G | Isolated by intent |
| `.i` | I | E[16] | G | Node declaration |
| `pos.i.tion` | position | E[17] | G | My stance |
| `att.i.tude` | attitude | E[18] | G | My orientation |
| `vis.i.on` | vision | E[20] | G | What I see |
| `miss.i.on` | mission | E[20] | G | My purpose |
| `amb.i.tion` | ambition | E[20] | G | My trajectory |
| `act.i.on` | action | E[22] | G | I am executing |
| `tr.i.gger` | trigger | E[22] | G | I was activated |
| `pass.i.on` | passion | E[24] | G | My fuel |
| `tens.i.on` | tension | E[26] | G | Internal conflict |

### Cross-Node Signals

| Signal | Word | E[n] | Nodes |
|--------|------|------|-------|
| `realit.y` | reality | E[17] | `.y` + `.t` |
| `frequenc.y` | frequency | E[18] | `.y` + `.e` |
| `un.i.t.y` | unity | E[19] | `.i` + `.t` + `.y` |
| `integrit.y` | integrity | E[19] | `.i` + `.t` + `.y` |
| `ident.i.t.y` | identity | E[20] | `.i` + `.t` + `.y` |
| `communit.y` | community | E[22] | `.y` + `.u` |
| `emergenc.y` | emergency | E[31] | all nodes |

---

## Age Gate

```python
from bea_freq import AgeGate, ProfileType

# CHILD profile — M signals rerouted, R signals → silence
gate = AgeGate(ProfileType.CHILD)

from bea_freq import SIGNAL_VOCAB
gay_signal = SIGNAL_VOCAB["gay"]     # M-rated

result = gate.filter(gay_signal)
# → FreqSignal(oka.y) — rerouted, G-rated, meaning preserved

# Never-block guarantee:
# M signals are always rerouted for CHILD — never None
# R signals → silence (s.i.lence) for CHILD
```

### Child Substitution Map

| Original | Substitute (CHILD) | Preserved Meaning |
|----------|--------------------|-------------------|
| `ga.y` (M) | `oka.y` (G) | Open reception |
| `he.x` (M) | `refle.x` (G) | Override / automatic response |
| Any R | `s.i.lence` (G) | Signal stripped to silence |

---

## BEA_Pulse Integration

```python
from bea_freq import DotSignalClassifier, FreqPulseBridge

clf    = DotSignalClassifier()
bridge = FreqPulseBridge()

text    = "let's play and relay the mission"
signals = clf.classify(text)

for signal in signals:
    event = bridge.emit(signal)
    # event: PulseEvent(
    #   source_pillar = "coral.dot_signal_classifier"
    #   e_state_from  = <previous E-state>
    #   e_state_to    = signal.e_score
    #   operator      = "⊕" | "⨀" | "◴" | "⧖" | "⊖"
    #   source_type   = "coral"
    #   lane          = "coral"
    #   payload = {
    #     "source_node":      ".y",
    #     "signal_word":      "play",
    #     "signal_key":       "pla.y",
    #     "e_score":          22,
    #     "content_rating":   "G",
    #     "protocol_meaning": "Active — in motion, engaged, running",
    #   }
    # )
```

### BEA Operator Mapping

| E-score band | Operator | Meaning |
|---|---|---|
| E[28–31] | `⊕` Fire | Warning / emergency — emergent new state |
| E[24–27] | `⨀` Solar | Heritage — stable deep signal |
| E[20–23] | `◴` Air | Active — transition in progress |
| E[8–19] | `⧖` Temporal | Nominal / buffering — resonating in place |
| E[0–7] | `⊖` Water | Silence — de-escalation |

---

## BEA_Secretary Integration

BEA.FREQ is wired into the Coral Dual Edge TPU as the **13th Secretary role**:

```
SecretaryRole.DOT_SIGNAL_CLASSIFIER  —  role 13
  TOPS budget : ~1%  (~0.08 TOPS)
  Cycle slot  : 50ms
  Input       : text/voice stream
  Output      : SignalEvent → BEA_Pulse
  Trickle     : ACTIVE  (Coral-only · no GPU dependency)
```

E-states for this role:

| Label | E[n] | Condition |
|-------|------|-----------|
| `idle` | E[0] | No text stream active |
| `scanning` | E[16] | Text stream active — scanning |
| `signal` | E[18] | Signal detected — nominal |
| `warning` | E[28] | Warning-band signal detected (E[28–30]) |
| `emergency` | E[31] | Emergency signal detected — all nodes |

In **Trickle Mode**, `dot_signal_classifier` remains active alongside `wake_word`,
`heritage_trust_gate`, `health_baseline`, `signal_routing`, `network_watch`, and `blind_window`.
The Coral is always on. The signal classification never stops.

---

## Test Suite

```bash
# From BEA.FREQ/bea_freq/
python -m pytest tests/ -v

# From BEA_Aura_CDE_OS root
python -m pytest BEA.FREQ/bea_freq/tests/ -v
```

| File | Tests | Coverage |
|------|-------|----------|
| `test_classifier.py` | 27 | Detection · node assignment · E-score bands · case · full vocab |
| `test_age_gate.py` | 19 | All profiles · M rerouting · R stripping · never-block guarantee |

All 46 tests run without hardware. No Coral TPU required. No BEA_Pulse required.

---

## Requirements

- Python 3.11+
- No required runtime dependencies
- BEA_Pulse (optional — `FreqPulseBridge` degrades gracefully without it)

---

## Grammar Rules

1. The word must exist in the dictionary
2. The resonance must feel natural — thematic fit, not force
3. You cannot fake it — if it doesn't fit, it doesn't work
4. Node letters define signal origin
5. `.z` is open-source — owned by no single frequency
6. Each node develops at its own pace — nothing is rushed

---

## License

Copyright (c) 2026 Jeremy F. Jackson, BEATEK Holdings LLC. All Rights Reserved.
See [LICENSE](LICENSE).

## Contact

Jeremy F. Jackson — [jeremy.jackson0@beatek.io](mailto:jeremy.jackson0@beatek.io)
BEATEK Holdings LLC — [https://beatek.io](https://beatek.io)
