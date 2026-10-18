---
name: bdk-relevance
description: Judge whether the evidence behind an AI outcome applies to us, directly, through an adjacent product or segment, or by analog, using our pantry of product, user, business, and market data. Use after evidence is labeled and dated; step 5 of the Baloney Funnel, in the Confusion tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[the outcome, its labeled evidence, and what our pantry holds]"
intent: >-
  Help a product person find out whether real, fresh, honestly labeled
  evidence is about our people, our product, and our economics, or about
  somebody else's. A competitor's win, an analyst's market, or another
  segment's pilot can still be relevant, but only through a named mechanism
  that survives the differences. Our own pantry often already holds the
  answer, or the contradiction.
theme: baloney-detection
tier: 2-confusion
sift-question: "Does the evidence apply to us: directly, by an adjacent product, or by analog?"
status: active
best-for:
  - "Evidence from a competitor, analyst, or vendor's other customers"
  - "A result from one of our segments offered as proof for another"
  - "Checking what our own usage, sales, support, and cost data already say"
  - "Borrowing a mechanism from another industry (precedent thinking)"
scenarios:
  - "A competitor launched it, so the board assumes our customers want it"
  - "An enterprise pilot is offered as proof for the SMB tier"
  - "A logistics company's routing win is offered as the model for our scheduling feature"
produces:
  - "Relevance Map: each piece of evidence rated direct, adjacent, analog, or not relevant, with the mechanism and the differences"
  - "Pantry pull: what our own data already says about the outcome and the four squares, including cost to serve"
  - "A Relevance rating (Check the Context Pantry) and an exit for each claim"
depends-on: []
combine-with:
  - bdk-sell-by
  - bdk-context-pantry
  - bdk-taste-test
interface:
  display_name: "Check the Context Pantry: Relevance"
  short_description: "Does this evidence apply to us, and how?"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-relevance to rate each piece of evidence behind this outcome as direct, adjacent, analog, or not relevant to us, pull what our own pantry says, and stop with a Relevance Map and an exit for each claim."
  allow_implicit_invocation: true
---

# Check the Context Pantry: Relevance

## Purpose

Find out whether the evidence behind an outcome is about us. Real, fresh, honestly labeled evidence can still be about somebody else's people, product, or economics.

This is step 5 of the Baloney Funnel, the last sift in the **Confusion** tier: *What do we actually know, is it still fresh, and does it apply to us?* It checks the evidence against our **pantry**: our product materials, user data, usage and support records, sales and cost data, and the market data we keep.

## When to use it

Use after Receipts, Labels, and Sell-By, or on its own when someone offers outside evidence as proof for our bet. For a deep dive on workflow, ownership, and two-sided economics, consult `bdk-context-pantry`. Use `bdk-detector` to run all seven steps.

## Inputs

Accept the outcome statement, the evidence with its labels and dates (or raw evidence), and whatever our pantry holds: product docs, analytics, customer interviews, support tickets, win/loss notes, pricing, cost to serve, segment definitions. No upstream artifact is required; missing pantry data is a finding.

## Key concepts

**Four kinds of relevance.** **Direct:** about our product, our users, our data. **Adjacent:** about a sibling product, segment, or market of ours (same buyers, different product; same product, different tier). **Analog:** another company or industry where the same mechanism solved the same kind of problem (precedent thinking). **Not relevant:** about somebody else, with no shared mechanism.

*Violation signal:* every piece of evidence is called "relevant" with no kind named.

**Mechanism, not resemblance.** Adjacent and analog evidence transfers only through a named mechanism (why it worked there), and only if the differences in people, data, incentives, workflow, and economics don't break that mechanism.

*Violation signal:* "a competitor launched it" or "it worked in fintech" is offered as support, with no mechanism and no differences listed.

**Check the pantry first.** Our own usage, support, sales, and cost data are usually the most relevant evidence there is, and they are often unopened. A pantry record that contradicts outside evidence outranks it.

*Violation signal:* the map rates three analyst reports and never asks what our own telemetry or tickets say.

**Relevant to this outcome and this size of bet.** Evidence can be relevant to a pilot and irrelevant to a rollout, or relevant to one segment and not another. Name the scope.

*Violation signal:* an enterprise segment's result is applied to every tier without comment.

## Outputs

A Relevance Map (evidence ID, kind of relevance, mechanism, differences that matter, which square it bears on, scope it supports), a pantry pull (what our own data says, what is missing, who owns it), the cost to serve where the pantry has it, a Context Pantry rating, and an exit per claim. Use [the template](template.md).

## Method

1. Restate the outcome statement and the scope of the bet. Relevance is judged against these.
2. List the evidence that survived Receipts, Labels, and Sell-By, with its labels and dates.
3. Rate each piece **direct**, **adjacent**, **analog**, or **not relevant**. For adjacent and analog, name the mechanism in one sentence, then the differences in people, data, incentives, workflow, and economics.
4. Decide whether each mechanism survives its differences for our beneficiary and context. If it does, say for what scope. If it doesn't, say which difference breaks it.
5. Pull from the pantry: what our own usage, support, sales, interview, and cost records say about the outcome's metric and about each of the four squares. Name the record and its owner. Show the cost to serve where it matters (AI usage costs grow with users), built bottom-up (uses per user × cost per use × users), with a range and its reason where usage is uncertain. If the records exist but aren't in hand, that is a Send back, not a guess. Public market facts (segment sizes, peer adoption, published prices) are yours to look up when tools allow; private pantry records are the user's to supply.
6. Name contradictions between outside evidence and the pantry. The pantry wins unless the outside evidence is about a condition the pantry can't see.
7. Map each relevant piece to the square it informs, and mark squares left with only analog or not-relevant evidence as **weak** or **missing**.
8. Rate Check the Context Pantry for this outcome and scope, and name the single pantry record that would most change the call. If relevance hinges on market size (how many buyers like ours exist), name `dlab-step02-segment` for a TAM/SAM/SOM rather than borrowing a top-down market figure.

## Human decision gate

Recommend one exit per claim, then stop:

- **Pass:** direct evidence, or adjacent or analog evidence whose mechanism survives the differences, enough for this size of bet.
- **Send back:** our pantry probably holds the deciding record (usage, cost, interviews) and it isn't in hand. Name the record and its owner.
- **Pivot:** the evidence applies to a narrower segment, scope, or context than proposed. Re-enter with that scope.
- **Sifted out (Punt):** the evidence is about somebody else's people or economics and no mechanism transfers, or our own pantry contradicts it.

Record the relevance kinds, mechanisms, pantry gaps, and who could fill them. Do not continue into the Taste Test on your own.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the outcome statement, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. In Guided Discovery, ask first what our own data says about the outcome's metric. In Spitballing, lead with the strongest difference that could break the borrowed mechanism. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Antagonist argues the analog is a coincidence; Boss asks what it costs us per user. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not treat a competitor's launch as demand, an analog as proof, or an outside report as stronger than our own records. Do not invent pantry data that wasn't supplied. Do not sift out analog evidence just for being from another industry; name the mechanism and test it. Do not blame users for a workflow nobody designed for them.

## Assets and examples

- [Relevance Map template](template.md)
- [Worked example: the competitor's chatbot](examples/worked-example.md)
- [Weak example: everyone else is doing it](examples/weak-example.md)
- Teaching cases: [ROI for one side](../../evals/loop-cases/loop-05-roi-for-one-side.yaml), [context conflict](../../evals/cases/03-context-conflict.md)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
