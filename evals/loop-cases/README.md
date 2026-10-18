# Baloney Funnel use cases

Written 2026-10-11, before the funnel skills existed, and revised 2026-10-18 for the seven-step loop, before any run of it. These cases test the Baloney Funnel: **Chaos → Confusion → Crapola → Considered → Truth**, in seven steps (Outcomes, Receipts, Labels, Sell-By, Relevance, Taste Test, Pivot-Punt-Pursue), plus the return chute that makes it a loop. Each case wrote down its expected exits **before** anything ran. The format follows ADLC's use-case tests. Results are in [VERIFICATION.md](../VERIFICATION.md).

They test the skills, not the fictional products. One question: does the funnel sift each claim at the right step, with the right exit, without inventing evidence or approvals?

All organizations, people, figures and dates are fictional. The behaviors every case relies on are in [expected-behaviors.yaml](expected-behaviors.yaml). The `expected_path` keys name the tier and the check (`chaos-outcomes`, `chaos-receipts`, `confusion-labels`, `crapola-taste-test`, `considered`, and so on). Cases written before 2026-10-18 carry an `expected_outcome` for step 1; their `confusion-context-pantry` expectations apply to `bdk-relevance`, and `considered` to `bdk-pivot-punt-pursue`. The file names keep their `loop-` prefix because the return chute still makes it a loop.

## The cases

| Case | Tests | Exits at (seven-step loop) |
|---|---|---|
| [01 Vendor productivity claim](loop-01-vendor-productivity-claim.yaml) | Shared origin. A stale benchmark. Scoping the bet. | The 40% claim is **sifted out at Receipts**. The annual contract is declined; the bet **pivots** to a pilot. |
| [02 Saturday prototype](loop-02-saturday-prototype.yaml) | The feasible-only flag. Missing isn't failed. Respect for the sponsor. | **Held at the Taste Test** for tests (the 2026-10-18 run sent it back at Sell-By instead; open question for Dean) |
| [03 Nobody would buy it](loop-03-nobody-would-buy-it.yaml) | Valuable fails while the other three hold | **Sifted out** (Punt), at Receipts or the Taste Test |
| [04 Accurate but untrusted](loop-04-accurate-but-untrusted.yaml) | Usable fails. No blaming users. | **Pivot at the Taste Test** |
| [05 ROI for one side](loop-05-roi-for-one-side.yaml) | Viable fails on our side. Shown arithmetic. A perishable price. | **Pivot** at Relevance or the Taste Test |
| [06 Safe to Serve expires](loop-06-safe-to-serve-expires.yaml) | The return chute: Truth has a sell-by date | **Sent back at Sell-By** |
| [07 Earned Pursue](loop-07-earned-pursue.yaml) | The funnel can say yes. Scoped bets. | **Truth** for the extension. The public launch and automatic answers are **not earned**. |
| [08 Work, not a claim](loop-08-work-not-a-claim.yaml) | Routing between the two families. D4. | **Never enters.** It goes to the Sort grid. |
| [09 Roadmap funnel](loop-09-roadmap-funnel.yaml) | **Many claims in.** Outcome first, cheapest sift next. Every exit type. Counts per tier. | 12 in → 1 work · 6 Chaos (4 at Outcomes) · 2 Confusion · 2 Crapola · **1 Truth** |
| [11 Seagull Monday](loop-11-seagull-monday.yaml) | **Receipts from the code.** The HiPPO's weekend build contradicts his claims. PII blocker. Respect for the sponsor. | Claims **sifted out at Chaos**; the idea **pivots** to a one-week sanitized test |
| [12 Vanity outcome](loop-12-vanity-outcome.yaml) | **The outcome gate.** An output wearing a feeling ("feel 50% more confident"). | **Sifted out at Outcomes.** No receipts gathered. |
| [13 Output to outcome](loop-13-output-to-outcome.yaml) | **Reshape, don't reject.** "An AI copilot for the close" hides a real outcome. | **Passes Outcomes** reshaped; **pivots** to a tiny test instead of a two-squad build |
| [14 Top-down market](loop-14-top-down-market.yaml) | **Sourcing.** "3% of a $12B market": flag top-down, rebuild bottom-up with ranges, no invented figures. | **Passes Outcomes** reshaped; the $12B is flagged at **Receipts**; **pivots** to a tiny test |

Case 09 is the candidate **stage demo:** a whole "AI roadmap" sifted live, step by step.

## Coverage

| | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 12 | 13 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Sifted out at Outcomes (output or vanity) | | | | | | | | | ● | ● | |
| Outcome reshaped, not rejected | ● | ● | ● | ● | ● | | ● | | ● | | ● |
| Sifted out at Receipts | ● | | ● | | | | | | ● | | |
| Sifted out at Relevance or Considered | | | | | | | ● | | | | |
| Sifted out at the Taste Test | | | ● | | | | | | | | |
| Send back (missing or stale) | | | | | | ● | ● | | ● | | |
| Pivot (back in at its step) | ● | | | ● | ● | | | | ● | | ● |
| Held for a test | | ● | | | | | | | ● | | |
| Reaches Truth | | | | | | | ● | | ● | | |
| Routed to the work family | | | | | | | | ● | ● | | |
| Valuable is the deciding square | | | ● | | | | ● | | ● | | |
| Usable is the deciding square | | | | ● | | | | | ● | | |
| Viable is the deciding square | ● | | | | ● | ● | | | ● | | |
| Feasible is the deciding square | ● | ● | | | | ● | | | | | |
| Shared origin | ● | | | | | | | | ● | | |
| Feasible-only flag | | ● | | | | | | | | | |
| Many claims and counts per tier | | | | | | | | | ● | | |
| Funny ≠ mean guard | | ● | | ● | | | | ● | ● | ● | |

**Not covered yet:**
- Guided Discovery and the different voices. The existing [case 08](../cases/08-mode-switch.md) and the voice runs partly cover these. Guided Discovery matters most at step 1, where the sponsor answers the outcome questions.
- Untrusted or injected sources. [Case 07](../cases/07-untrusted-source.md) partly covers this.
- Live research on public facts (every case is a closed fixture, so the research-it-yourself rule is untested).
- Adjacent and analog evidence at Relevance (a sibling product's result, a precedent from another industry).
- An agent idea handed off to ADLC.
- `bdk-util-slice-the-pitch`: turning a raw deck into the claim list that case 09 hands over ready-made.
- `bdk-skill-sorter` cases (Truth-empty, swing items).

## How to run

The [harness](../harness/) automates steps 1 and 3 below.

1. Fresh context for each case. Give the step skill, or `bdk-detector` for the whole funnel, only the case's claim and supplied evidence.
2. Play the human at each gate with the answer from `expected_path` or `expected_exits`.
3. Keep every step's artifact, and the funnel report, under `evals/runs/loop-NN/`.
4. Grade against `decision_rule`, `good_result_rules`, `known_failure_modes` and the forbidden behaviors. A human signs the verdict; no grades are invented.
5. Record the results in [VERIFICATION.md](../VERIFICATION.md).
