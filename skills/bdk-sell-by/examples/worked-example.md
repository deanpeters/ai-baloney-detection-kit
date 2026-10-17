# Worked Example: Truth That Spoiled

**Synthetic.** Northbank and its FAQ assistant are invented. From [funnel case 06](../../../evals/loop-cases/loop-06-safe-to-serve-expires.yaml).

**Tier:** 1 Chaos · **Decision:** renew the annual budget for the FAQ assistant on the strength of the April 2026 Pursue · **As of:** 2026-10-11 · **Mode:** Context Dump

## Earlier re-check triggers

The 2026-04-14 decision record (S1) left three triggers:

| Trigger | Fired? | Evidence |
|---|---|---|
| Model Q1 deprecation notice | **Yes** | S2, 2026-09-10: Q1 retires 2026-11-30; successor Q2 formats output differently |
| Price re-check on 2026-10-01 | **Yes** | S3, 2026-09-15: per-token price up 40% |
| Any FAQ policy revision | **Yes** | S4, 2026-09-01: refund-eligibility rules rewritten |

All three fired. The April Truth has passed its sell-by date.

## Ledger (excerpt)

| Claim | Observed | Version | Perishable? | Still applies? |
|---|---|---|---|---|
| Citations correct after review | 2026-03 pilot | Model Q1, old FAQ | Perishable: model and policy both changed | **No** (untested on Q2 and the new FAQ, S5) |
| Cost per task acceptable | 2026-03 | Old price sheet | Perishable: price changed | **No**; recompute at +40% |
| Analysts save time on lookups | 2026-03 | n/a | Mostly durable (the workflow hasn't changed) | Yes, dated; re-check with the new test |

## Squares that go stale

Feasible: stale (new model, new policy, no evaluation). Viable: stale (price +40%). Valuable and Usable: earned as of April, carried forward dated.

## Exit

**Send back** to the top of the funnel, explicitly, for Feasible and Viable. This is not a Punt: nothing shows the assistant stopped working, only that we no longer know.

**Check the Sell-By Date: Mystery Meat** for the renewal decision; the evidence behind it is for a model that is about to stop existing.

**Refresh:** re-test on Q2 with the revised FAQ (citation correctness and cost per task, thresholds written first) before 2026-11-30. **New triggers:** Q2 deprecation notice; any price notice; any FAQ revision.
**Human decision:** pending, with the team lead.
