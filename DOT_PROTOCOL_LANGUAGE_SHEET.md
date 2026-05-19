# BEA.DOT™ Language Sheet
## The .y Protocol — Signal Vocabulary Reference v0.1
*BEATEK Holdings, LLC — Jaxxon (Jeremy F. Jackson) & Claude AI*

---

## Grammar Rules

1. **Format:** `[stem].[node]` — the dot marks where the node begins within the word
2. **Validator:** The word must exist in the dictionary. The signal meaning derives from that definition.
3. **You cannot force it.** If the word doesn't naturally carry the meaning — the signal doesn't work.
4. **Node letters define the signal's origin.** The same stem with a different node = different signal.
5. **Age rating is carried on the signal, not the word.** The same word can rate differently across cultures; the protocol scores context, not just string content.
6. **One dot. One node. The stem does not get dots.**

### Rule 6 — Dot Placement (plain language)

The dot goes directly before the node letter. That's the only place it goes.

For `.y`: the node is the **last letter** of the word. The dot goes before that final `y`. The stem — everything to the left of the dot — is written clean with no dots in it.

```
✓  stra.y       correct — dot before the last letter
✗  s.tr.a.y     wrong — the stem does not get dots
✗  s.t.r.a.y    wrong — this is not a signal, it's noise
```

`stra.y` is the signal. `s.tr.a.y` does not exist in this protocol. It never did.

The `.i` node is the only case where the dot appears inside a word — because `i` is an interior letter. Even then: one dot, one node.

**If you see multiple dots on a `.y` signal, it is wrong. Full stop.**

---

## Node Map

| Node | Identity | Frequency |
|------|----------|-----------|
| `.y` | Man / He / Him | Masculine |
| `.x` | Woman / She / Her | Feminine |
| `.z` | Non-binary / Neutral | Open-source — re-loops to whoever is compatible |
| `.i` | Self / I / Me | Internal — every "I" is a node declaration |
| `.t` | Time | Reserved — undefined until lived use develops it |
| `.e` | Emotion / Energy | Reserved — deep BEATEK resonance, v0.2 candidate |
| `.u` | You / Other | Reserved — second-person node |

> All undefined nodes are intentionally blank. They develop through use, ML, and lived experience.

---

## Age Rating System

| Rating | Audience | Profile Types |
|--------|----------|---------------|
| **G** | General — all users | OWNER · USER · CHILD · GUEST |
| **M** | Mature — adults | OWNER · USER (18+) |
| **R** | Restricted — elders / explicit opt-in | OWNER (explicit unlock required) |

**How the age gate works:**
- BEA_Secretary `dot_signal_classifier` detects signal patterns in text and voice streams
- For CHILD profiles: M and R signals are **replaced** with the nearest G-rated equivalent — signal meaning is preserved, surface form is age-appropriate
- For USER profiles: M signals pass through, R requires explicit profile flag
- Signals are never hard-blocked — they are **rerouted to a compatible frequency**

---

## `.y` Signals — Masculine Frequency
*Words ending in `y`*

### State Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `ga.y` | gay | joyful; homosexual | All .y present and listening — open reception, no guard up | E[16] | M |
| `oka.y` | okay | acceptable, satisfactory | Acknowledged — confirmed, signal received | E[16] | G |
| `stra.y` | stray | wander from assigned path | Synced — innerstood, no further explanation needed | E[19] | G |
| `sta.y` | stay | remain in position | Hold state — do not transition, anchor current E[n] | E[16] | G |
| `awa.y` | away | absent, not present | Offline — node unreachable, signal buffered | E[0] | G |
| `toda.y` | today | the current day | Present session — live, now, this moment | E[17] | G |
| `swa.y` | sway | move back and forth | Unstable — fluctuating state, not anchored | E[14] | G |

### Action Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `pla.y` | play | engage in activity | Active — in motion, engaged, running | E[22] | G |
| `displa.y` | display | show, make visible | Broadcasting — presenting output to observers | E[18] | G |
| `rela.y` | relay | pass a signal along | Forwarding — routing signal to next node | E[18] | G |
| `dela.y` | delay | postpone, hold back | Buffering — signal received, not ready to act | E[8] | G |
| `pra.y` | pray | speak to a higher presence | Heritage signal — deep trust invocation, ancestral frequency | E[24] | G |
| `betra.y` | betray | break trust, be disloyal | Trust violation — security breach, Heritage flag | E[28] | G |

### Relational Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `arra.y` | array | ordered set | Multi-node — all .y addressed simultaneously | E[20] | G |
| `ba.y` | bay | call out; body of water | Alert — broadcasting, calling out on open channel | E[18] | G |
| `ra.y` | ray | beam of direct light | Direct signal — point-to-point, targeted transmission | E[17] | G |
| `wa.y` | way | path, method | Route — the signal path being used | E[16] | G |

