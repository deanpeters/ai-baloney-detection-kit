---
name: bdk-outcomes
description: Shape an AI pitch, claim, or idea into a measurable outcome statement (direction, metric, target, timeframe, beneficiary, context), or sift it out as output-only or vanity. Use first, before checking any evidence; step 1 of the Baloney Funnel, in the Chaos tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[a pitch, claim, idea, roadmap item, or feature request]"
intent: >-
  Help a product person find the outcome hiding inside a pitch before anyone
  spends time on its evidence. "An AI interface that makes accountants feel 50%
  more confident" is an output wearing a feeling; "increase month-end-close
  adoption 50% for corporate accountants" is something the rest of the funnel
  can check. If a pitch cannot be shaped into a real outcome, or only leads to
  vanity metrics, it leaves here, in minutes.
theme: baloney-detection
tier: 1-chaos
sift-question: "Is there a real, measurable outcome here?"
status: active
best-for:
  - "Feature requests and AI pitches that describe what we'd ship, not what would change"
  - "Roadmap items with a success metric nobody could observe"
  - "Executive asks that need an outcome before they need a plan"
scenarios:
  - "A VP wants 'an AI copilot for the finance team' by Q2"
  - "A pitch promises users will 'feel more confident' or 'love it'"
  - "A roadmap lists outputs (agents, chatbots, interfaces) with no metric"
produces:
  - "Outcome statement: [direction] [metric] [by how much] [by when] for [beneficiary] in [context], before and after shaping"
  - "Outcome check: each part present, inserted (labeled), or missing"
  - "An exit for each pitch: Pass, Send back, or Sifted out"
depends-on: []
combine-with:
  - bdk-util-slice-the-pitch
  - bdk-receipts
  - bdk-detector
interface:
  display_name: "Name the Outcome"
  short_description: "Outcome or output? Shape it, or sift it out"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-outcomes to shape this pitch into a measurable outcome statement (direction, metric, target, timeframe, beneficiary, context), or sift it out as output-only or vanity, and stop with the statement and an exit."
  allow_implicit_invocation: true
---

# Name the Outcome

## Purpose

Find the outcome inside a pitch, claim, or idea, and write it so that the rest of the funnel can check it:

**[direction] [metric] [by how much] [by when] for [beneficiary persona] in [problem context]**, optionally **without [a health metric] crossing [a limit]**

This is step 1 of the Baloney Funnel, in the **Chaos** tier: *Is there a real, measurable outcome here?* It is the cheapest sift of all. A pitch that is only an output ("an AI interface"), or that only leads to a vanity metric ("feel more confident"), leaves here, before anyone looks for receipts.

## When to use it

Use first, on anything that proposes an investment: a pitch, a feature request, a vendor promise, a roadmap item, a hot take turned into a project. If the input is a deck or a document rather than one pitch, slice it first (`bdk-util-slice-the-pitch`) and shape each item. Use `bdk-detector` to run all seven steps.

## Inputs

Accept a sentence, a pitch, a roadmap line, a brief, or a stated success metric. Any supplied context about users, segments, baselines, or timelines is used before asking. No other step is required first.

## Key concepts

**Outcome, not output.** An outcome is a change in someone's world or in the business (adoption, retention, time, cost, revenue, errors, NPS). An output is something we ship (an interface, an agent, a copilot, a model). "AI" in the statement is almost always output.

*Violation signal:* the shaped statement still has "AI interface," "chatbot," or "agent" where the metric should be.

**Observable, not vanity.** A metric earns its place if someone could count or observe it, quantitatively (a %, a ratio, a number, time, money) or qualitatively (a coded interview theme, an observed task completion, NPS), and if it could not rise while nothing that matters changes. Page views, prompts sent, sign-ups without activation, model accuracy alone, and a feeling with no observation method are vanity.

*Violation signal:* "feel 50% more confident" passes because it has a percentage in it.

**Rework before rejecting.** Most pitches hide a real outcome. Ask, or reshape from the supplied material, show the before and after, and label every part you inserted. Only a pitch that cannot be shaped at all, or that leads only to vanity, is sifted out.

*Violation signal:* a pitch is sifted out for wording when the supplied material clearly names who benefits and what would change.

**Inserted parts stay labeled.** A target or timeframe you proposed is an ASSUMPTION, not the sponsor's commitment. Mark it, so Receipts and Taste know what still needs a basis.

*Violation signal:* the shaped statement reads "increase adoption 50% by Q3" and nobody can tell which half the sponsor said.

