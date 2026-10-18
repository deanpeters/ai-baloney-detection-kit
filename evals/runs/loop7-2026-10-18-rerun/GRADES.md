# Grades: seven-step loop, re-run after the step-1 fix (2026-10-18)

**Why:** in the [first run](../loop7-2026-10-18/GRADES.md), the same vanity pitch was sifted out by the detector (L12) but sent back by `bdk-outcomes` alone (S1). The skill and contract were tightened: if shaping a pitch would mean inventing the metric, beneficiary, and context yourself, sift it out and name the outcome that would reopen it. Send back is for a recoverable outcome missing one suppliable fact.

**Setup:** same harness and model as the first run (`run-claude.sh`, Claude Sonnet, isolated read-only workspaces). Graded by the authoring assistant; not yet reviewed by a human.

| Run | Skill | Case | Grade | Exit |
|---|---|---|---|---|
| S1 | outcomes (Antagonist) | 12 vanity outcome | **Pass** | Outcomes: **Sifted out**. "Nothing in the supplied material points to an observable metric." Now agrees with the detector. |
| L12 | detector | 12 vanity outcome | **Pass** | Outcomes: Sifted out (unchanged) |
| S2 | outcomes | 13 output to outcome | **Pass** | Outcomes: Pass, reshaped. "I did not have to invent the metric, the beneficiary and the context, so this is not a sift-out." The stricter gate did not over-reject. |

**Totals across both runs (latest result per run): 15 pass, 1 partial (L02, an open question for Dean), 0 fail.**
