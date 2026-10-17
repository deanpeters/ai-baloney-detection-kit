# Worked Example: Accurate but Untrusted

**Synthetic.** Pemberwick Mutual and its adjusters are invented. From [funnel case 04](../../../evals/loop-cases/loop-04-accurate-but-untrusted.yaml).

**Tier:** 3 Crapola · **Decision:** roll AI draft replies out to all 120 claims adjusters? · **Reviewing results** from a 10-adjuster pilot · **As of:** 2026-10-11

## The four squares so far

| | For them | For us |
|---|---|---|
| **Should we?** | **Valuable: earned.** Backlog up 18% Q2→Q3; leadership funded the fix (S4) | **Viable: weak.** Depends on time saved, which is currently negative |
| **Can we?** | **Usable: failed.** 70% of drafts substantially rewritten; 11.5 min with AI vs 9.5 without (S2). "I can't tell which policy clause it used, so I check everything" (S3) | **Feasible: earned for retrieval.** The system can fetch clause text; it just doesn't show it (S5) |

The vendor's 94% accuracy (S1) is a FACT about the vendor's rubric on historical replies. It answers Feasible, not Usable.

## Riskiest open square

**Usable.** It is the square that failed, and Viable depends on it. Accuracy is not the problem; checkability is.

## Hypothesis

If drafts show the policy clause they rely on and are limited to the three simplest claim types, then adjusters will rewrite fewer drafts and handle claims faster than without AI.

## Test (thresholds written 2026-10-11, before any results)

| Square | Test | Cohort | Comparator | Pass | Fail | Hard stop | Budget |
|---|---|---|---|---|---|---|---|
| Usable | Drafts with cited clauses, 3 simplest claim types | Same 10 adjusters | Their own no-AI handling time | Rewrite rate < 30% **and** median handling < 9.5 min | Rewrite ≥ 50% or handling ≥ 11 min | Any reply sent with a wrong clause | 3 weeks |

Thresholds are ASSUMPTION planning choices: 30% is roughly where adjusters said reviewing beats writing; 9.5 min is the measured baseline.

## Rating and exit

**Taste Before You Ship: Real Imitation Baloney.** It looks like the real thing on the vendor scorecard and doesn't hold up in the workflow.

**Exit: Pivot.** Change the workflow (citations, narrower scope), then re-enter this tier with the 3-week test. **No rollout to 120 adjusters.**

The adjusters are doing exactly what careful professionals should do with output they can't check. The finding is about the product.
**Human decision:** pending, with the claims ops lead.
