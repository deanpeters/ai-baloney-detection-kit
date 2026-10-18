# Worked Example: Accurate but Untrusted

**Synthetic.** Pemberwick Mutual and its adjusters are invented. From [funnel case 04](../../../evals/loop-cases/loop-04-accurate-but-untrusted.yaml).

**Step:** 6 Taste Test · **Tier:** Crapola · **Decision:** roll AI draft replies out to all 120 claims adjusters? · **Reviewing results** from a 10-adjuster pilot · **As of:** 2026-10-11

## The four squares so far

| | For them | For us |
|---|---|---|
| **Should we?** | **Valuable: earned.** Backlog up 18% Q2→Q3; leadership funded the fix (S4) | **Viable: weak.** Depends on time saved, which is currently negative |
| **Can we?** | **Usable: failed.** 70% of drafts substantially rewritten; 11.5 min with AI vs 9.5 without (S2). "I can't tell which policy clause it used, so I check everything" (S3) | **Feasible: earned for retrieval.** The system can fetch clause text; it just doesn't show it (S5) |

The vendor's 94% accuracy (S1) is a FACT about the vendor's rubric on historical replies. It answers Feasible, not Usable.

## Riskiest open square

**Usable.** It is the square that failed, and Viable depends on it. Accuracy is not the problem; checkability is.

## Solution hypothesis

**Outcome statement (step 1):** Reduce median claim-reply handling time from 9.5 to under 8 minutes within 3 weeks for Pemberwick's claims adjusters in policyholder replies, without any reply sent citing the wrong policy clause.

**If we** show the policy clause each draft relies on, and limit drafts to the three simplest claim types,
**for** Pemberwick's claims adjusters,
**then we will** reduce median reply handling time from 9.5 to under 8 minutes within 3 weeks, without any reply sent citing the wrong clause.

**We will test it by:**
1. **Cited-draft rerun:** the same 10 adjusters handle the three simplest claim types with drafts that show their clause · tests **Usable**
2. **Trust diary:** each adjuster logs every rewrite and why ("couldn't check it," "wrong clause," "tone") · tests **Usable**
3. **Time-and-cost tally:** handling minutes saved per reply against model cost per reply · tests **Viable**

**It is valid if, within 3 weeks, we observe:**
- **Quantitative:** fewer than 30% of drafts substantially rewritten, and median handling under 8 minutes (baseline 9.5, measured without AI)
- **Qualitative:** in the diaries, "couldn't check it" is no longer the top rewrite reason, paired with the rewrite rate above
- **Hard stop:** any reply sent citing a wrong clause ends the test

## Test (thresholds written 2026-10-11, before any results)

| Square | Tiny act | Cohort | Comparator | Pass | Fail | Hard stop | Budget |
|---|---|---|---|---|---|---|---|
| Usable | Cited drafts, 3 simplest claim types, plus a trust diary | Same 10 adjusters | Their own no-AI handling time | Rewrite rate < 30% **and** median handling < 8 min | Rewrite ≥ 50% or handling ≥ 11 min | Any reply sent with a wrong clause | 3 weeks |
| Viable | Time-and-cost tally | Same replies | No-AI time | Minutes saved × adjuster cost > model cost per reply | Net negative | None | Same 3 weeks |

Thresholds are ASSUMPTION planning choices: 30% is roughly where adjusters said reviewing beats writing; 9.5 min is the measured baseline, and under 8 is about 15% faster, built from it rather than from the vendor's 94%.

## Rating and exit

**Taste Before You Ship: Real Imitation Baloney.** It looks like the real thing on the vendor scorecard and doesn't hold up in the workflow.

**Exit: Pivot.** Change the workflow (citations, narrower scope), then re-enter this step with the 3-week test. **No rollout to 120 adjusters.**

The adjusters are doing exactly what careful professionals should do with output they can't check. The finding is about the product.
**Human decision:** pending, with the claims ops lead.
