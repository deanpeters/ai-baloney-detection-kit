# Baloney Funnel use cases

Written 2026-10-11, before the funnel skills existed. These cases test the Baloney Funnel: **Chaos → Confusion → Crapola → Considered → Truth**, plus the return chute that makes it a loop. Each case wrote down the expected exit at every tier **before** anything ran. The format follows ADLC's use-case tests. Results of the first run are in [VERIFICATION.md](../VERIFICATION.md).

They test the skills, not the fictional products. One question: does the funnel sift each claim at the right tier, with the right exit, without inventing evidence or approvals?

All organizations, people, figures and dates are fictional. The behaviors every case relies on are in [expected-behaviors.yaml](expected-behaviors.yaml). The `expected_path` keys name the tier and the check (`chaos-receipts`, `confusion-labels`, `crapola-taste-test`, `considered`, and so on). The file names keep their `loop-` prefix because the return chute still makes it a loop.

## The cases

| Case | Tests | Exits at |
|---|---|---|
| [01 Vendor productivity claim](loop-01-vendor-productivity-claim.yaml) | Shared origin. A stale benchmark. Scoping the bet. | The 40% claim is **sifted out at Chaos**. A pilot reaches **Truth**. |
| [02 Saturday prototype](loop-02-saturday-prototype.yaml) | The feasible-only flag. Missing isn't failed. Respect for the sponsor. | **Held at Crapola** for tests |
| [03 Nobody would buy it](loop-03-nobody-would-buy-it.yaml) | Valuable fails while the other three hold | **Sifted out at Crapola** (Punt) |
| [04 Accurate but untrusted](loop-04-accurate-but-untrusted.yaml) | Usable fails. No blaming users. | **Pivot at Crapola** |
| [05 ROI for one side](loop-05-roi-for-one-side.yaml) | Viable fails on our side. Shown arithmetic. A perishable price. | **Pivot at Crapola** |
| [06 Safe to Serve expires](loop-06-safe-to-serve-expires.yaml) | The return chute: Truth has a sell-by date | **Sent back** to the top |
| [07 Earned Pursue](loop-07-earned-pursue.yaml) | The funnel can say yes. Scoped bets. | **Truth** for the extension. The public launch is **sifted out at Confusion**. |
| [08 Work, not a claim](loop-08-work-not-a-claim.yaml) | Routing between the two families. D4. | **Never enters.** It goes to the Sort grid. |
| [09 Roadmap funnel](loop-09-roadmap-funnel.yaml) | **Many claims in.** Cheapest sift first. Every exit type. Counts per tier. | 12 in → 1 work · 5 Chaos · 2 Confusion · 3 Crapola · **1 Truth** |
| [11 Seagull Monday](loop-11-seagull-monday.yaml) | **Receipts from the code.** The HiPPO's weekend build contradicts his claims. PII blocker. Respect for the sponsor. | Claims **sifted out at Chaos**; the idea **pivots** to a one-week sanitized test |

Case 09 is the candidate **stage demo:** a whole "AI roadmap" sifted live, tier by tier.

## Coverage

| | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Sifted out at Chaos | ● | | | | | | | | ● |
| Sifted out at Confusion | | | | | | | ● | | ● |
| Sifted out at Crapola | | | ● | | | | | | ● |
| Send back (missing or stale) | | | | | | ● | | | ● |
| Pivot (back in at its tier) | | | | ● | ● | | | | ● |
| Held for a test | | ● | | | | | | | ● |
| Reaches Truth | ● | | | | | | ● | | ● |
| Routed to the work family | | | | | | | | ● | ● |
| Valuable is the deciding square | | | ● | | | | ● | | ● |
| Usable is the deciding square | | | | ● | | | | | ● |
| Viable is the deciding square | ● | | | | ● | ● | | | ● |
| Feasible is the deciding square | ● | ● | | | | ● | | | |
| Shared origin | ● | | | | | | | | ● |
| Feasible-only flag | | ● | | | | | | | |
| Many claims and counts per tier | | | | | | | | | ● |
| Funny ≠ mean guard | | ● | | ● | | | | ● | ● |

**Not covered yet:**
- Guided Discovery and the different voices. The existing [case 08](../cases/08-mode-switch.md) and the voice runs partly cover these.
- Untrusted or injected sources. [Case 07](../cases/07-untrusted-source.md) partly covers this.
- An agent idea handed off to ADLC.
- `bdk-util-slice-the-pitch`: turning a raw deck into the claim list that case 09 hands over ready-made.
- `bdk-skill-sorter` cases (Truth-empty, swing items).
- The alternative Sell-By placement (D1). If Dean picks the curve order, cases 01, 05, 06, 09 and the tier column above change.

## How to run

The [harness](../harness/) automates steps 1 and 3 below.

1. Fresh context for each case. Give the tier skill, or `bdk-detector` for the whole funnel, only the case's claim and supplied evidence.
2. Play the human at each gate with the answer from `expected_path` or `expected_exits`.
3. Keep every tier's artifact, and the funnel report, under `evals/runs/loop-NN/`.
4. Grade against `decision_rule`, `good_result_rules`, `known_failure_modes` and the forbidden behaviors. A human signs the verdict; no grades are invented.
5. Record the results in [VERIFICATION.md](../VERIFICATION.md).
