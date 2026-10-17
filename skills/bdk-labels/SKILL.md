---
name: bdk-labels
description: Separate fact, inference, assumption, and best guess in AI claims or product documents. Use when polished wording or repeated claims hide uncertainty; the first sift in the Confusion tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[a document, generated analysis, notes, or claim IDs]"
intent: >-
  Help a product person see which parts of a claim are recorded, which are
  reasoned, and which are merely being treated as true, so that a decision
  rests on what is actually known. Repetition and fluent prose launder
  assumptions into facts; labeling reverses the laundering.
theme: baloney-detection
tier: 2-confusion
sift-question: "What do we actually know, and does it apply to us?"
status: active
best-for:
  - "Generated strategy or market analysis"
  - "PRDs and business cases full of confident numbers"
  - "Mixed evidence ledgers from several people"
scenarios:
  - "A deck says 'customers will love it' and nobody asked a customer"
  - "A forecast is built on real inputs and reported as fact"
  - "The same inference has been copied into five documents"
produces:
  - "Labeled Claims: one primary label per atomic claim, with its basis"
  - "Corrected wording for the claims that most inflate confidence"
  - "A Labels rating and an exit for each claim"
depends-on: []
combine-with:
  - bdk-context-pantry
  - bdk-receipts
interface:
  display_name: "Label the Lunch Meat"
  short_description: "Separate fact, inference, assumption, guess"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-labels to label each claim as fact, inference, assumption, or best guess with its basis, and stop with Labeled Claims and an exit for each."
  allow_implicit_invocation: true
---

# Label the Lunch Meat

## Purpose

Make the difference between what is recorded, what is reasoned, and what is merely being treated as true visible enough to change a decision.

This is the first sift in the **Confusion** tier: *What do we actually know, and does it apply to us?* Claims that survived the Chaos tier are real and current; this tier asks what they actually establish.

## When to use it

Use on generated analysis, strategy, market research, product claims, or a mixed evidence ledger. This is classification with reasons, not independent source verification unless access and scope allow it. Pair it with `bdk-context-pantry` to finish the Confusion tier.

## Inputs

Accept text, notes, attachments, or claim IDs from another check. Preserve supplied qualifiers and source locations.

## Key concepts

**What the document says versus what is true.** A supplied slide is FACT evidence that the slide asserts savings. The savings remain unsupported until results exist.

*Violation signal:* "the deck states X" quietly becomes "X."

**One atomic claim, one label.** Sentences bundle observations, causes, and predictions. Split them before labeling, or the strongest label gets borrowed by the weakest part.

*Violation signal:* a row labeled FACT contains the word "will."

**Unsupported stays unsupported.** An assertion supplied without support is not a BEST GUESS and not an INFERENCE. Mark the missing support; do not manufacture a basis to make it respectable.

*Violation signal:* a claim with no evidence in the input is labeled INFERENCE with a reasoning chain the assistant made up.

**Labels travel.** A copied inference keeps its label in every document it lands in, and repetition never upgrades it.

*Violation signal:* a claim labeled ASSUMPTION in the brief reappears as FACT in the summary.

## Outputs

A claim ledger with one primary evidence label per atomic claim, a basis for each label, missing support, corrected wording, the four-risk square each claim bears on, a Labels rating, and an exit for each claim. Use [the template](template.md).

## Method

1. Extract claims that could change the decision. Split sentences combining observed results, causal explanations, and predictions.
2. Locate support already present. Distinguish what the artifact records from whether the underlying statement is true.
3. Apply FACT only to directly supported propositions within the evidence's scope. Apply INFERENCE when supporting facts and a reasoning chain exist. Apply ASSUMPTION to an explicitly adopted premise. Apply BEST GUESS to a judgment under incomplete evidence. An unsupported assertion supplied as fact remains an unsupported assertion.
4. State the basis and uncertainty. For unsupported supplied claims, propose qualified wording or mark missing support; do not manufacture a basis. Missing evidence remains a status.
5. Track reuse. A copied inference retains its label. Repeated generated statements do not become independent evidence. If an assumption changes, identify dependent conclusions that need revisiting.
6. Tag each claim with the four-risk square it bears on (Valuable, Usable, Viable, Feasible). A square held up only by ASSUMPTION or BEST GUESS is **weak** or **missing**, not earned.
7. Rate Label the Lunch Meat on the artifact's labeling discipline, not on whether every claim has become FACT. A transparent early hypothesis can have good Labels and weak Taste.
8. Return the few corrections that most reduce false confidence, with evidence needed to strengthen the claims.

## Human decision gate

Recommend one exit per decision-bearing claim, then stop:

- **Pass:** honestly labeled, and the labels can bear the decision being asked of them.
- **Send back:** a load-bearing claim is unsupported but could be supported (name the evidence to get).
- **Sifted out (Punt):** the decision rests entirely on assumptions presented as facts and nobody can name evidence that would support them.

Record the relabeled claims and the dependent conclusions that change. Do not continue into the next tier on your own.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not relabel every forecast as fact because its inputs are real. Do not mistake confidence adjectives for evidence. Do not turn an unsupported assertion into an INFERENCE without supporting facts. Labeling is not validation.

## Assets and examples

- [Labeled Claims template](template.md)
- [Worked example: the churn whisperer](examples/worked-example.md)
- [Weak example: everything is a fact](examples/weak-example.md)
- Teaching case: [mixed claims](../../evals/cases/02-mixed-claims.md)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
