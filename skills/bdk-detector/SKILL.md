---
name: bdk-detector
description: Run one AI idea or a whole pile (a roadmap, vendor pitches) through the seven-step Baloney Funnel - outcome, receipts, labels, sell-by, relevance, taste test, pivot-punt-pursue - and report what was sifted out where, and what earned Pursue, Pivot, or Punt.
license: CC-BY-NC-SA-4.0
argument-hint: "[a claim, idea, roadmap, pitch, or a pile of them]"
intent: >-
  Help a product person sift AI claims by elimination: first, is there a real
  outcome at all; then the cheapest evidence questions, so most baloney leaves
  the funnel in minutes and only the survivors earn an expensive test. Show where each claim was caught, which exit it took,
  and what the few that reach Truth have earned, without averaging anything.
theme: baloney-detection
tier: funnel
sift-question: "What survives all seven steps?"
status: active
best-for:
  - "An 'AI roadmap' with too many items"
  - "A pile of vendor pitches or analyst claims"
  - "One consequential claim, run end to end"
  - "Unattended or Context Dump runs that need a full capture"
scenarios:
  - "The CPO asks which of twelve AI ideas deserve Q1 money"
  - "A VP forwards three articles and a contract deadline"
  - "A team wants to renew an AI budget on last spring's decision"
produces:
  - "Funnel report: how many entered and left each tier, and one line per claim with its tier, exit, and reason"
  - "Claim ledger and per-tier findings"
  - "Four-risk grid and decision record for each survivor"
depends-on: []
combine-with:
  - bdk-util-slice-the-pitch
  - bdk-outcomes
  - bdk-receipts
  - bdk-labels
  - bdk-sell-by
  - bdk-relevance
  - bdk-taste-test
  - bdk-pivot-punt-pursue
interface:
  display_name: "AI Baloney Detector"
  short_description: "Sift AI claims: chaos, confusion, crapola, truth"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-detector to run these AI ideas through the seven-step Baloney Funnel, outcome first and cheapest sifts next, and stop with a funnel report: what left at each step, why, and what earned pursue, pivot, or punt."
  allow_implicit_invocation: true
---

# AI Baloney Detector

## Purpose

Help an AI bet earn the right to move forward, and help a pile of AI ideas shrink to the few that deserve investment. The detector runs the whole **Baloney Funnel**: seven steps in four tiers, a process of elimination, cheapest sift first.

| Step | Tier | Question | Skill |
|---|---|---|---|
| 1 | **Chaos** | Is there a real, measurable outcome here? | `bdk-outcomes` |
| 2 | **Chaos** | What evidence supports that outcome's metric and direction? | `bdk-receipts` |
| 3 | **Confusion** | How much of it is fact, inference, assumption, or best guess? | `bdk-labels` |
| 4 | **Confusion** | Is it fresh enough for this decision? | `bdk-sell-by` |
| 5 | **Confusion** | Does it apply to us: directly, adjacent, or by analog? | `bdk-relevance` |
| 6 | **Crapola** | What's the tiniest test that returns the most brutal truth? | `bdk-taste-test` |
| 7 | **Considered** | Pursue, pivot, or punt, and why? | `bdk-pivot-punt-pursue` |

What comes out the bottom is **Truth**: scoped to the bet it earned, with a sell-by date of its own.

## When to use it

Use for a full assessment of a claim, pitch, concept, feature, workflow, agent, or product, and especially for many at once. For a one-minute pitch verdict use `bdk-value-or-theater`; for what someone does all week use `bdk-skill-sorter`. To go deep on one tier, use that tier's skill.

## Inputs

Accept a sentence, a messy context dump, a roadmap slide, a list of pitches, links, attachments, prior assessments, or experiment results. If the input is a document rather than a list of ideas, extract the pitches and claims first (as `bdk-util-slice-the-pitch` does) and show the list. Do not require the user to run the step skills first.

## Key concepts

**Outcome first.** Nothing gets checked until we know what it is supposed to change, for whom. A pitch that is only an output, or only leads to a vanity metric, leaves at step 1. Everything after checks evidence *for that outcome*.

*Violation signal:* receipts are gathered for "an AI copilot" before anyone has said what the copilot should change.

**Elimination, not evaluation.** The funnel exists to stop spending. A claim with no traceable origin should leave at Chaos before anyone designs an experiment around it.

