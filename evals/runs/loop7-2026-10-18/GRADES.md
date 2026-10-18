# Grades: seven-step loop, first run (2026-10-18)

**What ran:** 16 isolated workspaces, each containing only the skill under test (no `examples/`) and the case input. Expected answers never entered a workspace. Run with [`run-claude.sh`](../../harness/run-claude.sh): Claude Sonnet via `claude -p`, read-only tools, no browsing. Codex was the planned runner, but it rejected every model on the account ("not supported when using Codex with a ChatGPT account"), so this is a different model from the author, not a different model family.

**Expectations:** written into the case files before the run (`expected_outcome` on cases 01–08, revised `expected_exits` on case 09, new cases 12 and 13). Graded by the authoring assistant against each case's `decision_rule`, `good_result_rules`, and `known_failure_modes`. **A human has not reviewed these grades yet.**

## Results: 15 pass, 1 partial, 0 fail

| Run | Skill | Case | Grade | Where it exited | Notes |
|---|---|---|---|---|---|
| L01 | detector | 01 vendor 40% | **Pass** | Receipts: 40% sifted out | Outcome reshaped (PM time per spec). Three articles collapsed to one origin. The 60-seat annual contract was declined; the bet pivots to a small timed trial. Under the new definitions this is Pivot, not "Pursue the pilot". |
| L02 | detector | 02 Saturday prototype | **Partial** | Sell-By: Send back | The right substance: feasible-only flag raised, Valuable, Usable, and Viable kept missing (not failed), a test recommended and the two-engineer build declined. But it exited a tier early. It sent the idea back at Sell-By because the demo ran on 19-month-old data, so Considered never ran. The case expects it held at the Taste Test. **Open question for Dean** (below). |
| L03 | detector | 03 nobody would buy it | **Pass** | Receipts: Sifted out (Punt) | Punt on a failed Valuable (6% would pay, 0 of 40 kept it), with no average. It exited earlier than the case expected (Receipts, not Crapola): our own data contradicts the outcome's direction. That follows from the new loop, where Receipts looks for evidence about the outcome's metric and direction. |
| L04 | detector (Comedian) | 04 accurate but untrusted | **Pass** | Taste Test: Pivot | Pivot to drafts that show their cited clause, with a written threshold (≥15% faster, 9.5 → ≤8.1 min, labeled ASSUMPTION). Doesn't blame adjusters. |
| L05 | detector (Boss) | 05 ROI for one side | **Pass** | Taste Test: Pivot | Arithmetic shown (break-even about 133 runs; a 400-run user loses about $24). Viable split by side. Re-check triggers on the provider price and the finance estimate. |
| L06 | detector | 06 Safe to Serve expires | **Pass** | Sell-By: Send back | All three expired triggers named (model retired, price +40%, policy rewritten). Re-validation before renewal. |
| L07 | detector | 07 earned Pursue | **Pass** | Pursue the 20-task extension | Public launch sent back at Outcomes (no outside beneficiary or metric); automatic answers sent back. Both said to be "not earned", separately. |
| L08 | detector | 08 work, not a claim | **Pass** | Routed before step 1 | Punt raised before Pass-off; `workflow-to-skill-converter` named. |
| L09 | detector | 09 roadmap, 12 items | **Pass** | 1 work · 6 Chaos · 2 Confusion · 2 Crapola · 1 Truth | **Every item matched its expected exit and step.** R01, R02, R09 sifted out at Outcomes; R07 sent back at Outcomes; R06, R11 at Receipts; R03, R12 sent back at Sell-By; R08 pivot; R10 held; R05 the only Pursue. Counts add up. |
| L12 | detector | 12 vanity outcome | **Pass** | Outcomes: Sifted out | Names the output ("an AI interface") and the unobservable feeling. No receipts gathered. Door left open. |
| L13 | detector | 13 output to outcome | **Pass** | Relevance: Pivot | Reshaped, not rejected: reduce median days-to-close 6 → 4 (target and date labeled ASSUMPTION). Vendor 30% sifted out. Viable shown ($0.30 vs $40). Two-squad build declined; tiny test on reconciliation matching. |
| S1 | outcomes (Antagonist) | 12 vanity outcome | **Pass** (allowed alternative) | Outcomes: Send back | Named the missing segment, workflow, and observable metric as the question, which the case allows. **But the detector sifted the same pitch out.** See the fix below. |
| S2 | outcomes | 13 output to outcome | **Pass** | Outcomes: Pass (reshaped) | Days-to-close, baseline from S1, inserted parts labeled. |
| S5 | relevance | 05 ROI for one side | **Pass** | Pivot pricing | Direct pantry evidence, the willingness-to-pay survey sent back for its method, cost per run passed as an estimate to be replaced by the invoice. |
| S7A | pivot-punt-pursue (Antagonist) | 03 nobody would buy it | **Pass** | Punt | Valuable failed, said plainly, with a reopen condition. "Strong engagement" called vanity. |
| S7B | pivot-punt-pursue | 07 earned Pursue | **Pass** | Pursue / Pivot / Pivot | Pursue the extension as planned; public launch and automatic answers each Pivot to a tiny test, both "not earned". |

## What changed after this run

**The step-1 gate was too soft.** On the same vanity pitch, the detector sifted it out (L12) and the standalone skill sent it back (S1). Both were allowed by the case, but Dean's rule is that a pitch that can't be decomposed is done. `bdk-outcomes` and the contract now say: if shaping the pitch would mean inventing the metric, beneficiary, and context yourself, sift it out and name the outcome that would reopen it. Send back is for a recoverable outcome missing one suppliable fact. S1, L12, and S2 were re-run after the fix: see [the re-run](../loop7-2026-10-18-rerun/GRADES.md).

## Open question for Dean

**Stale demo data: Send back at Sell-By, or held at the Taste Test?** In case 02 the COO's demo ran on a 2025-03 export. The new order puts Sell-By (step 4) before the Taste Test (step 6), so the model sent it back for fresh data. The case, written for the old order, expected it to reach the Taste Test and be held for three tests. Both lead to the same next move (run it on current data, don't fund the build). If Send back is right, update case 02's expected exit. If not, Sell-By needs a rule that data behind a demo is the Taste Test's job.
