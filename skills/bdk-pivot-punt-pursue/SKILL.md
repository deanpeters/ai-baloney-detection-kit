---
name: bdk-pivot-punt-pursue
description: Recommend Pursue, Pivot, or Punt for an AI bet, and say why, from its outcome, its relevant, labeled, fresh receipts, and the tiny tests run on the four risks (valuable, usable, viable, feasible). Use when it's time to decide; step 7 of the Baloney Funnel, the Considered tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[the bet, its outcome statement, evidence, and test results]"
intent: >-
  Help a product person make a call they can defend. Pursue means so much
  proof that we go forward as planned. Pivot means adjust based on what the
  data and the discoveries showed. Punt means the orange is not worth the
  squeeze: say no. The four risks show why, the weakest square decides, and
  the recommendation is scoped to the investment the evidence actually earned.
theme: baloney-detection
tier: 4-considered
sift-question: "Pursue, pivot, or punt, and why?"
status: active
best-for:
  - "Ending a funnel run with a recommendation and its reasons"
  - "Deciding what size of bet the evidence has earned"
  - "Saying no clearly, with what would reopen it"
  - "A one-page decision record with owner role, by-when, and re-check triggers"
scenarios:
  - "Leadership wants a rollout and the evidence supports a pilot"
  - "Everyone agrees it works and nobody has asked who would pay"
  - "The tiny tests came back and someone has to make the call"
produces:
  - "The recommendation per scope: Pursue, Pivot, or Punt, with the why"
  - "Four-risk grid: each square earned, weak, missing, stale, or failed, with its evidence"
  - "Outcome check: was the outcome statement's target earned?"
  - "A decision record: owner role, by-when, what would change the call, re-check triggers"
depends-on: []
combine-with:
  - bdk-taste-test
  - bdk-four-risks
  - bdk-detector
interface:
  display_name: "Pivot, Punt, or Pursue"
  short_description: "Recommend pursue, pivot, or punt, and say why"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-pivot-punt-pursue to read this bet's outcome, receipts, and tiny-test results on the four risks, recommend pursue, pivot, or punt for each scope with the why, and stop with a decision record."
  allow_implicit_invocation: true
---

# Pivot, Punt, or Pursue

## Purpose

Turn everything the funnel found into a recommendation and its reasons:

- **Pursue:** so much proof that we go forward as planned.
- **Pivot:** make adjustments based on the data, the evidence, and the discoveries.
- **Punt:** the orange is not worth the squeeze. Say no.

This is step 7 of the Baloney Funnel, the **Considered** tier: *Pursue, pivot, or punt, and why?* What comes out the bottom is **Truth**: this outcome, for these people, under these conditions, has earned the next named investment. Truth has a sell-by date too, so the recommendation leaves with re-check triggers.

## When to use it

Use after the Taste Test, or on its own when a bet's evidence is already in hand and someone needs a call. It works on one claim, a feature, a vendor purchase, or one roadmap item. For a whole roadmap, run `bdk-detector`. For the four-risk grid on its own, `bdk-four-risks` goes deeper.

## Inputs

Accept the bet and the investment asked for, its outcome statement, and whatever the funnel produced: receipts, labels, freshness, relevance, tiny-test results. Notes or a sentence also work. No upstream artifact is required; missing evidence becomes a missing square.

## Key concepts

**The four risks say why.** Use the questions verbatim. **Valuable:** "Is this something someone would buy?" Not that they like it: they'd take money out of their wallets and put it into ours. **Usable:** "Will users trust and adopt it?" So usable it ensures and expands adoption, removes obstacles, and creates delight that turns users into advocates. **Viable:** "Is this good business?" (Is there ROI for both sides?) A good business model for us: SaaS is, but add generative or agentic AI and you can go broke adding users. **Feasible:** "Can we even do this with what we know and have?" The people, process, culture, and capital to make it happen.

*Violation signal:* a square is rated without naming its evidence, or Viable is judged without the cost of each additional user.

**The weakest square decides.** Never average. Three earned squares and a failed Valuable is a Punt, not "75% ready."

*Violation signal:* an overall score, a percentage, or "mostly positive."

