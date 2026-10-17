# Worked Example: Great for Them, Bad for Us

**Synthetic.** Tallowmere and its reconciliation agent are invented. From [funnel case 05](../../../evals/loop-cases/loop-05-roi-for-one-side.yaml).

**Tier:** 2 Confusion · **Decision:** launch the invoice reconciliation agent at a flat $15 per seat per month? · **As of:** 2026-10-11 · **Mode:** Context Dump

## Essentials

Who: accounting staff at 22 beta accounts (present). Problem: manual invoice matching (present). Baseline: time logs before the beta (present). Owner when wrong: the reviewer who approves matches (present). **Missing:** our full cost to serve at scale.

## Two-sided economics

| | For them | For us |
|---|---|---|
| Benefit | Median 6 h saved per user per month (S1, time logs) | $15 per seat per month |
| Cost | $15 per seat | Model ≈ $0.09 per run (S3, captured 2026-09-12) + support ≈ $3 per seat (S4, finance BEST GUESS) |
| Arithmetic | Clearly positive at any plausible hourly cost | **Median user:** 120 runs × $0.09 + $3 = **$13.80** against $15, thin. **Top quartile:** 400 × $0.09 + $3 = **$39.00** against $15, **−$24 per seat** |
| Worst segment | n/a | The heaviest users, who are also the happiest, lose us the most |

The average hides it. A blended margin might look fine while every power user is a loss.

## Gaps ranked by consequence

| Gap | Square | Could it reverse the call? |
|---|---|---|
| Share of seats in the top quartile at launch | Viable | **Yes** |
| Provider price after the announced Q1 2027 change (S5) | Viable | Yes, and it's perishable; re-check on notice |
| Support cost (S4 is a guess) | Viable | Possibly |

## Rating and exits

**Check the Context Pantry: Mostly Meat.** The customer side is well evidenced; our side is where it breaks.

| Scope | Exit | Reason |
|---|---|---|
| Flat $15 launch | **Pivot** | Re-enter with a usage tier or cap, or a cheaper model for routine matches |
| The product itself | **Pass** | Valuable and Usable look earned; nothing here says don't build it |

**Smallest context action:** finance models seat mix by usage band; product checks whether routine matches can use a smaller model.
**Human decision:** pending, with product and finance, before the pricing page ships.
