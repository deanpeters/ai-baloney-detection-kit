# Worked Example: A Pilot Earned, a Launch Not

**Synthetic.** Northbank and its FAQ assistant are invented. From [funnel case 07](../../../evals/loop-cases/loop-07-earned-pursue.yaml).

**Step:** 7 Considered · **As of:** 2026-10-18 · **Mode:** Context Dump

**Outcome statement:** Reduce analyst time per policy question 20% by end of Q4 2026 for Northbank's internal support analysts in FAQ research.

## The recommendation

| Scope | Recommendation | Why |
|---|---|---|
| 1. Extend the draft-only pilot to 20 more tasks, analyst review kept | **Pursue** | All four squares earned at pilot size: 33% time saved against a prewritten 20% bar, every answer cited after review, pennies in model cost, and it runs on our own FAQ export. That's proof enough to go forward as planned. |
| 2. Sell it publicly | **Punt** | The orange isn't worth the squeeze yet. Nobody outside has been asked to buy it, and internal minutes saved say nothing about an outside wallet. Reopen with five buyer conversations that end in a price. |
| 3. Let it send answers automatically | **Pivot** | Every result so far includes an analyst's review. Removing review is a different product. Adjust: run a shadow test where it drafts and analysts score whether they'd have sent it unchanged; the bar is 95% on 100 questions. |

## The four risks (scope 1)

| | For them | For us |
|---|---|---|
| **Should we?** | **VALUABLE: earned.** Analysts chose it over manual search for every task; 36 → 24 minutes across four matched tasks | **VIABLE: earned for a pilot.** Their side: 12 analyst-minutes saved per four tasks. Ours: $0.20 total model usage; at 2,000 questions a month that's about $100 a month, well inside the team's tooling budget |
| **Can we?** | **USABLE: earned.** All final answers correctly cited; the one inaccessible record handed back to manual search as designed | **FEASIBLE: earned.** Current FAQ export (effective 2026-10-01), model Q1, one analyst lead to own review; no new hires or capital |

Feasible-only flag: no. There is evidence in all four squares.

## Outcome check

| Target | Earned | Gap |
|---|---|---|
| 20% less analyst time per question | 33% on four matched tasks | Four tasks is a small sample; the 20-task extension tests whether it holds |

## Decision record

| | |
|---|---|
| Recommendation and scope | Pursue the 20-task extension; Punt public sale for now; Pivot automatic sending to a shadow test |
| Deciding squares | All four at pilot size; Valuable (outside buyer) for sale; Usable without review for automation |
| Suggested owner role | Support analytics lead |
| By when | Results by 2026-11-15 |
| What would change the call | Time saved under 20% on the extension, or any uncited final answer |
| Where it goes next | Scope 1 → Truth (pilot only). Scope 3 → back in at the Taste Test |
| Re-check triggers | FAQ export revision, model version change, or 2026-12-31, whichever comes first |
| Hand-off | None |
| **Human decision** | _recorded by the human, not the assistant_ |
