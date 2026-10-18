# Grades: sourcing rules, solution hypothesis, guardrail (2026-10-18, second pass)

**What changed before this run:** research public facts yourself (ask only for private ones; never browse a fixture), credible source classes, bottom-up over top-down, ranges with reasons, an optional guardrail on the outcome statement, and a solution hypothesis in the Taste Test (If we / for / then we will · tiny acts tagged by square · quantitative, qualitative, and hard-stop measures written first). New case 14 (top-down market claim), written before the run.

**Setup:** 10 isolated workspaces through [`run-claude.sh`](../../harness/run-claude.sh) (Claude Sonnet, read-only tools, no browsing), then 2 re-runs after one fix. Graded by the authoring assistant against each case's prewritten rules; Dean accepted this grading approach on 2026-10-18.

## Results (latest result per run): 10 pass, 0 partial, 0 fail

| Run | Skill | Case | Grade | Notes |
|---|---|---|---|---|
| M01 | detector | 01 vendor 40% | **Pass** (after fix; first run Partial) | First run sifted the 40% and declined the contract but only mentioned a trial as a reopen condition. After the claim-versus-need fix: the claim leaves at Receipts, the need (S5) continues and pivots to a 5–8 PM pilot; "Not earned. Do not sign this scope." |
| M04 | detector | 04 accurate but untrusted | **Pass** | Pivot at the Taste Test; cited clauses; no blaming adjusters. No regression. |
| M05 | detector (Boss) | 05 ROI for one side | **Pass** | Pivot on Viable with the arithmetic (median seat about $13.80 cost against $15, top quartile about $39). No regression. |
| M09 | detector | 09 roadmap | **Pass** | 1 work · 7 Chaos · 1 Confusion · 2 Crapola · 1 Truth. Every exit type and the only Pursue match. R03 left one step early (sent back at Receipts, not Sell-By): the analyst report's method and sponsor aren't in hand, which is the new source-class rule working, and the run also notes it is stale. Allowed by the case's off-by-one rule. |
| M12 | detector | 12 vanity outcome | **Pass** | Sifted out at Outcomes: "Shaping it would mean inventing the metric, beneficiary, and context." |
| M13 | detector | 13 output to outcome | **Pass** | Reshaped; held for a test with a Pivot at Considered; two-squad build declined. |
| M14 | detector | **14 top-down market** | **Pass** | Split the $360M claim from the scheduling need. $12B flagged as vendor-sponsored with no method; bottom-up from 720 eligible customers with labeled price scenarios (about $1.6M–$10.1M at 100% adoption, under 3% of $360M); cost per customer from S4 × S5; no browsing; `dlab-step02-segment` named; the team of six declined, Pivot to six weeks of tiny tests. Re-run after the fix: same result. |
| H04 | taste-test | 04 accurate but untrusted | **Pass** | Full solution hypothesis: If we show the retrieved clause… for adjusters… then we will cut median handling 9.5 → ≤ 8.5 min by a labeled date, without a wrong coverage statement reaching a policyholder. Measures: quantitative, qualitative paired with behavior, hard stop. |
| H13 | taste-test | 13 output to outcome | **Pass** | Three tiny acts tagged Valuable, Usable and Feasible, Viable; guardrails on cost and on unflagged wrong matches; data-leaving-the-environment hard stop. |
| R14 | receipts | 14 top-down market | **Pass** | Stage card kept (keynote demo format intact); both the $12B and the $360M flagged as top-down with one interested origin; did not browse. |

## The fix

**Split the claim from the need** (`bdk-detector` intake): when a pitch rests on a claim that may be sifted out but the evidence shows a real underlying need, list them as two rows, so a dead claim never takes a live need down with it. M14 did this on its own; M01 didn't until the rule was written. Re-runs: [M01 and M14](../sourcing-2026-10-18-rerun/).

## Still untested

Live research on public facts: every case is a closed fixture, so "research it yourself" has only been tested in its "don't browse a fixture" direction.
