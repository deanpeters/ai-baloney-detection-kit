# Worked Example: Twelve Roadmap Ideas, One Truth

**Synthetic.** Marrowgate Software and its roadmap are invented. From [funnel case 09](../../../evals/loop-cases/loop-09-roadmap-funnel.yaml).

**What went in:** the twelve items on a Q1 slide titled "Our AI Roadmap," each with the one evidence line the team has. · **Decision:** which deserve Q1 investment · **As of:** 2026-10-11 · **Mode:** Context Dump, unattended

## The funnel at a glance

| Stage | Count | Claims |
|---|---|---|
| Entered | **12** | R01–R12 |
| Routed to the work family | 1 | R04 |
| **Chaos**: left | 5 | sifted out R01, R06, R11 · sent back R03, R12 |
| **Confusion**: left | 2 | sifted out R02 · sent back R07 |
| **Crapola**: left | 3 | pivot R08 · sifted out R09 · held for a test R10 |
| **Considered**: reached **Truth** | **1** | R05 |

1 + 5 + 2 + 3 + 1 = 12.

## One line per claim

| ID | Claim | Left at | Exit | Reason |
|---|---|---|---|---|
| R04 | AI-written internal release notes | before the funnel | Work family | A ceremony with 4 readers: Sort grid, Punt if nobody reads it, else Pass-off (`workflow-to-skill-converter`) |
| R01 | "Agentic everything" | Chaos | Sifted out | A slogan; there is no claim to check |
| R06 | Pricing optimizer "boosts revenue 20%" | Chaos | Sifted out | Four sources, one origin: a vendor webinar |
| R11 | "AI replaces tier-1 support by Q3" | Chaos | Sifted out | One vendor pitch behind a consequential workforce claim |
| R03 | Meeting notes "save 5 hours a week" | Chaos | Send back | Real receipt, 2023 data, retired model; refresh it rather than kill it |
| R12 | Internal code-review bot, −15% PR cycle time | Chaos | Send back | Our own trial, but on a model and plugin since replaced; re-run it |
| R02 | Copilot sidebar | Confusion | Sifted out | "A competitor announced it" is a FACT; "our customers want it" is an unsupported ASSUMPTION. Hand-off: `mi-build-battle-card` |
| R07 | Churn prediction | Confusion | Send back | Good offline accuracy, but no owner and no defined action on a flag |
| R08 | Onboarding assistant | Crapola | Pivot | Valuable earned (8/10 struggle); Usable failed (3/5 won't accept auto-configured permissions). Show changes before applying them, re-test |
| R09 | Voice commands for dashboards | Crapola | Sifted out | Valuable failed: "sounds cool" with zero demand signals |
| R10 | Contract summarizer | Crapola | Held for a test | Valuable weak (3 requests); Viable missing ($0.60 a document, no price). Test willingness to pay with the 3 requesters |
| R05 | Smart help-doc search | Considered | **Pursue → Truth** | All four squares earned at 10% traffic against prewritten thresholds |

## Survivor: R05 smart help-doc search

| | For them | For us |
|---|---|---|
| **Should we?** | **Valuable: earned.** 38% of tickets are how-to questions already answered in docs | **Viable: earned.** $0.004 per query vs a ≤$0.01 threshold; deflection reduces ticket cost |
| **Can we?** | **Usable: earned.** CSAT flat while deflection rose | **Feasible: earned.** Ran on our docs and traffic for two weeks |

**Decision record:** Pursue, scoped to expanding from 10% to 50% of traffic with the same thresholds, written before results. Owner role: support product lead. Re-check triggers: model price change, any docs restructure. Not earned: 100% rollout before the 50% step reports.

## Damage if ignored

- **Chaos initiation:** R11 would reorganize a team around a sales pitch.
- **Confusion induction:** R02 and R07 have no owner for the outcome.
- **Crapola instantiation:** R01, R06, and R09 carry confidence far beyond any evidence.

## Next

Three cheap actions this week: refresh R03 and R12 on current models; ask customer success who would act on a churn flag (R07); ask the three R10 requesters what they'd pay. **Human decisions:** pending, with the CPO.

Twelve ideas went in. One earned money, two need a refresh, and the rest cost nothing more than an afternoon to sift.
