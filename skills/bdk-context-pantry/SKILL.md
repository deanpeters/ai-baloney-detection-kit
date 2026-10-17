---
name: bdk-context-pantry
description: Find decision-critical context, contradictions, and gaps in an AI idea. Use when the customer, outcome, workflow, economics, or constraints are unclear; the second sift in the Confusion tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[an idea, brief, transcripts, research, or constraints]"
intent: >-
  Help a product person find out whether the context in hand is enough for
  this decision: for whom, compared with what, inside which workflow, at what
  cost to each side. "AI increased productivity 40%" is a claim with no
  pantry; this skill finds the missing shelves and ranks them by whether they
  could reverse the call.
theme: baloney-detection
tier: 2-confusion
sift-question: "What do we actually know, and does it apply to us?"
status: active
best-for:
  - "Fuzzy AI ideas with no named user or owner"
  - "Document-heavy proposals that still miss the decisive context"
  - "Two-sided economics: the customer's ROI and ours"
scenarios:
  - "Nobody can say who acts on the AI's output or what they do differently"
  - "A competitor's success is offered as proof it will work here"
  - "The business case shows our cost but not the customer's effort, or the reverse"
produces:
  - "Context Inventory: present, conflicting, and missing, ranked by consequence"
  - "Workflow trace: who does what differently, who owns it when wrong"
  - "Two-sided economics, with the arithmetic shown"
  - "A Context rating and an exit for each claim"
depends-on: []
combine-with:
  - bdk-labels
  - bdk-taste-test
interface:
  display_name: "Check the Context Pantry"
  short_description: "For whom, compared with what, at what cost?"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-context-pantry to find the decision-critical context gaps in this idea, trace the workflow and both sides' economics, and stop with a Context Inventory and an exit for each claim."
  allow_implicit_invocation: true
---

# Check the Context Pantry

## Purpose

Determine whether the available context is sufficient for this decision and expose the gaps that materially change the bet. More documents do not automatically mean better context. Thin context produces thick crapola.

This is the second sift in the **Confusion** tier: *What do we actually know, and does it apply to us?* A real, current, honestly labeled claim can still fail here because it is about somebody else's people, workflow, or economics.

## When to use it

Use for a fuzzy idea or a document-heavy proposal. Examine the requested investment, not a universal completeness checklist. Do not force formal framing in Spitballing.

## Inputs

Accept an idea, brief, transcripts, existing research, constraints, economics, definitions, or prior decisions. Direct notes work; no persona or canvas prerequisite.

## Key concepts

**For whom, compared with what.** A result without a person and a baseline is a number floating in space. Name who changes behavior and what they do today.

*Violation signal:* the context map names "users" and "efficiency" but no role, no current workaround, and no baseline.

**Who owns it when it's wrong.** AI output will sometimes be wrong. If no one owns the consequence, the workflow is incomplete, however good the model.

*Violation signal:* the workflow trace ends at "the AI generates…" with no review, handback, or rollback.

**ROI for both sides.** The customer's benefit and our cost to deliver it are separate ledgers. One side winning does not make it good business.

*Violation signal:* "customers save six hours a month" appears with no mention of what each of those hours costs us to serve.

**Precedent is not transfer.** Another company's success shows a mechanism worked under their conditions. Name the differences in people, data, incentives, and economics before borrowing the conclusion.

*Violation signal:* "a competitor launched it" is listed as context supporting demand.

## Outputs

A compact present/conflicting/missing context map ranked by consequence, a workflow trace, two-sided economics, alternative explanations, the four-risk squares each gap affects, a Context rating, and an exit for each claim. Use [the template](template.md).

## Method

1. State the decision and its stakes. Locate the user/customer, problem, desired outcome, current behavior and workaround, and baseline. Separate customer outcome from internal output volume.
2. Extract constraints, business model, market alternatives, operating environment, definitions, timeframe, success criteria, existing evidence, known decisions, dependencies, risks, and accountability. Use relevant fields only; record where each came from.
3. Trace the proposed change through the actual workflow: who does what differently, who handles exceptions, and who owns the consequence when wrong. Identify added coordination, cost, and ambiguity.
4. Inspect economics on both sides: customer effort/benefit and provider cost/value capture. Include review, integration, exception handling, adoption, and support where material. Show the arithmetic from supplied values; use variables or labeled ranges when values are absent. Do not hide a losing segment inside an average.
5. Challenge solution-first framing. Consider eliminating or simplifying the work, a deterministic rule, a manual service, or improving the existing workaround. If the "AI initiative" is really a ceremony to automate, say it belongs on the Sort grid (`bdk-skill-sorter`).
6. Examine precedent transfer: identify the mechanism and the differences in people, constraints, incentives, data, or economics.
7. Map each material gap to the square it leaves open (Valuable, Usable, Viable, Feasible).
8. Rank gaps by whether they could reverse the recommendation. In Guided Discovery ask the next highest-impact question; unattended, preserve private-context gaps and make planning assumptions explicit.
9. Rate Check the Context Pantry for the named investment and propose the smallest observation, clarification, or workflow inspection that reduces the decisive gap.

## Human decision gate

Recommend one exit per claim or scope, then stop:

- **Pass:** enough context for *this size of bet* (a small test needs less than a rollout).
- **Send back:** a decisive gap that someone can fill (an owner, a baseline, a cost figure). Name who and what.
- **Sifted out (Punt):** the claim does not apply to us (wrong people, wrong workflow, economics that cannot work), or a wider scope with no context at all, such as a public launch proposed on internal evidence.
- **Pivot:** the context shows a narrower scope that *does* apply; re-enter at this tier with that scope.

Record the gaps, who could fill them, and what changes if they are filled. Do not continue into the next tier on your own.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not reward document count, require every possible field before a small experiment, invent a customer or owner, or treat an executive mandate as evidence of customer need. Distinguish unresolved definitions from a product failure. Do not blame users for a workflow that was never designed for them.

## Assets and examples

- [Context Inventory template](template.md)
- [Worked example: great for them, bad for us](examples/worked-example.md)
- [Weak example: the document pile](examples/weak-example.md)
- Teaching cases: [context conflict](../../evals/cases/03-context-conflict.md), [ROI for one side](../../evals/loop-cases/loop-05-roi-for-one-side.yaml)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