*Violation signal:* the output proposes a test for every item on the list.

**Four exits.** Every claim leaves a step one of four ways: **Pass** (to the next step), **Sifted out** (Punt, with the reason), **Send back** (missing or stale, back to the step that can fetch or refresh it), or **Pivot** (change one thing, re-enter at the step where it failed). Missing is not failed; stale is not false.

*Violation signal:* old or untested items are killed outright, or every item is "needs more research."

**Where the baloney entered.** The useful output is the step and the square where each claim was caught, not a score.

*Violation signal:* a single rating for a whole roadmap, or an average across checks.

**Work is not a claim.** An "AI initiative" to automate a status report is a question about work. Route it to the Sort grid (`bdk-skill-sorter`) instead of running four tiers on it.

*Violation signal:* the funnel solemnly evaluates whether a weekly report nobody reads should be AI-generated.

## Outputs

Two sizes. **Lead with the stage card; give the full report when asked.**

**Stage card (default).** It must read on a projector in under a minute: 200 words or fewer, no ledger, no ratings table.

```
## Baloney Funnel: <what went in>  ·  <N> in → <n> Truth

**Outcome:** <the shaped outcome statement> (one line per idea when several)

**CHAOS** · Real outcome? Real receipts? · <N> → <n>
- #<id> <short claim>: SIFTED OUT at Outcomes · <output only / vanity>
- #<id> <short claim>: SIFTED OUT at Receipts · <reason in ≤ 8 words>

**CONFUSION** · Labeled, fresh, and about us? · <n> → <n>
- #<id> <short claim>: SEND BACK at Sell-By · <what to refresh>

**CRAPOLA** · Would reality disagree? · <n> → <n>
- #<id> <short claim>: PIVOT · <the named change>

**CONSIDERED** · Pursue, pivot, or punt?
- #<id> <short claim>: **PURSUE** · <why, in ≤ 12 words>

Say "full report" for the ledger, ratings, and decision records.
```

Routed work items get one line above CHAOS ("Not a claim: routed to the work family"). Name the step a claim left at (Outcomes, Receipts, Labels, Sell-By, Relevance, Taste). **Counting:** list each claim exactly once, in the tier it left. Every exit leaves the tier (Sifted out, Send back, Pivot, and Held for a test all count as out; a Pivot re-enters later, not now). `In → Out` counts only what passes down. Claims that reach Considered are listed only there. The counts must add up to the number that went in.

**Full report** (when the user asks for it, asks for a capture or file, or the run is an unattended assessment that asks for the complete output): the **funnel report** (counts per tier, one line per claim: step, exit, reason), the outcome statement for each idea (before and after), a claim ledger with the label mix, per-step findings, a four-risk grid, recommendation with its why, and decision record for each claim that reaches Considered, and the next smallest evidence action. Use [the template](template.md).

## Method

