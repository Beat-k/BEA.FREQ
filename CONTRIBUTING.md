# Contributing to BEA.FREQ™

**Owner:** Jeremy F. Jackson · BEATEK Holdings, LLC
**Contact:** jeremy.jackson0@beatek.io

Thank you for your interest in BEA.FREQ. This guide covers the grammar rules, vocabulary standards,
signal integrity requirements, age gate contracts, code standards, and submission process.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Grammar Rules — Non-Negotiable](#grammar-rules--non-negotiable)
3. [Adding Signals to the Vocabulary](#adding-signals-to-the-vocabulary)
4. [Node Expansion Rules](#node-expansion-rules)
5. [E-Score Assignment](#e-score-assignment)
6. [Age Rating Rules](#age-rating-rules)
7. [Age Gate Contract](#age-gate-contract)
8. [Child Substitution Map](#child-substitution-map)
9. [Classifier Rules](#classifier-rules)
10. [BEA_Pulse Integration Rules](#bea_pulse-integration-rules)
11. [Development Setup](#development-setup)
12. [Test Standards](#test-standards)
13. [Submission Process](#submission-process)
14. [What Not to Change](#what-not-to-change)

---

## Architecture Overview

BEA.FREQ is a signal vocabulary and content rating framework — not a language model, not a
telecommunications protocol. It is a shared vocabulary where compatible communicators (people
and systems) broadcast state without over-explaining.

```
bea_freq/
  schema.py        — vocabulary, node designations, E-scores, content ratings
  classifier.py    — DotSignalClassifier: text → list[FreqSignal]
  age_gate.py      — AgeGate: profile-based signal filtering + rerouting
  pulse_bridge.py  — FreqPulseBridge: FreqSignal → PulseEvent → BEA_Pulse
```

The Coral Dual Edge TPU runs `dot_signal_classifier` as role 13 of the Secretary layer.
This role scans text/voice streams in a 50ms timeslice at ~1% TOPS and fires `FreqSignal`
events to `FreqPulseBridge` → BEA_Pulse. It stays active in Trickle Mode.

---

## Grammar Rules — Non-Negotiable

These rules apply to every signal in the vocabulary. They are not style preferences.

1. **The word must exist in the dictionary.**
   No invented words. No portmanteaus. No proper nouns. The word must have a standard
   English dictionary definition.

2. **The resonance must feel natural.**
   The protocol meaning must derive from the dictionary definition — not be forced onto it.
   If you have to explain why the word means what you claim, it doesn't work.

3. **You cannot fake it.**
   A signal that doesn't resonate should not be added. Wait for the right word.

4. **Node letters define signal origin.**
   The same stem with a different node is a different signal. `rela.y` and `rela.x` are
   distinct signals from distinct nodes — do not conflate them.

5. **`.z` is open-source.**
   No single identity owns `.z`. Contributions to the `.z` vocabulary must be neutral.

6. **Nodes develop through use.**
   Reserved nodes (`.t`, `.e`, `.u`, `.a`) may not be formally assigned without documented
   lived use and approval from Jeremy F. Jackson. Do not pre-populate reserved nodes.

---

## Adding Signals to the Vocabulary

New signals are added in `schema.py` via the `_sig()` helper:

```python
_sig(
    key     = "stra.y",        # dot-notation key — stem + .node
    word    = "stray",         # the English word (will be lowercased as dict key)
    node    = NodeDesignation.Y,
    e       = 19,              # E-score 0–31
    rating  = "G",             # "G" | "M" | "R"
    meaning = "Synced — innerstood, no further explanation needed",
)
```

**Requirements for a new signal:**

- The word must pass all five grammar rules above
- The `meaning` field must read as a protocol description, not a dictionary definition
- The E-score must be justified against the E-score assignment rules below
- The `key` must follow dot-notation: `[stem].[node]` or `[stem].i.[stem]` for `.i` signals
- The English word must not already be in `SIGNAL_VOCAB`

**Where to place it:**
Add the `_sig()` call in the appropriate node section of `schema.py`, ordered by E-score
ascending within each category (state / action / relational / warning).

---

## Node Expansion Rules

**Active nodes (`.y`, `.x`, `.z`, `.i`):**
Signals may be added by any contributor following grammar and vocabulary rules.
`.x` signals are prioritized for `.x` contributors — seeds are offered, not claimed.
`.z` signals must be demonstrably neutral.

**Reserved nodes (`.t`, `.e`, `.u`, `.a`):**
Do not add signals to reserved nodes without documented justification.
A signal may be proposed for a reserved node if:
- The word carries the node meaning unmistakably
- The signal has been used organically in communication before being defined
- Approval is obtained from Jeremy F. Jackson before merging

**Cross-node signals:**
Words containing multiple node letters active simultaneously. The `CROSS` node designation
is used. Document which nodes are present in the meaning field.

---

## E-Score Assignment

E-scores are not calculated — they are assigned based on the weight and resonance of the signal.
The following guidelines apply:

| Intended band | E-score range | Assign when... |
|---|---|---|
| Silence | E[0–7] | The signal means absence, withdrawal, or offline state |
| Buffering | E[8–15] | Low tension, receptive, holding, not acting yet |
| Nominal | E[16–19] | Present, acknowledged, synced, active listening |
| Active | E[20–23] | In motion, executing, creating, broadcasting |
| Heritage | E[24–27] | Deep trust signals, ancestral resonance, long-term meaning |
| Warning | E[28–30] | Trust violation, deception, friction, breakdown |
| Emergency | E[31] | Reserved — `emergenc.y` and `ma.x` hold E[31]. Do not assign E[31] to new signals without explicit approval. |

When in doubt, assign lower. A signal that escalates can always be revised upward through usage. A
signal over-scored loses meaning.

---

## Age Rating Rules

**G (General):**
The default. Assign to any signal appropriate for all audiences including children.

**M (Mature):**
Assign when the word has a sexual, adult, or culturally sensitive meaning that would not
be appropriate for a child audience. The protocol meaning itself may be neutral — the
word's dictionary definition is what triggers the M rating.

Examples of M signals: `ga.y` (joyful; homosexual), `he.x` (cast a spell; used in adult contexts).

**R (Restricted):**
Reserved for explicit content. No R-rated signals exist in v0.1. R-rated signals require
approval from Jeremy F. Jackson and explicit documentation of the opt-in path.

**When in doubt, rate G.** An M rating restricts the signal for child profiles. Only apply M
when the word's standard definition would require parental guidance.

---

## Age Gate Contract

The `AgeGate` class enforces the following contract. **Do not violate these rules.**

1. **G signals always pass through** for all profile types. No exceptions.

2. **M signals are never stripped for CHILD profiles** — they are rerouted to the nearest
   G-rated equivalent that preserves the protocol meaning. If no substitute is defined,
   the signal routes to `s.i.lence` (G, E[4]). `None` is never returned for CHILD + M.

3. **R signals route to `s.i.lence`** for CHILD profiles (not None — rerouted).

4. **Signals are never blocked — they are rerouted to a compatible frequency.**
   The "never-block" principle is canonical. Any change that causes `None` to be returned
   for a CHILD profile is a contract violation.

5. **GUEST profiles receive G only.** M and R signals return `None` for GUEST.

6. **OWNER + `r_unlocked=True`** is the only path for R signals to pass through.

---

## Child Substitution Map

When adding an M-rated signal, you must define a child substitution if one exists:

```python
# In schema.py
CHILD_SUBSTITUTION: Dict[str, str] = {
    "gay":  "okay",    # ga.y (M) → oka.y (G)
    "hex":  "reflex",  # he.x (M) → refle.x (G)
    # new entry:
    "word": "substitute_word",
}
```

Rules for substitutes:
- The substitute must be G-rated and already in `SIGNAL_VOCAB`
- The substitute must preserve the protocol meaning as closely as possible
- The substitute must be a single vocabulary entry (not a constructed phrase)
- If no appropriate substitute exists, the signal routes to `s.i.lence` by default

---

## Classifier Rules

`DotSignalClassifier` uses a pre-compiled regex pattern built from `SIGNAL_VOCAB` at import time.
Adding a word to `SIGNAL_VOCAB` automatically adds it to the pattern — no manual regex changes needed.

Rules for the classifier:
- Words are matched as whole words (`\b` boundary) and case-insensitively
- The standalone capital `I` is the `.i` node declaration — lowercase `i` is not matched
- Longest words are matched first (sorted by `len`, descending) to prevent partial matches
- The classifier is stateless — it does not track context between calls
- Do not add stateful behavior to `DotSignalClassifier` — it runs in a 50ms Coral timeslice

If you add a word that is a substring of another vocabulary word (e.g., `"ray"` and `"stray"`),
verify that the longest-first ordering handles the overlap correctly. Add a test for it.

---

## BEA_Pulse Integration Rules

`FreqPulseBridge` maps FreqSignals to BEA operators. The operator mapping is fixed:

| E-band | Operator | Do not change |
|---|---|---|
| E[28–31] | `⊕` Fire | Warning signals are always FIRE |
| E[24–27] | `⨀` Solar | Heritage signals are always SOLAR |
| E[20–23] | `◴` Air | Active signals are always AIR |
| E[8–19] | `⧖` Temporal | Nominal signals resonate |
| E[0–7] | `⊖` Water | Silence is always de-escalation |

Priority mapping:
- E[31] → `EventPriority.CRITICAL`
- E[28–30] → `EventPriority.HIGH`
- All others → `EventPriority.NORMAL`

`FreqPulseBridge` is stateful — it tracks `_current_e` across calls. One instance per session
is the intended pattern. Do not reset `_current_e` between signals in a single session.

The `source_pillar` for all BEA.FREQ events is `"coral.dot_signal_classifier"`.
Do not change this value.

---

## Development Setup

```bash
# From BEA.FREQ/bea_freq/
python -m pytest tests/ -v

# From BEA_Aura_CDE_OS root
python -m pytest "BEA.FREQ/bea_freq/tests/" -v

# With coverage
python -m pytest "BEA.FREQ/bea_freq/tests/" -v --tb=short
```

No dependencies beyond Python 3.11 stdlib. BEA_Pulse is optional — the bridge degrades gracefully.

---

## Test Standards

Every contribution must:

- Add tests for every new signal in `test_classifier.py` (detection + node + E-score)
- Add age gate tests for every new M-rated signal (substitute for CHILD, stripped for GUEST)
- Maintain 100% pass rate — no skips
- Include the new signal in `test_all_vocab_words_detectable` via the vocabulary loop
  (this test is automatic — if the word is in `SIGNAL_VOCAB`, it is tested)
- Verify the `never-block` guarantee passes for any new M-rated signal:
  `test_child_m_never_returns_none` runs automatically over all M signals in `SIGNAL_VOCAB`

For any new M signal with a child substitute:
```python
def test_m_<word>_substituted_for_child():
    result = AgeGate(ProfileType.CHILD).filter(get("<word>"))
    assert result is not None
    assert result.word == "<substitute>"
    assert result.rating == ContentRating.G
```

Do not add randomness or sleep to tests. The classifier is deterministic — tests must be too.

---

## Submission Process

1. Fork the repository and create a feature branch:
   ```
   git checkout -b feat/bea-freq-<signal-or-feature>
   ```

2. Make your changes following all rules in this guide.

3. Run the full test suite:
   ```
   python -m pytest "BEA.FREQ/bea_freq/tests/" -v
   ```
   All tests must pass.

4. Open a pull request with:
   - Title: `feat(BEA.FREQ): <brief description>`
   - Description: new signals added, node, E-score justification, age rating rationale
   - Grammar attestation: confirm each new signal passes all five grammar rules
   - Test count before and after

5. Contact for questions or commercial contributions:
   Jeremy F. Jackson — jeremy.jackson0@beatek.io

---

## What Not to Change

The following are architectural constants. Do not modify without explicit approval
from Jeremy F. Jackson:

| Item | Rule |
|---|---|
| Grammar rules (1–6) | The grammar is the foundation — these rules are not adjustable |
| `SIGNAL_VOCAB` existing entries | Removing or redefining an existing signal breaks downstream systems |
| `CHILD_SUBSTITUTION` values | Changing substitutes alters the child profile experience — coordinate first |
| E-31 assignment | `emergenc.y` and `ma.x` hold E[31] — do not add new E[31] signals without approval |
| Never-block contract | `AgeGate.filter()` must never return `None` for CHILD profiles with M-rated signals |
| `source_pillar` value | `"coral.dot_signal_classifier"` is the canonical Coral role identity |
| Operator mapping in `pulse_bridge.py` | The Fire / Solar / Air / Temporal / Water mapping is a BEA system-wide contract |
| `.i` node detection | Standalone capital `I` only — lowercase `i` must never fire the node declaration |
| Reserved nodes | `.t`, `.e`, `.u`, `.a` are reserved — do not assign signals without approval |

---

*BEATEK Holdings, LLC · Founded by Jeremy F. Jackson · © 2026*
*BEA.FREQ™ is part of BEA_Aura_CDE_OS — The signal finds its audience.*
