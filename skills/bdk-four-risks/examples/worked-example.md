# Worked Example: A Pilot Earned, a Launch Not

**Synthetic.** Northbank and its FAQ assistant are invented. From [the bounded-pilot case](../../../evals/cases/06-bounded-pilot.md) and [funnel case 07](../../../evals/loop-cases/loop-07-earned-pursue.yaml).

**Tier:** 4 Considered · **As of:** 2026-10-11 · **Mode:** Context Dump

**Scopes on the table:**
1. Extend the draft-only internal pilot to 20 more tasks, with analyst approval kept
2. Sell it publicly
3. Let it send answers automatically

## The grid (scope 1: internal extension)

| | For them | For us |
|---|---|---|
| **Should we?** | **VALUABLE: earned.** 36 → 24 minutes across four matched tasks (33% saved), against a prewritten ≥20% criterion (S2, S3) | **VIABLE: earned for a pilot.** Their side: 12 analyst-minutes saved per four tasks. Our side: $0.20 total model usage (S4). Setup and support costs unknown, which is acceptable at pilot size |
| **Can we?** | **USABLE: earned.** All four final answers correctly cited after review; the one inaccessible record was handed back to manual search as designed | **FEASIBLE: earned** on the current FAQ export (effective 2026-10-01) and model Q1 |

Feasible-only flag: no. There is evidence in all four squares.

## Moves

| Scope | Move | Deciding square | Why |
|---|---|---|---|
| 1. Internal 20-task extension | **Pursue** | All four, at pilot size | Prewritten criteria met; the extension is the next test, not proof of scale |
| 2. Public sale | **Punt (for now)** | Valuable, *for an outside buyer*: missing | No buyer, price, or support context exists. Internal time saved says nothing about who would buy it |
| 3. Automatic answers | **Not earned** | Usable and Feasible without review: untested | Every result so far includes analyst review; removing it is a different product |

## Decision record

| | |
|---|---|
| Recommended move | Pursue the 20-task internal extension, draft-only, with analyst approval |
| Deciding evidence | S2 matched-task log; S3 prewritten criteria |
| Suggested owner role | Team lead (pilot owner) |
| By when | Before the next FAQ revision, so results stay comparable |
| What would change the call | Any unauthorized send (hard stop); time saved below 20%; citation errors after review |
| Where it goes next | **Truth**, scoped to the extension |
| Re-check triggers | Model Q1 deprecation notice · provider price change · any FAQ policy revision |
| **Human decision** | Pending, with the team lead |

This is what "yes" looks like: clear, scoped, and with its own sell-by date.
