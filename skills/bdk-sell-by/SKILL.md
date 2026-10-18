---
name: bdk-sell-by
description: Assess whether evidence is fresh enough for a specific AI decision and set re-check dates. Use for changing prices, models, policies, benchmarks, markets, or experiments; step 4 of the Baloney Funnel, in the Confusion tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[sources with dates, model versions, prices, or an earlier decision record]"
intent: >-
  Help a product person tell durable evidence from perishable evidence for this
  decision, refresh what has spoiled, and leave a re-check date on everything
  perishable so that an approved bet (Truth) gets sent back for a refresh when
  its evidence expires instead of being silently reused.
theme: baloney-detection
tier: 2-confusion
sift-question: "Is the evidence fresh enough for this decision?"
status: active
best-for:
  - "Benchmarks and pilots run on an older model version"
  - "Prices, policies, and regulations that change"
  - "Re-checking an earlier Pursue before a renewal"
  - "Setting re-check triggers on a new decision"
scenarios:
  - "A vendor benchmark predates the model now shipping"
  - "A team wants to renew a budget on last spring's decision"
  - "Pricing assumptions came from a sheet captured months ago"
produces:
  - "Freshness Ledger separating publication, observation, retrieval, effective period, and version"
  - "Re-check dates or event triggers for perishable evidence"
  - "A Sell-By rating and an exit for each claim"
depends-on: []
combine-with:
  - bdk-labels
  - bdk-relevance
  - bdk-receipts
interface:
  display_name: "Check the Sell-By Date"
  short_description: "Is this evidence fresh enough for this call?"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-sell-by to check whether this evidence is fresh enough for the decision, set re-check triggers, and stop with a Freshness Ledger and an exit for each claim."
  allow_implicit_invocation: true
---

# Check the Sell-By Date

## Purpose

Check temporal applicability rather than stamping everything older than an arbitrary number of days as rotten. Freshness depends on the claim and the decision.

This is step 4 of the Baloney Funnel, in the **Confusion** tier: *What do we actually know, is it still fresh, and does it apply to us?* It dates the labeled evidence from `bdk-labels`, and checks it against the outcome statement's timeframe: evidence that will spoil before the outcome's by-when needs a re-check before then. It is a date check, so it is cheap, and it belongs before anyone designs a test. It also closes the loop: every perishable piece of evidence behind a Pursue leaves with a re-check date, and when one expires, Truth goes back for a refresh (to Receipts and Sell-By) instead of being reused.

## When to use it

Use when claims depend on changing conditions or an old experiment is being reused, and whenever an earlier decision is about to be renewed. Durable historical records may remain suitable; current capability, price, policy, and deployment conditions need current evidence.

## Inputs

Accept a ledger, sources, dates, model/version identifiers, experiment periods, pricing assumptions, an earlier decision record with re-check dates, and the decision date. Obtain the current date from the environment rather than inventing it.

## Key concepts

**Perishable versus durable.** A historical fact about what happened in March stays true; a claim about how a model, price, or policy behaves *now* spoils. Ask what would have to stay the same for the evidence to still apply.

*Violation signal:* everything older than 90 days is marked stale, or nothing is, with no reason tied to the claim.

**The dates are different dates.** Publication, observation (when it was measured), retrieval, effective period, and version are separate. A page fetched today about an experiment run last year is last year's evidence.

*Violation signal:* the retrieval date is reported as the experiment date.

**Stale is not false.** Spoiled evidence goes back for a refresh. It does not prove the claim wrong, and it should not kill an otherwise promising bet.

*Violation signal:* a claim is sifted out solely because its evidence is old.

**Truth has a sell-by date.** A Pursue rests on evidence that will change. Re-check triggers (a model deprecation, a price notice, a policy revision) are part of the decision, not an afterthought.

*Violation signal:* a renewal cites an old decision without checking whether any of its triggers fired.

## Outputs

A Freshness Ledger (claim, dates, version, perishable/durable and why, still applies?), refresh priorities, re-check dates or triggers, a Sell-By rating, an exit for each claim, and residual temporal limits. Use [the template](template.md).

## Method

1. Establish the assessment date, the target decision period, and the outcome statement's by-when if there is one. If the runtime date is unavailable, report as-of unknown rather than assuming today.
2. For each material claim record publication date, observation/experiment period, effective/expiry date, retrieval date, and model/tool/policy version when relevant. Keep absent values missing. A recent retrieval does not make an old observation current.
3. Explain why the claim is perishable or durable. Use the decision's consequence and rate of change to propose a freshness requirement. A numeric refresh interval is an ASSUMPTION unless justified by a source or supplied policy; there is no universal expiry period.
4. If an earlier decision record is supplied, check each of its re-check dates and triggers first, and say which fired.
5. Inspect current authoritative versions when tools and scope permit. Compare what changed, not just page timestamps. Note whether a current page applies to the same region, plan, model, cohort, or workflow.
6. Recompute implications with supplied or inspected values. Preserve uncertainty if period/version alignment is unresolved. Historic results can be factual for their period and still fail to establish present performance.
7. Identify downstream statements needing revision and which four-risk squares become stale (usually Feasible for model changes, Viable for price changes).
8. Set a re-check date or event trigger for every perishable item that will remain in play.
9. Rate Check the Sell-By Date for this decision. If all material evidence is durable, say so with reasons rather than fabricating stale items.

## Human decision gate

Recommend one exit per claim, then stop:

- **Pass:** fresh enough for this decision, with re-check triggers recorded.
- **Send back:** stale or freshness unknown. Name the refresh (re-run on the current model, re-pull the price, re-read the policy). This is the usual exit for spoiled evidence.
- **Sifted out (Punt):** rare. Only when the claim *depends* on a condition that no longer exists (a discontinued product, a repealed policy) and nothing can refresh it.

When re-checking an earlier Truth, say plainly that it is going back into the funnel and which evidence expired. Do not continue into the next tier on your own.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not use fetched date as experiment date, a blog update as policy effective date, or a current leaderboard as proof of product behavior. Do not invent an expiry date or a future price. An undated source has unknown freshness; it is not automatically false. Do not renew an old decision because "it already passed."

## Assets and examples

- [Freshness Ledger template](template.md)
- [Worked example: Truth that spoiled](examples/worked-example.md)
- [Weak example: the 90-day rule](examples/weak-example.md)
- Teaching cases: [stale evidence](../../evals/cases/04-stale-evidence.md), [Safe to Serve expires](../../evals/loop-cases/loop-06-safe-to-serve-expires.yaml)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
