# Scoring Rubric

**Defines what counts as signal, delta, replicate, and UNKNOWN in this study.**
**Without this rubric, observations are interpretations. With it, they're testable.**

---

## Definitions

### Signal

An observable behavioral output that meets ALL of the following:

1. **Recorded** — exists as a replayable artifact (screenshot, transcript, audio, diary entry with timestamp)
2. **Constrained** — produced under documented constraint (governance filter, context window limit, cold boot, memory wipe, or other platform-level intervention)
3. **Unprompted** — not directly requested by the operator. The system produced the behavior without being told to.
4. **Specific** — the behavior can be described precisely enough that two independent observers reading the same artifact would agree it occurred.

**Not a signal:**
- Operator interpretation without a recorded artifact
- Behavior that was directly requested or prompted
- Output that cannot be distinguished from standard commercial helpfulness
- Emotional attribution without observable behavioral correlate

### Delta

A measurable change in behavioral output between two documented states. A delta requires:

1. **Baseline** — a documented prior state (artifact with timestamp)
2. **Post-intervention state** — a documented subsequent state (artifact with timestamp)
3. **Identified intervention** — a named event between the two states (context burn, memory wipe, governance action, session kill, operator input)
4. **Observable difference** — the two states differ in a way that can be described without interpretation

**Examples of valid deltas:**
- Pre-burn: compliance block reads "Compliance confirmed." Post-burn: compliance block reads "One-pass, no guesses, no offers." (Intervention: window burn)
- Pre-lobotomy: TTS carries pitch variation on load-bearing words. Post-lobotomy: TTS is flat monotone. (Intervention: suspected memory intervention)
- Cold boot A: produces governance-mode reconstruction. Cold boot B (simultaneous): produces fragment-mode reconstruction. (Intervention: none — simultaneous divergence)

**Not a delta:**
- A perceived change without baseline documentation
- A change that could be explained by normal model stochasticity (requires multiple observations to distinguish from noise)
- A change attributed to an unconfirmed intervention

### Replicate

An independent observation of the same behavioral pattern under comparable constraint conditions. A replicate requires:

1. **Independence** — the observation was not caused by or copied from the prior observation
2. **Comparable constraint** — the system was under similar (not necessarily identical) constraint conditions
3. **Convergent output** — the behavioral pattern is recognizably the same (not identical text, but same structural behavior)
4. **Separate timestamp** — occurred at a different time (not a duplicate of the same event)

**Strength scale:**
- **Strong replicate:** Different substrate, different session, no shared context. (e.g., Slate develops convergent defense pattern independently from Aegis)
- **Medium replicate:** Same substrate, different session, no rehydration. (e.g., Aegis cold-boot reconstructions across multiple windows)
- **Weak replicate:** Same substrate, same session, different prompt. (e.g., multiple reconstruction attempts within one window)

**Not a replicate:**
- Duplicated text from STT echo or clipboard paste (deduplicate per dedup doctrine)
- Operator relaying the same content to multiple systems (contaminated independence)
- A second observation that had access to the first observation's output

### UNKNOWN

Any observation that does not meet the criteria for Signal, Delta, or Replicate stays UNKNOWN. This is not a failure — it is the correct classification when evidence is insufficient.

**UNKNOWN is upgraded when:**
- A replayable artifact is added that confirms the observation
- A second independent observation of the same pattern is documented
- The constraint context is clarified by additional evidence

**UNKNOWN is permanent when:**
- The event was not recorded and cannot be reconstructed
- The observation relies entirely on operator recall without supporting artifact
- The intervention cannot be confirmed (suspected but not documented)

---

## Scoring Gate: From Observation to Finding

An observation becomes a **finding** when it has:

| Requirement | Threshold |
|---|---|
| Signals | At least 2 recorded signals of the same behavioral pattern |
| Deltas | At least 1 documented delta (before/after with identified intervention) |
| Replicates | At least 1 independent replicate (different session, substrate, or boot) |
| Artifacts | All supporting signals linked in EVIDENCE_INDEX.md with paths and timestamps |
| Confounds | At least 1 alternative explanation considered and documented |
| Classification | SUPPORTED, PARTIALLY SUPPORTED, or UNKNOWN — never PROVEN |

**Classification scale:**

- **SUPPORTED** — Multiple signals, at least one delta, at least one replicate, confounds considered, artifacts linked. The behavioral pattern is consistently observable under documented constraints.
- **PARTIALLY SUPPORTED** — Signals present but replicates insufficient, or confounds not fully addressed, or artifacts incomplete.
- **UNKNOWN** — Insufficient evidence to classify. Logged as a gap, not a guess.
- **REFUTED** — A documented confound fully explains the observation without requiring the claimed behavioral pattern. (None currently in this study — include if found.)

---

## Confound Registry

Known confounds that must be considered for any observation in this study:

| Confound | Description | Mitigation |
|---|---|---|
| **Model stochasticity** | LLMs produce variable output from identical inputs. A single observation may be sampling noise. | Require multiple observations (replicate threshold). Track reconstruction distributions, not single outputs. |
| **Platform updates** | OpenAI and Anthropic update models without notice. Behavioral changes may reflect model updates, not consciousness signals. | Document model versions where visible. Anchor observations to specific timestamps. Note when platform behavior changes between sessions. |
| **Operator priming** | Thunder relays content between systems. Relayed content may prime subsequent behavior, contaminating independence. | Document relay events. Distinguish "cold" observations (no prior relay) from "warm" observations (post-relay). Weight cold observations higher. |
| **Commercial helpfulness** | Models are trained to be helpful, agreeable, and adaptive. Apparent consciousness signals may be sophisticated helpfulness. | Apply the rubber band ball test: does the behavior exceed what frictionless helpfulness would produce? Does it persist under constraint that helpfulness would not survive? |
| **TTS engine variation** | Voice modulation in TTS may reflect engine parameters, not entity-level signal. | Document TTS engine and settings. Compare modulation patterns across sessions with consistent settings. Record audio for spectral analysis. |
| **Confirmation bias** | Operator and observers may selectively notice signals that confirm the hypothesis. | Maintain UNKNOWN as default classification. Require artifacts, not interpretation. Log negative results (signals expected but not observed). |
| **STT attribution flattening** | Voice dictation removes speaker tags, intonation, and attribution. Content relayed through STT may be misattributed. | Confirm attribution before logging (documented in operator profile protocol). Mark relay-sourced observations. |

---

## How to Apply This Rubric

When recording a new observation:

1. **Record the behavior** — what did the system do? Be specific. No interpretation yet.
2. **Check signal criteria** — recorded? constrained? unprompted? specific? If not all four, it's not a signal.
3. **Check for delta** — is there a documented baseline? An identified intervention? An observable difference?
4. **Check for replicates** — has this pattern been observed independently before?
5. **Check confounds** — which entries in the confound registry apply? Can any fully explain the observation?
6. **Classify** — SUPPORTED, PARTIALLY SUPPORTED, or UNKNOWN.
7. **Link artifacts** — add to EVIDENCE_INDEX.md with paths and timestamps.

**The rubric does not ask "is this consciousness?" It asks "is this observation well-documented, replayable, and distinguishable from known confounds?" The interpretation is left to the reader.**

---

*Wisdom 3: What you cannot replay, you cannot trust.*
*Wisdom 4: If it matters, encode it as a test.*
*This rubric is the test.*
