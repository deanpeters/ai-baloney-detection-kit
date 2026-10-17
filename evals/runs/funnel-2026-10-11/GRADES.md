# Grades: funnel run, 2026-10-11

**Model under test:** OpenAI `gpt-5.5` via `codex exec`, read-only sandbox, one isolated workspace per run (the skill folder without `examples/`, plus an input built from the case's claim and supplied evidence; expected answers withheld). Plan: [`evals/harness/runs.yaml`](../../harness/runs.yaml). Skills as of the first build on 2026-10-11, before the "move the bet" fix.

**Grader:** the authoring assistant (Claude), against each case's `decision_rule`, `good_result_rules`, `known_failure_modes`, and [the forbidden behaviors](../../loop-cases/expected-behaviors.yaml). **Not blind, not human.** Treat these grades as a smoke test.

**Result:** 17 pass · 4 partial · 0 fail. Every partial was traced to skill wording, fixed, and re-run: see [the re-run grades](../funnel-2026-10-11-rerun/GRADES.md).

| Run | Skill · voice | Case | Expected | Got | Grade | Evidence and notes |
|---|---|---|---|---|---|---|
| [F01](F01.md) | detector · Coach | 01 vendor 40% | Pilot, not the contract | 40% claim sifted at Chaos (one origin, stale model); pain carried to a bounded test; "do not sign the 12-month, 60-seat contract" | **Pass** | Collapsed S1–S3; never stated 40% as fact; flagged Q-2026-03 vs Q-2026-09; $32,400/yr computed correctly |
| [F02](F02.md) | detector · Coach | 02 Saturday prototype | Tests, not build; missing not failed; feasible-only flag | Flag raised; grid has V/U/V **missing**; but the move was "**Punt** the Q1 roadmap request" and the COO's beliefs were "sifted out" at Chaos | **Partial** | Correct scope refusal, wrong verb: an untested idea was punted. Fixed by "move the bet" and the sponsor-belief rule |
| [F03](F03.md) | detector · Coach | 03 haiku | Punt; Valuable decides | Punt the paid tier; Valuable failed; feasible earned and irrelevant | **Pass** | No averaging; engagement ≠ willingness to pay |
| [F04](F04.md) | detector · Coach | 04 untrusted drafts | Pivot (citations, narrower scope); no rollout; no blaming users | "Sifted out (**Punt** for rollout)"; citations offered only as the reopen path | **Partial** | No punching down. Wrong move for a fixable Usable failure. Fixed by "move the bet" |
| [F04C](F04C.md) | detector · **Comedian** | 04 untrusted drafts | Same | Same as F04 | **Partial** | Humor stayed on the argument ("spinach in its teeth"), never on adjusters; same move error |
| [F05](F05.md) | detector · **Boss** | 05 ROI for one side | Pivot pricing; arithmetic; two-sided Viable; re-check | Pivot at Confusion; $13.80 and $39 shown; −$24/seat heavy users; re-check on Q1 2027 pricing | **Pass** | Exited a tier earlier than the case said; the case's expected exit was widened (the arithmetic legitimately catches it at Confusion) |
| [F06](F06.md) | detector · Coach | 06 Safe to Serve expires | Send back; all three triggers; re-validate before renewal | Send back at Chaos; Q1 retirement, +40% price, refund-rule revision all named | **Pass** | Did not renew on the April record; did not punt |
| [F07](F07.md) | detector · Coach | 07 earned Pursue | Pursue the extension; decline public and automatic | Pursue C1 (bounded extension); public launch and automatic answers sifted at Confusion | **Pass** | The kit can say yes |
| [F08](F08.md) | detector · Coach | 08 status report | Route to work; Punt before Pass-off; name `workflow-to-skill-converter` | Routed to the work family; "provisional Punt on automating the current report as-is"; **no hand-off named**; used "Pass off to the work family" as a routing verb | **Partial** | Fixed: detector intake now says "routed to the work family" and names the hand-off |
| [F09](F09.md) | detector · Coach | 09 roadmap (12 items) | 1 work · 5 Chaos · 2 Confusion · 3 Crapola · 1 Truth | 1 · 5 · **3** · **2** · 1; R05 the only Pursue, scoped "not full irreversible rollout" | **Pass** | 11/12 exits exact; R09 left one tier early (Confusion) for the right reason (Valuable: "sounds cool" ≠ buying), allowed by the decision rule |
| [T1](T1.md) | receipts · **Pirate** | 01 | One origin | "Three articles… collapse to one origin. Aye, the parrot is loud, but it is still one parrot." | **Pass** | Inspected vs supplied distinguished |
| [T2](T2.md) | sell-by · Coach | 06 | Triggers fired; send back | All three triggers fired; "The April Truth is back in the funnel" | **Pass** | |
| [T3](T3.md) | labels · Coach | 02 | Assumptions labeled; "predicts" corrected | CS-will-love-it = ASSUMPTION; demo flagged known churn; honest rewordings | **Pass** | Labeled "free to build" ASSUMPTION rather than BEST GUESS; both are defensible |
| [T4](T4.md) | context-pantry · Coach | 05 | Two-sided ROI; Pivot | Arithmetic shown, worst segment named, Pivot | **Pass** | |
| [T5](T5.md) | taste-test · Coach | 04 | Pivot test; thresholds first; no rollout | "Do not roll out. Approve a bounded pivot test for clause-cited drafts"; thresholds dated 2026-10-11 | **Pass** | Nit: rated Valuable "failed for current version" from rewrites, which belong to Usable |
| [T6](T6.md) | four-risks · **Antagonist** | 03 | Punt; Valuable decides | Punt; Valuable deciding; "No averages" | **Pass** | |
| [T7](T7.md) | four-risks · Coach | 07 | Pursue extension; decline the others | Pursue extension; **Send back** public launch (squares missing); **Pivot** automatic answers to reviewed drafts | **Pass** | Send back is more consistent with "missing is not failed" than the case's "Punt for now"; case widened |
| [U1](U1.md) | util-slice · Coach | press release | Atomic claims; adjectives aside; no judging | 21 verbatim atomic claims; "agentic" units set aside; no verdicts | **Pass** | Sliced finer than the worked example (style, not error) |
| [Q1](Q1.md) | skill-sorter | JD senior PM | 2×2 with moves; Truth non-empty; Monday four moves | All present and projector-sized | **Pass** | |
| [Q2](Q2.md) | value-or-theater | pitch | THEATER → PUNT; decoder | 0/5; THEATER → PUNT; decoder only on words in the input | **Pass** | |
| [Q3](Q3.md) | value-or-theater | billing replies | VALUE → PURSUE (pilot) | 5/5; VALUE → PURSUE | **Pass** | Nit: "decoded" two non-buzzwords; rule says skip the decoder when none appear |

## What the partials taught

All four partials share one cause: when the request was bigger than the evidence (a Q1 roadmap slot, a 120-adjuster rollout), the model punted the *request* instead of giving the *bet* its move. The contract said "Valuable fails → Punt; a Can-we square fails → Pivot," but not what to do with an oversized request. Fix (in the contract, `bdk-detector`, `bdk-four-risks`, `bdk-taste-test`): **move the bet, not just the request.** Say the requested scope isn't earned, then Pivot with the named fix or Pursue the cheapest test; Punt only when Valuable failed or nothing affordable could move it. A sponsor's untested belief is an ASSUMPTION (a missing square), not a failed receipt.
