---
name: bdk-four-risks
description: Read the four-risk grid (valuable, usable, viable, feasible) and recommend Pursue, Pivot, or Punt for a named investment. Use when deciding what an AI bet has earned; the Considered tier of the Baloney Funnel.
license: CC-BY-NC-SA-4.0
argument-hint: "[the bet, its evidence, or earlier funnel artifacts]"
intent: >-
  Help a product person turn evidence into a decision they can defend: put
  every piece of evidence in one of four squares, see which square is weakest,
  and let that square choose the move. Pursue is scoped to the bet the
  evidence earned, often a pilot rather than a rollout, and what survives is
  Truth, with a sell-by date of its own.
theme: baloney-detection
tier: 4-considered
sift-question: "Pursue, pivot, or punt?"
status: active
best-for:
  - "Deciding what size of bet the evidence has earned"
  - "Seeing which risk is actually blocking a roadmap item"
  - "Separating a pilot decision from a rollout or contract decision"
  - "A one-page decision record with owner, by-when, and re-check triggers"
scenarios:
  - "Leadership wants a rollout and the evidence supports a pilot"
  - "Everyone agrees it works and nobody has asked who would pay"
  - "A bet passed every check and needs a decision record before money moves"
produces:
  - "Four-Risk Grid: Should we? / Can we? × For them / For us, each square rated with its evidence"
  - "A move per scope: Pursue, Pivot, Punt, or Send back"
  - "A decision record: owner role, by-when, what would change the call, re-check triggers"
depends-on: []
combine-with:
  - bdk-taste-test
  - bdk-detector
interface:
  display_name: "The Four Risks"
  short_description: "Valuable, usable, viable, feasible: then decide"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-four-risks to place this bet's evidence on the valuable, usable, viable, feasible grid, recommend pursue, pivot, or punt for a named investment, and stop with a decision record."
  allow_implicit_invocation: true
---

# The Four Risks

## Purpose

Turn the evidence about an AI bet into a decision a product person can defend, and scope that decision to the investment the evidence has actually earned.

This is the **Considered** tier of the Baloney Funnel: *Pursue, pivot, or punt?* What comes out the bottom is **Truth**: this bet, for these people, under these conditions, has earned the next named investment. Truth has a sell-by date too, so the decision leaves with re-check triggers.

## When to use it

Use after the other tiers, or on its own when someone needs a decision on a bet whose evidence is already in hand. It works on a single claim, a feature, a vendor purchase, or one item from a roadmap. For a whole roadmap, run `bdk-detector`, which calls this tier for each survivor.

## Inputs

Accept the bet and its proposed investment, plus whatever evidence exists: earlier funnel artifacts (Receipts Ledger, Labeled Claims, Context Inventory, Taste Test), pilot results, notes, or a sentence. No upstream artifact is required. Missing evidence becomes a missing square.

## Key concepts

**The grid.** Two questions by two audiences. **Should we?** for them is **Valuable:** "Is this something someone would buy?"; for us it is **Viable:** "Is this good business?" (Is there ROI for both sides?). **Can we?** for them is **Usable:** "Will users trust and adopt it?"; for us it is **Feasible:** "Can we even do this with what we know and have?" Use the questions verbatim; they are the same ones on the keynote's Monday grid.

*Violation signal:* a square is rated without naming the evidence in it, or the questions have been paraphrased into something softer.

**The weakest square decides.** The grid is not averaged. A bet with three earned squares and a failed Valuable is a Punt, not "75% ready."

*Violation signal:* an overall score, percentage, or "mostly positive" summary.

**Missing is not failed.** A square nobody has tested is missing; send it back or test it. A square tested and contradicted is failed; that drives Pivot or Punt.

*Violation signal:* an untested idea is punted, or a contradicted one is "held for more data."

**Scope the bet.** Evidence earns a specific investment. A two-week pilot can be earned while an annual contract, a public launch, or automatic actions are not. Give each scope its own move.

*Violation signal:* one verdict covers the pilot and the rollout together.

## Outputs

A Four-Risk Grid, a move for each scope, the deciding square, and a decision record. Use [the template](template.md).

## Method

1. Name the bet and every scope on the table (pilot, rollout, contract, public launch, automatic action). Each gets its own decision.
2. Place every piece of evidence in a square. Use earlier funnel artifacts when supplied; otherwise extract from the input. Label claims (FACT, INFERENCE, ASSUMPTION, BEST GUESS) as you go.
3. Rate each square **earned**, **weak**, **missing**, **stale**, or **failed**, naming the evidence, and give a Baloney Scale rating per square where it helps. Show Viable's two sides separately: their ROI and ours.
4. Raise the **feasible-only flag** by name if a working demo is the only evidence: "AI made building cheap. The demo proves buildable, not feasible."
5. Read the grid for each scope:
   - All four squares earned for this size of bet → **Pursue** the named investment.
   - A Can-we square (Usable, Feasible) fails and the others hold → **Pivot** the how.
   - Viable fails while Valuable holds → **Pivot** price, scope, or cost for whichever side's ROI fails.
   - Valuable fails, or no affordable test could move the riskiest square → **Punt**.
   - A square is missing or stale → **Send back** to the top of the funnel (or run `bdk-taste-test`), not Punt.
6. **Move the bet, not just the request.** When the requested scope (rollout, contract, roadmap slot) is not earned, say so, then give the bet its move: Pivot with the named fix when a Can-we or Viable square failed, Pursue the cheapest test when squares are missing. Punt only when Valuable failed or nothing affordable could move the riskiest square.
7. Name the deciding square for each move, so everyone can see where the baloney entered.
8. Write the decision record: move, scope, deciding squares and evidence, suggested owner role (named owner only if supplied), by-when, what would change the call, where it goes next, and re-check triggers for perishable evidence behind any Pursue.
9. Name a sibling hand-off when one fits (for example, an agent idea that reaches Truth goes to `adlc-step1-frame-intent`). Do not claim the hand-off was run.

## Human decision gate

Present the recommended move for each scope first, with the deciding square, then the alternatives a reasonable person might choose and what each would cost. Then stop. The move is a recommendation; a person decides, and only a person's decision is recorded as one. Do not approve spend, sign, launch, or start the next step.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. In Guided Discovery, ask about the square with the least evidence first. In Spitballing, lead with the weakest square as a question rather than a grid. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Boss leans on Viable; Antagonist argues the strongest case for the square you rated best. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not average the squares, let an earned Feasible stand in for the other three, punt something merely untested, or pursue a rollout on pilot evidence. Do not paraphrase the four questions. Do not record a human decision nobody made. Do not treat PASS-OFF as a verdict on a claim; it is a move for work (see `bdk-skill-sorter`).

## Assets and examples

- [Four-Risk Grid and decision record template](template.md)
- [Worked example: a pilot earned, a launch not](examples/worked-example.md)
- [Weak example: the average](examples/weak-example.md)
- Teaching cases: [nobody would buy it](../../evals/loop-cases/loop-03-nobody-would-buy-it.yaml), [earned Pursue](../../evals/loop-cases/loop-07-earned-pursue.yaml)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