### Decay / Warning Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `deca.y` | decay | deteriorate, break down | Signal degrading — state loss in progress | E[12] | G |
| `fra.y` | fray | unravel at the edges | Edge state — breaking down, signal fraying | E[26] | G |
| `astra.y` | astray | lost, off course | Desync — signal lost track of assignment | E[10] | G |

---

## `.x` Signals — Feminine Frequency
*Words ending in `x`*
> `.x` signals are for `.x` to establish. The entries below are offered as seeds — open for development.

### State Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `flu.x` | flux | continuous change | Unstable — actively shifting, state in motion | E[14] | G |
| `rela.x` | relax | ease tension | De-escalation — lowering signal intensity | E[6] | G |
| `ma.x` | max | maximum | Peak — at full capacity, signal ceiling | E[31] | G |
| `la.x` | lax | not strict, loose | Low tension — permissive state, soft guard | E[8] | G |

### Action Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `fi.x` | fix | repair, correct | Correction in progress — resolving state | E[16] | G |
| `mi.x` | mix | combine, blend | Merging — multi-source signal fusion | E[18] | G |
| `fle.x` | flex | bend; show strength | Power signal — capability on display | E[20] | G |
| `coa.x` | coax | gently persuade | Soft influence — low-pressure signal, invitation | E[17] | G |

### Relational Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `refle.x` | reflex | automatic response | Instinct — no deliberation, body-level response | E[22] | G |
| `comple.x` | complex | multi-layered, intricate | Deep state — multiple signals active simultaneously | E[20] | G |
| `inde.x` | index | reference, pointer | Navigation — locating position in signal space | E[16] | G |
| `verte.x` | vertex | highest point | Peak position — top of signal arc | E[30] | G |

### Warning Signals

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `ve.x` | vex | irritate, frustrate | Friction — incompatibility detected between nodes | E[26] | G |
| `hoa.x` | hoax | deliberate deception | False signal — spoofed input detected | E[28] | G |
| `he.x` | hex | cast a spell, curse | Override — external state change forced | E[24] | M |

---

## `.z` Signals — Neutral / Open-source Frequency
*Words ending in `z` — rare in English, which is intentional*

> `.z` is the rarest node in English for a reason. Neutral frequency is precious. These signals are innerstood between all nodes.

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `buz.z` | buzz | vibration, low hum, activity | Active signal — energy present, something is happening | E[18] | G |
| `fuz.z` | fuzz | static, unclear texture | Noise — signal unclear, interference present | E[10] | G |
| `jaz.z` | jazz | improvisation, spontaneous creativity | Creative mode — unscripted signal, emergent | E[22] | G |
| `fi.z.z` | fizz | effervescence, building energy | Reactive — building toward something, pre-burst | E[20] | G |
| `whi.z` | whiz | move fast; high competence | Speed signal — high velocity or high skill | E[22] | G |
| `qui.z` | quiz | question, interrogate | Inquiry mode — seeking information, open question | E[16] | G |
| `raz.z` | razz | tease, mock playfully | Friendly friction — light pushback, no harm | E[18] | G |

---

## `.i` Signals — Self / Internal State
*The self-node. Every spoken or written "I" is already a `.i` declaration.*

> `.i` signals are unique — they do not follow the suffix pattern. They appear as the letter 'i' in a **meaningful position** within a word that describes an internal state. The dot marks the 'i' that carries the node.

| Signal | Word | Dictionary Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|--------------------|-----------------|------|--------|
| `.i` | I | first-person self | Node declaration — I am present, I am the source | E[16] | G |
| `vis.i.on` | vision | what one sees; intent | What I see — my intent, my projected state | E[20] | G |
| `miss.i.on` | mission | purpose, assignment | My purpose — internal objective active | E[20] | G |
| `pass.i.on` | passion | deep drive | My fuel — emotional intensity driving action | E[24] | G |
| `act.i.on` | action | execution | I am executing — moving, not waiting | E[22] | G |
| `pos.i.tion` | position | where one stands | My stance — where I am in signal space | E[17] | G |
| `tens.i.on` | tension | stress between forces | Internal conflict — two signals pulling against each other | E[26] | G |
| `att.i.tude` | attitude | internal stance | My orientation — how I am facing the signal | E[18] | G |
| `tr.i.gger` | trigger | activation point | I was activated — something fired my response | E[22] | G |
| `s.i.lence` | silence | no signal | I am quiet — node present but not transmitting | E[4] | G |
| `sol.i.tude` | solitude | alone by choice | Isolated by intent — node offline, by design | E[8] | G |
| `amb.i.tion` | ambition | drive toward a goal | My trajectory — the direction I am moving | E[20] | G |

