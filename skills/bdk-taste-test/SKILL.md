---
name: bdk-taste-test
description: Design the cheapest tests of whether an AI bet is valuable, usable, viable, and feasible, or review supplied results. Use before a bet advances beyond plausible output or a working demo; the Crapola tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[the bet, its open risk squares, traces, or experiment results]"
intent: >-
  Help a product person give reality a specific, affordable chance to disagree
  before the next investment. Test only the riskiest open squares, write the
  thresholds before looking at results, and keep a plan, an executed result,
  and the decision it can support separate. AI made building cheap; this is
  where buildable-but-nobody-wants-it gets caught.
theme: baloney-detection
tier: 3-crapola
sift-question: "Would reality disagree?"
status: active
best-for:
  - "Turning a working demo into the cheapest real test"
  - "Reviewing pilot results against prewritten criteria"
  - "Testing trust and adoption, not just accuracy"
scenarios:
  - "An executive's prototype works and the only evidence is the demo"
  - "A vendor eval says 94% accurate and users rewrite most drafts"
  - "A beta shows engagement and nobody has asked who would pay"
produces:
  - "Taste Test: the riskiest open squares, the cheapest test for each, thresholds written first"
  - "Or a result review against prewritten criteria"
  - "A Taste rating and an exit for the bet"
depends-on: []
combine-with:
  - bdk-four-risks
  - bdk-context-pantry
interface:
  display_name: "Taste Before You Ship"
  short_description: "Cheapest tests of the four risks, before you build"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-taste-test to pick the riskiest open squares among valuable, usable, viable, and feasible, design the cheapest test for each with thresholds written first, and stop at the test plan."
  allow_implicit_invocation: true
---

# Taste Before You Ship

## Purpose

Give reality a specific opportunity to disagree before the next investment. Separate an experiment plan, an executed result, and the decision that result can support.

This is the **Crapola** tier: *Would reality disagree?* Claims arrive here real, current, honestly labeled, and in context. What remains is whether anyone would buy it, trust it, profit from it, and whether we can actually do it. It is the most expensive tier, which is why it runs last and tests only what is still open.

## When to use it

Use before building, piloting, scaling, or claiming validation. Accept early ideas as well as traces and results. A small useful test can precede a prototype.

## Inputs

Accept the person/problem, desired change, baseline, constraints, the four-risk squares so far, riskiest assumption, traces, experiment results, and decision criteria. Missing results produce a plan, never a validation verdict.

## Key concepts

**The four risks.** Use the questions verbatim. **Valuable:** "Is this something someone would buy?" **Usable:** "Will users trust and adopt it?" **Viable:** "Is this good business?" (Is there ROI for both sides?) **Feasible:** "Can we even do this with what we know and have?" Test the riskiest open square, not all four by habit.

*Violation signal:* a plan with four tests of equal size, or a plan that never mentions Usable.

**Feasible-only.** A working demo answers "can it be built?", which AI made cheap. It does not answer whether *we* can do it with our data and constraints, and it says nothing about the other three squares.

*Violation signal:* the only evidence is a demo and the recommendation is to build.

**Thresholds before results.** A pass/fail line written after seeing the numbers is a story, not a test.

*Violation signal:* the criteria appear for the first time in the results section.

**Accurate is not trusted.** Model quality and user adoption are different squares. People who can't see why the output is right will check everything, and the time saved disappears.

*Violation signal:* "94% accurate" is offered as the answer to "will users trust and adopt it?"

## Outputs

An experiment brief or result review covering the open squares; criteria and hard stops; evidence limits; a Taste rating; and an exit for the bet. Use [the template](template.md).

## Method

1. Declare whether this is planning before results or review of supplied results. Identify the decision and the riskiest uncertainty that could overturn it.
2. Lay out the four squares with their status so far (earned, weak, missing, stale, failed). If the only evidence is a working demo, raise the **feasible-only flag** by name.
3. Pick the one to three riskiest open squares. Explain any square that cannot yet be assessed.
4. Express the hypothesis: if this change reaches these people under these conditions, then this observable outcome should improve compared with the current approach. Label unverified premises.
5. Choose the smallest revealing test for each chosen square: a conversation with a buyer (Valuable), watching one person use it (Usable), a willingness-to-pay ask or unit-cost model (Viable), a run on our own data and constraints (Feasible), a concierge trial, a historical replay, or a bounded prototype. A technical benchmark cannot settle willingness to change behavior.
6. For each test name input/cohort/context, comparator, observation method, measure and denominator, time/cost budget, proposed owner role, success/failure/inconclusive criteria, hard stops, and what decision changes. Include review and exception costs. Propose thresholds as ASSUMPTION planning choices when absent and do not claim statistical sufficiency from an arbitrary sample size.
7. Before reviewing results, preserve existing criteria and version. If no criteria were prewritten, disclose the review is exploratory; do not retrofit a pass. Keep planned, executed, and untested conditions separate.
8. For AI behavior tests include decision-relevant failure cases: contradictions, inaccessible records, untrusted instructions, unsupported certainty, and handback/rollback. No aggregate success rate cancels a critical failure.
9. If a rubric or automated judge will be used, first check whether it detects a known bad output. Model agreement is not a human verdict. This skill can propose these activities without pretending to have performed them.
10. Review supplied results against the criteria, calculate only from available rows, name confounders, and cap the conclusion to the tested period, population, and version. Synthetic results explain the method; they do not establish real-world success.
11. Rate Taste Before You Ship on completed, relevant evidence, not plan quality.

## Human decision gate

Recommend one exit for the bet, then stop:

- **Pass** to Considered (`bdk-four-risks`): results meet prewritten criteria for the open squares.
- **Held for a test:** the squares are missing, not failed. The recommendation is to run the named tests, not to build. This is not a Punt.
- **Pivot:** one square failed and a specific change could fix it (show sources to earn trust, narrow scope, change pricing). Re-enter this tier with the change. If the request was a rollout, the rollout is "not earned" and the bet is a Pivot, not a Punt.
- **Sifted out (Punt):** Valuable failed, or no affordable test could move the riskiest square.

Record the approved test, its owner role, budget, and thresholds. Do not run the test, approve a build, or continue to Considered on your own.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not declare validation from a demo, user compliments, a benchmark, generated traces, a competitor precedent, or executive enthusiasm. Do not treat monitoring as rubric validation or judge verification. Do not invent human grades, executed tests, permission, or measured outcomes. Do not blame users when they don't trust an output they cannot check; that is a Usable finding about the product.

## Assets and examples

- [Taste Test template](template.md)
- [Worked example: accurate but untrusted](examples/worked-example.md)
- [Weak example: the demo passed](examples/weak-example.md)
- Teaching cases: [demo is not validation](../../evals/cases/05-demo-not-validation.md), [bounded pilot](../../evals/cases/06-bounded-pilot.md)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