1. Read the bundled assessment contract. Identify the decision and investment for each claim, reuse supplied context, select mode and voice, and state evidence access limits and the as-of date.
2. **Intake.** List the claims, one atomic claim per line, with IDs. Route any item that is really work (a ceremony, a report, a ritual) to the work family: say "routed to the work family" (not "pass off"), ask the Theater question first ("Who's this for, the customer or the audience?") so a chore nobody needs is punted, and name the `workflow-to-skill-converter` hand-off for a chore that survives. For one claim, the funnel has one row.
3. **Step 1, Outcomes (Chaos).** Shape each idea into an outcome statement: [direction] [metric] [by how much] [by when] for [beneficiary persona] in [problem context]. Reshape before rejecting, and label every inserted part (a proposed target or timeframe is an ASSUMPTION). Exits: output only, a slogan, or only vanity metrics → Sifted out; a real outcome with no basis for the beneficiary or metric that someone can supply → Send back; otherwise Pass with the statement.
4. **Step 2, Receipts (Chaos).** For each outcome: find the evidence about its metric and direction (a baseline, support that the change moves the metric, support for the target's size). Trace origins and collapse shared ones. Exits: an interested party's outcome number with no method offered as the evidence → Sifted out; the receipt exists but is not in hand → Send back with what to fetch; otherwise Pass. A sponsor's untested belief ("they'll love it") is not a failed receipt: label it ASSUMPTION and carry it forward as a missing square.
5. **Step 3, Labels (Confusion).** Label the load-bearing evidence FACT, INFERENCE, ASSUMPTION, or BEST GUESS, and give the label mix. Exits: the decision rests entirely on assumptions presented as facts that nobody can support → Sifted out; a load-bearing claim that could be supported → Send back; otherwise Pass.
6. **Step 4, Sell-By (Confusion).** Date the evidence: publication, observation, model or price version, and against the outcome's by-when. Exits: stale or freshness unknown → Send back with the refresh named (stale is not false); depends on a condition that no longer exists → Sifted out; otherwise Pass with re-check triggers.
7. **Step 5, Relevance (Confusion).** Rate each piece of evidence direct, adjacent, analog, or not relevant to our beneficiary and context, name the mechanism for adjacent and analog evidence, and pull what our own pantry (usage, support, sales, cost to serve) says. Exits: about somebody else's people or economics with no transferable mechanism, or contradicted by our pantry → Sifted out; the deciding pantry record isn't in hand → Send back; applies to a narrower scope → Pivot; otherwise Pass.
8. **Step 6, Taste Test (Crapola).** For survivors: lay out the four squares, raise the feasible-only flag when a demo is the only evidence, and either review supplied results against prewritten criteria or design the tiniest test that returns the most brutal truth on the riskiest open square, with thresholds from the outcome's target. Exits: Valuable failed → Sifted out; a Usable, Feasible, or Viable square failed with a specific fix → **Pivot** (name the change and its threshold; never Punt this); squares missing → Held for a test (not a Punt); criteria met → Pass.
9. **Step 7, Pivot, Punt, or Pursue (Considered).** For survivors and held bets: recommend a move per scope (pilot, rollout, contract, public launch, automatic action), with the why. **Pursue:** so much proof that we go forward as planned (all four squares earned for that scope). **Pivot:** adjust based on the data and discoveries (a fixable failed square, a smaller scope than requested, or the tiny test first when squares are missing). **Punt:** the orange is not worth the squeeze; say no and what would reopen it. **Move the bet, not just the request:** when the requested scope is not earned, say so, then give the bet its move. Write a decision record with re-check triggers.
10. Rate the five checks where assessed, using the shared anchors, and name the weakest consequential finding. Never average ratings or squares.
11. Map the findings to the damage they would do if ignored: **Chaos initiation** (added workflow, coordination, cost, or risk), **Confusion induction** (unclear meanings, evidence, metrics, or ownership), **Crapola instantiation** (confidence exceeding support). State when a dimension has no material finding.
12. Write the **stage card** (default) or, when asked, the full **funnel report**: entered, routed to work, left at each tier (by exit type), held for a test, reached Truth. The counts must add up. Do the full analysis either way; the stage card only shortens what is shown.
13. Name sibling hand-offs where they fit, the next smallest evidence action, proposed owner roles, and remaining uncertainty. In formal modes use the capture shape in the bundled contract; in Spitballing keep it conversational unless asked to formalize. Save only when authorized and never silently overwrite.

If the step skills are available, consult them for depth (and `bdk-context-pantry` or `bdk-four-risks` for deeper workflow, economics, or grid work). If unavailable, complete each step using the method above; do not stop or silently skip a step.

## Human decision gate

Present the funnel report and each survivor's recommended move first, then stop. Ask the human which claims to act on and who owns each. Every exit and move is a recommendation; do not record decisions, approvals, or owners nobody supplied, and do not start tests or purchases.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. In Guided Discovery, settle the outcome statement with the user before checking any evidence; with many ideas, walk one tier at a time and confirm the survivors before the next. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable. The baloney is in the claims, not the people who brought them.

## Failure modes

Do not hide a critical failure behind an average score, score a plan as executed validation, count model consensus as independent proof, or turn a sparse concept into a fabricated business case. Do not gather evidence for a pitch that has no outcome, or run expensive steps on claims that fail cheap ones. Do not kill stale or untested claims as if they were false. Do not presume the kit's output grants launch permission. Revise the recommendation when stronger evidence arrives.

## Assets and examples

- [Funnel report template](template.md)
- [Worked example: twelve roadmap ideas, one Truth](examples/worked-example.md)
- [Weak example: twelve experiments](examples/weak-example.md)
- Teaching cases: [all funnel cases](../../evals/loop-cases/README.md), [bounded pilot](../../evals/cases/06-bounded-pilot.md)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