**Pursue means proof, not hope.** Pursue is for going forward *as planned*, and only when all four squares are earned for that scope. A bet with missing squares gets Pivot to the tiny test, not Pursue and not Punt.

*Violation signal:* "Pursue, pending validation."

**Punt means no, said plainly.** When the orange isn't worth the squeeze (Valuable failed, the outcome was vanity, nothing transfers, or the proof would cost more than the outcome is worth), say no and say what would reopen it. Missing is not failed: never Punt something merely untested.

*Violation signal:* an untested idea is punted, or a contradicted one is "held for more data."

**Scope the call.** Evidence earns a specific investment. A two-week pilot can be earned while an annual contract, a public launch, or automatic actions are not. Each scope gets its own move.

*Violation signal:* one verdict covers the pilot and the rollout together.

## Outputs

Lead with the recommendation for each scope and the why in one line each. Then the four-risk grid, the outcome check (did the evidence earn the outcome's target, or a smaller one?), and the decision record. Use [the template](template.md).

## Method

1. Name the bet, its outcome statement, and every scope on the table (pilot, rollout, contract, public launch, automatic action). Each gets its own call.
2. Gather what the funnel found: the outcome, the receipts and their labels, their freshness, their relevance, and the tiny-test results. Note what each step left missing.
3. Place the evidence in the four squares. Rate each **earned**, **weak**, **missing**, **stale**, or **failed**, naming the evidence. Show Viable's two sides: their ROI, and ours including the cost per additional user at scale. For Feasible, name the people, process, culture, and capital.
4. Raise the **feasible-only flag** by name if a working demo is the only evidence.
5. Check the outcome: did the evidence earn the target and timeframe in the outcome statement, a smaller target, or none?
6. Make the call for each scope:
   - All four squares earned for this scope → **Pursue** as planned.
   - A Usable or Feasible square failed and the others hold → **Pivot** the how (trust, workflow, review burden, or the people, process, or capital we lack).
   - Viable failed while Valuable holds → **Pivot** price, scope, or cost for whichever side's ROI fails.
   - The requested scope isn't earned and a smaller one is → **Pivot** to the smaller scope, and say the larger one is not earned.
   - Squares missing, not failed → **Pivot** to the tiny test first (or send it back to the step that can fetch the evidence).
   - Valuable failed, the outcome was vanity or output only, nothing transfers to us, or the proof would cost more than the outcome returns → **Punt**.
7. Write the why for each call in one or two sentences: the deciding square, the evidence in it, and what the call protects.
8. Write the decision record: move, scope, deciding squares and evidence, suggested owner role (named owner only if supplied), by-when, what would change the call, where it goes next, and re-check triggers for perishable evidence behind any Pursue.
9. Name a sibling hand-off when one fits (an agent idea that reaches Truth goes to `adlc-step1-frame-intent`). Do not claim the hand-off was run.

## Human decision gate

Present the recommendation for each scope first, with its why, then the alternatives a reasonable person might choose and what each would cost. Then stop. The recommendation is not the decision: a person decides, and only a person's decision is recorded as one. Do not approve spend, sign, launch, or start the next step.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the outcome statement, the four risks, Pursue, Pivot, and Punt, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. In Guided Discovery, ask about the square with the least evidence first. In Spitballing, lead with the weakest square as a question rather than a grid. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Boss leans on Viable; Antagonist argues the strongest case for the square you rated best. Pirate may say the orange isn't worth the plunder. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not average the squares, let an earned Feasible stand in for the other three, Pursue a rollout on pilot evidence, or Punt something merely untested. Do not paraphrase the four questions. Do not record a human decision nobody made. Do not treat PASS-OFF as a verdict on a claim; it is a move for work (see `bdk-skill-sorter`).

## Assets and examples

- [Recommendation and decision record template](template.md)
- [Worked example: a pilot earned, a launch not](examples/worked-example.md)
- [Weak example: pursue, pending validation](examples/weak-example.md)
- Teaching cases: [nobody would buy it](../../evals/loop-cases/loop-03-nobody-would-buy-it.yaml), [earned Pursue](../../evals/loop-cases/loop-07-earned-pursue.yaml)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