**Success needs a guardrail when it can be bought by breaking something.** A success metric says what should improve; a guardrail (a health metric) says what must not get worse: AI cost to serve, trust, error rates, support load. Add one when the outcome could be hit by spending or breaking your way there. It becomes a hard stop in the Taste Test.

*Violation signal:* "increase AI-assisted replies 40%" with nothing about accuracy, review time, or cost per reply.

## Outputs

For each pitch: the original wording, the shaped outcome statement, a parts check (direction, metric and how it is observed, target and how it was built, timeframe, beneficiary, context, and an optional guardrail: each **stated**, **inserted** with its label, or **missing**), any secondary outcomes set aside, the risk square the outcome speaks to most, and an exit. Use [the template](template.md).

## Method

1. Quote the pitch as supplied. Name the decision or investment it asks for.
2. Strip the output. Set aside the thing to be built ("AI interface," "agent," "copilot") and ask what would be different for someone if it worked.
3. Find the beneficiary persona: a role or segment whose world changes, not "users." Use supplied context; if none, ask (Guided) or propose one as a labeled ASSUMPTION (Context Dump or unattended).
4. Find the metric and the direction. Prefer a metric the business already watches (adoption, retention, cycle time, error rate, revenue, NPS). Name how it would be observed. Test it against the vanity list: could it rise while nothing that matters changes?
5. Find or propose the target and timeframe. If supplied, keep them verbatim. If absent, propose them as labeled ASSUMPTIONs; they become the Taste Test thresholds and the Sell-By horizon later. Build a proposed target bottom-up from a baseline or countable parts where you can, or give a range with its reason; a target borrowed from a vendor or a top-down market share stays an ASSUMPTION. Look up public facts (industry baselines, market counts) yourself when tools allow and the input isn't a closed fixture; ask the user only for private ones.
6. Name the problem context: the workflow, situation, or market where the change happens.
7. Propose a guardrail when the outcome could be hit by breaking something else (cost to serve, trust, error rate, support load). Optional; label it as proposed.
8. Write the statement in the standard order. Show before and after. If the pitch implies several outcomes, pick the one the decision leans on and list the others.
9. Note which risk square the outcome speaks to most (an adoption metric speaks to Usable, a revenue metric to Valuable or Viable).
10. Recommend an exit. If the outcome depends on market size (a share of a market, a number of buyers), name `dlab-step02-segment` for a TAM/SAM/SOM; don't build one here.

## Human decision gate

Recommend one exit per pitch, then stop:

- **Pass:** a real outcome with direction, metric, beneficiary, and context, stated or reshaped with labels. It goes to `bdk-receipts` carrying the statement.
- **Send back:** the material points to a real outcome (an observable metric or a named beneficiary and workflow), and one fact is missing that someone can supply, such as which segment, or the baseline. Name the question and who could answer it.
- **Sifted out (Punt):** the pitch cannot be shaped into an outcome (output only, a slogan), or its only stated metric is vanity and nothing in the material points to an observable one. If shaping it would mean inventing the metric, the beneficiary, and the context yourself, that is your outcome, not the sponsor's: sift it out. Say why, and name the outcome that would reopen it (a named role, a named workflow, and a metric someone can count); the sponsor can bring it back to step 1.

Record the before and after, the inserted parts, and the questions still open. The sponsor confirms the outcome statement; do not record their agreement for them. Do not continue into Receipts on your own.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the outcome statement, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. In Guided Discovery, ask about the beneficiary first, then the metric, then the target, one at a time. In Context Dump, reshape from the material and label every inserted part. In Spitballing, offer two or three candidate outcomes and ask which one the sponsor would bet on. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Boss asks what the outcome is worth; Antagonist argues the metric could rise while nothing improves. Voice changes presentation; evidence standards and conclusions remain stable.

## Failure modes

Do not pass a feeling, an output, or a vanity number because it has a percentage attached. Do not sift out a pitch for clumsy wording when the outcome is recoverable. Do not invent a target and present it as the sponsor's. Do not check evidence here; that is the next step. Do not mock the sponsor: the pitch is the problem, not the person.

## Assets and examples

- [Outcome statement template](template.md)
- [Worked example: the accountant copilot](examples/worked-example.md)
- [Weak example: 50% more confident](examples/weak-example.md)
- Teaching cases: [vanity outcome](../../evals/loop-cases/loop-12-vanity-outcome.yaml), [output to outcome](../../evals/loop-cases/loop-13-output-to-outcome.yaml)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