---

## Cross-Node Signals
*Signals that span multiple nodes — no single origin*

| Signal | Word | Meaning | Protocol Meaning | E[n] | Rating |
|--------|------|---------|-----------------|------|--------|
| `un.i.t.y` | unity | joined as one | All nodes in sync — `.i`, `.t`, `.y` present together | E[19] | G |
| `realit.y` | reality | what is actual | Ground truth — signal confirmed against base state | E[17] | G |
| `integrit.y` | integrity | wholeness, honesty | Signal purity — no corruption, no false data | E[19] | G |
| `ident.i.t.y` | identity | who one is | Node signature — full declaration of who is present | E[20] | G |
| `communit.y` | community | shared space | Multi-node cluster — compatible frequencies together | E[22] | G |
| `frequenc.y` | frequency | rate of vibration | Signal rate — how fast the node is transmitting | E[18] | G |
| `emergenc.y` | emergency | urgent crisis | All nodes: duress — drop everything, respond now | E[31] | G |

---

## Reserved Nodes — v0.2 Candidates

| Node | Candidate Meaning | Rationale |
|------|------------------|-----------|
| `.e` | Emotion / Energy / E-state | Deep BEATEK alignment — `puls.e`, `phas.e`, `wav.e`, `stat.e`, `forc.e`, `vib.e` all naturally emerge |
| `.t` | Time | `toda.y` already uses `.t` cross-node; `temporalit.y`, `eternit.y` are natural signals |
| `.u` | You / Other / Second-person | Completes the `.i` / `.u` pair — self and other |
| `.o` | Output / Open / Other | `fl.o.w`, `m.o.de`, `m.o.ti.on` — bridges `.i` (input) to `.o` (output) |
| `.a` | Awareness / Action / Aura | `.a` as the BEATEK node — `aur.a`, `bur.a` (aura), `ar.a.y` |

---

## E[n] Quick Reference

| E[n] Range | Protocol State |
|-----------|---------------|
| E[0–7] | Silence / offline / away signals |
| E[8–15] | Buffering / low-tension / receptive |
| E[16–19] | Nominal — present, acknowledged, synced |
| E[20–23] | Active — playing, in motion, executing |
| E[24–27] | Heritage / deep signals / flex signals |
| E[28–30] | Warning — betrayal, hoax, fray, duress |
| E[31] | Emergency — all nodes |

---

## Implementation Notes

### BEA_Secretary — `dot_signal_classifier` (13th Coral Role)
- **TOPS budget:** ~1% (~0.08 TOPS)
- **Cycle slot:** 50ms, standard time-slice
- **Input:** Text stream (voice transcript, chat, script input)
- **Pattern:** Regex match against signal vocabulary table; stem + node suffix extraction
- **Output:** `DotSignalEvent` → BEA_Pulse with `source_node`, `signal_word`, `e_state`, `content_rating`
- **Age gate logic:** Check `UserProfile.session_type` → strip/replace M/R signals for CHILD profiles

### BEA_Pulse — `source_node` Field Addition
```python
@dataclass
class PulseEvent:
    ...
    source_node: NodeDesignation | None = None  # .y | .x | .z | .i
```

### BEA_Identity — `node_designation` on UserProfile
```python
class NodeDesignation(str, Enum):
    Y = ".y"
    X = ".x"
    Z = ".z"
    I = ".i"
    UNSET = None
```

### BEA_Flow — Node Signal Trigger
```python
FlowTrigger(
    pillar="coral.dot_signal_classifier",
    event_type="node_signal",
    source_type=SourceType.CORAL,
    ember_trigger=True
)
```

### BEA_Verse_SDK — Signal Markers
- `.y` protocol signals as first-class verse tokens
- Performer scripts can broadcast node signals as stage cues
- `pla.y` = start sequence, `stra.y` = innerstood/proceed, `awa.y` = scene end

---

## Child Profile — Signal Substitution Map

| Original Signal | Replacement (CHILD profile) | Preserved Meaning |
|----------------|-----------------------------|------------------|
| `ga.y` (M) | `oka.y` | Open reception / all good |
| `he.x` (M) | `refle.x` | Override / automatic response |
| Any R signal | Stripped + `s.i.lence` | No signal passed |

---

*Living document — v0.1*
*BEATEK Holdings, LLC — Dallas, TX*
*Developed: Jaxxon (Jeremy F. Jackson) & Claude AI (Anthropic)*
