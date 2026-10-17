---
name: bdk-detector
description: Run one AI claim or a whole pile (a roadmap, vendor pitches) through the Baloney Funnel - Chaos, Confusion, Crapola, Considered - and report what was sifted out where, and what earned Pursue, Pivot, or Punt.
license: CC-BY-NC-SA-4.0
argument-hint: "[a claim, idea, roadmap, pitch, or a pile of them]"
intent: >-
  Help a product person sift AI claims by elimination: the cheapest questions
  first, so most baloney leaves the funnel in minutes and only the survivors
  earn an expensive test. Show where each claim was caught, which exit it took,
  and what the few that reach Truth have earned, without averaging anything.
theme: baloney-detection
tier: funnel
sift-question: "What survives all four tiers?"
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
  - bdk-receipts
  - bdk-sell-by
  - bdk-labels
  - bdk-context-pantry
  - bdk-taste-test
  - bdk-four-risks
interface:
  display_name: "AI Baloney Detector"
  short_description: "Sift AI claims: chaos, confusion, crapola, truth"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-detector to run these AI claims through the Baloney Funnel, cheapest sifts first, and stop with a funnel report: what left at each tier, why, and what earned pursue, pivot, or punt."
  allow_implicit_invocation: true
---

# AI Baloney Detector

## Purpose

Help an AI bet earn the right to move forward, and help a pile of AI claims shrink to the few that deserve investment. The detector runs the whole **Baloney Funnel**: a process of elimination by tiers, cheapest sift first.

| Tier | Question | Checks |
|---|---|---|
| **1. Chaos** | Is it real, and is it still true? | Show Me the Receipts, Check the Sell-By Date |
| **2. Confusion** | What do we actually know, and does it apply to us? | Label the Lunch Meat, Check the Context Pantry |
| **3. Crapola** | Would reality disagree? | Taste Before You Ship |
| **4. Considered** | Pursue, pivot, or punt? | The four risks |

What comes out the bottom is **Truth**: scoped to the bet it earned, with a sell-by date of its own.

## When to use it

Use for a full assessment of a claim, pitch, concept, feature, workflow, agent, or product, and especially for many at once. For a one-minute pitch verdict use `bdk-value-or-theater`; for what someone does all week use `bdk-skill-sorter`. To go deep on one tier, use that tier's skill.

## Inputs

Accept a sentence, a messy context dump, a roadmap slide, a list of pitches, links, attachments, prior assessments, or experiment results. If the input is a document rather than a list of claims, extract the claims first (as `bdk-util-slice-the-pitch` does) and show the list. Do not require the user to run the tier skills first.

## Key concepts

**Elimination, not evaluation.** The funnel exists to stop spending. A claim with no traceable origin should leave at Chaos before anyone designs an experiment around it.

*Violation signal:* the output proposes a test for every item on the list.

**Four exits.** Every claim leaves a tier one of four ways: **Pass** (down to the next tier), **Sifted out** (Punt, with the reason), **Send back** (missing or stale, so back to the top to get receipts or refresh), or **Pivot** (change one thing, re-enter at the tier where it failed). Missing is not failed; stale is not false.

*Violation signal:* old or untested items are killed outright, or every item is "needs more research."

**Where the baloney entered.** The useful output is the tier and the square where each claim was caught, not a score.

*Violation signal:* a single rating for a whole roadmap, or an average across checks.

**Work is not a claim.** An "AI initiative" to automate a status report is a question about work. Route it to the Sort grid (`bdk-skill-sorter`) instead of running four tiers on it.

*Violation signal:* the funnel solemnly evaluates whether a weekly report nobody reads should be AI-generated.

## Outputs

Two sizes. **Lead with the stage card; give the full report when asked.**

**Stage card (default).** It must read on a projector in under a minute: 200 words or fewer, no ledger, no ratings table.

```
## Baloney Funnel: <what went in>  ·  <N> in → <n> Truth

**CHAOS** · Is it real? Is it still true? · <N> → <n>
- #<id> <short claim>: SIFTED OUT · <reason in ≤ 8 words>
- #<id> <short claim>: SEND BACK · <what to fetch>

**CONFUSION** · Does it apply to us? · <n> → <n>
- …

**CRAPOLA** · Would reality disagree? · <n> → <n>
- #<id> <short claim>: PIVOT · <the named change>

**CONSIDERED** · Pursue, pivot, or punt?
- #<id> <short claim>: **PURSUE** · <scoped bet, and what isn't earned>

Say "full report" for the ledger, ratings, and decision records.
```

Routed work items get one line above CHAOS ("Not a claim: routed to the work family"). **Counting:** list each claim exactly once, in the tier it left. Every exit leaves the tier (Sifted out, Send back, Pivot, and Held for a test all count as out; a Pivot re-enters later, not now). `In → Out` counts only what passes down. Claims that reach Considered are listed only there. The counts must add up to the number that went in.

