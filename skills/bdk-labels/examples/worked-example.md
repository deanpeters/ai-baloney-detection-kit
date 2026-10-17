# Worked Example: The Churn Whisperer

**Synthetic.** Fennimore Freight and its COO are invented. From [funnel case 02](../../../evals/loop-cases/loop-02-saturday-prototype.yaml).

**Tier:** 2 Confusion · **Decision:** put the weekend-built churn flagger on the Q1 roadmap with two engineers? · **As of:** 2026-10-11 · **Mode:** Context Dump, unattended

## Ledger

| ID | Atomic claim | Label | Basis | Status | Square |
|---|---|---|---|---|---|
| C1 | The prototype flags 23 of 200 accounts with plausible reasons | FACT | Demo recording, 2026-10-06 | Supported | Feasible |
| C2 | 11 of the 23 flagged accounts had already churned when the CSV was exported | FACT | CSV is a 2025-03 export (S2) | Supported | Feasible |
| C3 | The flagger predicts churn | INFERENCE, weak | From C1, but C2 shows half the "predictions" were already history | Contradicted in part | Feasible |
| C4 | Customer success will love it | ASSUMPTION | COO's note; no CSM has seen it | **Missing** | Valuable, Usable |
| C5 | It's basically free to build | BEST GUESS | Ignores live data access, PII handling, upkeep | Missing | Viable, Feasible |

## Corrections

| Claim | Honest wording |
|---|---|
| C3 | "Flags accounts with plausible reasons on a 2025 sample; predictive value untested on current data." |
| C4 | "We think CSMs might act on these flags; none has seen them." |
| C5 | "The demo was cheap. Running it on live, PII-bearing notes hasn't been costed." |

## Squares

Valuable and Usable: held up only by an assumption (C4), so **missing**. Viable: a best guess (C5), so **missing**. Feasible: **weak**, because buildable on an old CSV is not the same as feasible with our data and constraints.

## Rating and exits

**Label the Lunch Meat: Real Imitation Baloney.** The facts are real; the decision rests on the unlabeled parts.

| Claim | Exit | Reason |
|---|---|---|
| C3 | Send back | Re-run on current notes before calling it prediction |
| C4 | Send back | Show five CSMs ten current flags; ask what they'd do |
| C5 | Send back | Cost the data access and PII review |

Nothing here is sifted out. Missing is not failed. The idea is untested, not wrong.
**Human decision:** pending, with the CS lead and the COO.