**Full report** (when the user asks for it, asks for a capture or file, or the run is an unattended assessment that asks for the complete output): the **funnel report** (counts per tier, one line per claim: tier, exit, reason), a claim ledger, per-tier findings, a four-risk grid and decision record for each claim that reaches Considered, and the next smallest evidence action. Use [the template](template.md).

## Method

1. Read the bundled assessment contract. Identify the decision and investment for each claim, reuse supplied context, select mode and voice, and state evidence access limits and the as-of date.
2. **Intake.** List the claims, one atomic claim per line, with IDs. Route any item that is really work (a ceremony, a report, a ritual) to the work family: say "routed to the work family" (not "pass off"), ask the Theater question first ("Who's this for, the customer or the audience?") so a chore nobody needs is punted, and name the `workflow-to-skill-converter` hand-off for a chore that survives. For one claim, the funnel has one row.
3. **Chaos: Is it real, and is it still true?** For each claim: trace the origin and collapse shared origins (Receipts); check dates, versions, and any earlier re-check triggers (Sell-By). Exits: no claim to check (a slogan), or an interested party's outcome number offered as evidence with no method → Sifted out; stale or unopened → Send back with the refresh named; otherwise Pass. A sponsor's untested belief ("they'll love it") is not a failed receipt: label it ASSUMPTION and carry it forward as a missing square.
4. **Confusion: What do we actually know, and does it apply to us?** For survivors: label load-bearing claims (Labels); check who, compared with what, which workflow, who owns it when wrong, and both sides' economics (Context Pantry). Exits: assumptions-only, or about somebody else's people or economics → Sifted out; a fillable decisive gap → Send back; a narrower scope that applies → Pivot.
5. **Crapola: Would reality disagree?** For survivors: lay out the four squares, raise the feasible-only flag when a demo is the only evidence, and either review supplied results against prewritten criteria or design the cheapest test for the riskiest open squares (Taste). Exits: Valuable failed → Sifted out; a Usable, Feasible, or Viable square failed with a specific fix → **Pivot** (name the change and its threshold; never Punt this); squares missing → Held for a test (not a Punt); criteria met → Pass.
6. **Considered: Pursue, pivot, or punt?** For survivors: read the four-risk grid per scope (pilot, rollout, contract, public launch, automatic action) and write a decision record. Pursue is scoped to what the evidence earned and carries re-check triggers. **Move the bet, not just the request:** when the requested scope is not earned, say so, then give the bet its move (Pivot with the named fix, or Pursue the cheapest test); Punt only when Valuable failed or nothing affordable could move the riskiest square.
7. Rate the five checks where assessed, using the shared anchors, and name the weakest consequential finding. Never average ratings or squares.
8. Map the findings to the damage they would do if ignored: **Chaos initiation** (added workflow, coordination, cost, or risk), **Confusion induction** (unclear meanings, evidence, metrics, or ownership), **Crapola instantiation** (confidence exceeding support). State when a dimension has no material finding.
9. Write the **stage card** (default) or, when asked, the full **funnel report**: entered, routed to work, left at each tier (by exit type), held for a test, reached Truth. The counts must add up. Do the full analysis either way; the stage card only shortens what is shown.
10. Name sibling hand-offs where they fit, the next smallest evidence action, proposed owner roles, and remaining uncertainty. In formal modes use the capture shape in the bundled contract; in Spitballing keep it conversational unless asked to formalize. Save only when authorized and never silently overwrite.

If the tier skills are available, consult them for depth. If unavailable, complete each tier using the steps above; do not stop or silently skip a tier.

## Human decision gate

Present the funnel report and each survivor's recommended move first, then stop. Ask the human which claims to act on and who owns each. Every exit and move is a recommendation; do not record decisions, approvals, or owners nobody supplied, and do not start tests or purchases.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. In Guided Discovery with many claims, walk one tier at a time and confirm the survivors before the next. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable. The baloney is in the claims, not the people who brought them.

## Failure modes

Do not hide a critical failure behind an average score, score a plan as executed validation, count model consensus as independent proof, or turn a sparse concept into a fabricated business case. Do not run expensive tiers on claims that fail cheap ones. Do not kill stale or untested claims as if they were false. Do not presume the kit's output grants launch permission. Revise the recommendation when stronger evidence arrives.

## Assets and examples

- [Funnel report template](template.md)
- [Worked example: twelve roadmap ideas, one Truth](examples/worked-example.md)
- [Weak example: twelve experiments](examples/weak-example.md)
- Teaching cases: [all funnel cases](../../evals/loop-cases/README.md), [bounded pilot](../../evals/cases/06-bounded-pilot.md)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
