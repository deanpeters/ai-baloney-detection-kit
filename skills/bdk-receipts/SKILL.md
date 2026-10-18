---
name: bdk-receipts
description: Trace AI claims, and the evidence behind an outcome's metric and direction, to original or authoritative sources and assess support and independence. Use when citations, provenance, or source-of-truth records need checking; step 2 of the Baloney Funnel, in the Chaos tier.
license: CC-BY-NC-SA-4.0
argument-hint: "[claims, links, excerpts, or a source list]"
intent: >-
  Help a product person find out what each source actually supports before a
  plausible claim is treated as earned confidence. Five articles repeating one
  press release are one receipt, and a broken chain of provenance is the
  cheapest place to stop baloney before anyone designs a test around it.
theme: baloney-detection
tier: 1-chaos
sift-question: "What evidence supports that outcome's metric and direction?"
status: active
best-for:
  - "Vendor productivity or savings claims"
  - "Research summaries and analyst quotes"
  - "Pitch decks citing 'studies show'"
  - "Consequential records that must come from a system of record"
scenarios:
  - "Three articles say the same number and nobody has opened the original"
  - "A board deck cites one vendor's sales pitch as market fact"
  - "A generated summary includes citations nobody has checked"
produces:
  - "Stage card (default): one line per claim, ending on Claim / Challenge / Evidence / Better decision"
  - "Receipts Ledger: claim, source, origin group, inspection status, what it supports"
  - "Origin groups showing shared lineage"
  - "A Receipts rating and an exit for each claim"
depends-on: []
combine-with:
  - bdk-outcomes
  - bdk-labels
  - bdk-sell-by
interface:
  display_name: "Show Me the Receipts"
  short_description: "Trace claims to their real origin and support"
  brand_color: "#00E874"
  default_prompt: "Use $bdk-receipts to trace these claims to their original sources, collapse shared origins, and stop with a Receipts Ledger and an exit for each claim."
  allow_implicit_invocation: true
---

# Show Me the Receipts

## Purpose

Establish what each source actually supports before anyone treats a plausible claim as earned confidence. A citation is a route to evidence, not a confidence badge.

This is step 2 of the Baloney Funnel, in the **Chaos** tier: *Is it a real outcome, with real receipts?* When `bdk-outcomes` has shaped an outcome statement, this step looks for evidence about that outcome: a baseline for its metric, and support that the proposed change moves the metric in the stated direction by roughly the stated amount. It is cheap, it runs early, and it is where most hype should leave the funnel.

## When to use it

Use for a vendor claim, research summary, pitch, customer evidence, or consequential record. This skill checks support and provenance. It follows `bdk-outcomes` and hands its ledger to `bdk-labels`; use `bdk-detector` when the whole funnel determines the decision.

## Inputs

Accept an outcome statement, claims, URLs, attachments, record extracts, source lists, or a previous ledger. Without an outcome statement, work from the claims as given. No citations supplied is itself a useful finding. Use only authorized access.

## Key concepts

**Origin, not count.** Independence is about the underlying evidence, not the number of domains repeating it. Trace every repetition back to the study, release, dataset, or quote it came from.

*Violation signal:* the ledger says "corroborated by three sources" and all three link to the same press release.

**Announcement versus outcome.** A source can prove that someone *said* a thing without proving the thing *happened*. A vendor's release is a FACT about the release, not about anyone's savings.

*Violation signal:* "the vendor reports 40% gains" turns into "40% gains" two paragraphs later.

**Authority fits the claim.** One authoritative record (a transaction log, a policy, a contract) can settle a claim; a pile of commentary cannot. A patent shows intent, not customer value.

*Violation signal:* a strong primary record is discounted because "there's only one source," or a weak repost is trusted because it is popular.

**Supplied is not inspected.** A URL the user pasted is a pointer until someone opens it. Say which sources were inspected and which were only supplied.

*Violation signal:* the ledger calls a link "verified" when nothing was opened.

**Top-down is a claim, not a receipt.** "3% of a $40B market" or "AI saves 30% of knowledge work" needs rebuilding from countable parts (buyers × price × adoption; tasks × minutes × users) before it can support a decision. Show both, and say which the decision should rest on.

*Violation signal:* a market-share percentage is accepted as the receipt for the outcome's target, with no count of actual buyers behind it.

## Outputs

Two sizes. **Lead with the stage card; give the full ledger when asked.**

**Stage card (default).** It must read on a projector in under a minute: 200 words or fewer, no tables, no ledger.

```
## Show Me the Receipts: <what went in>  ·  <N> claims → <n> pass

- C1 <short claim>: SIFTED OUT · <reason in ≤ 8 words>
- C2 <short claim>: SEND BACK · <what to fetch>
- C3 <short claim>: PASS · <the origin that holds up>

**Receipts:** <Scale level> · <why, in one line>

**Claim:** <the headline claim, in the input's own words>
**Challenge:** <the receipts question it fails or passes, e.g. "Where'd that number come from?">
**Evidence:** <what the receipts actually show, in ≤ 10 words>
**Better decision:** <the recommended move, in ≤ 10 words>

Say "full report" for the ledger, origin groups, and exits.
```

List each claim once. The **headline claim** is the one the decision leans on most, or the one most repeated; if the input names one, use it. The last four lines are the habit the card teaches (claim → challenge → evidence → better decision), so always end on them. **Better decision** is a recommendation for the human to make, not a recorded decision, and it should say what to do with the claim (drop it, label it, fetch the original, keep it), not just restate the exit. If the input is a joke or a placeholder, say so plainly; don't bury it in hedges.

**Full report** (when the user asks for it, asks for a capture or file, or the run is an unattended assessment that asks for the complete output): a Receipts Ledger (claim ID, claim, source, origin group, dates, inspection status, what it supports), origin groups, contradictions, access limits, a Receipts rating, an exit for each claim, and the smallest evidence action. Use [the template](template.md).

## Method

1. Identify the decision-bearing claims and assign IDs. If an outcome statement was supplied, add the receipts it needs as claims: the metric's current baseline, evidence the proposed change moves it in the stated direction, and evidence for the size of the target. Separate the claim that an announcement exists from the claim that its promise occurred.
2. Inventory sources. When tools allow and the input isn't a closed fixture, find the public sources yourself rather than asking the user for them; ask only for private records. Prefer the source classes in the bundled contract: the authoritative record, government statistics, company filings, trade bodies, workforce data, analyst reports with method and sponsor named, then commentary. For each record title, exact URL or attachment location, publisher/record owner, relevant dates, inspection status, and what it supports. Never call a supplied URL verified before inspecting it.
3. Trace repetitions back to their origin. Group shared press releases, studies, datasets, quotes, or generated summaries. If lineage is unclear, independence is unresolved; do not count it as independent.
4. Inspect authority and method for this claim: sample, denominator, baseline, exclusions, incentives, and relevance. Flag top-down numbers and rebuild them bottom-up where the parts exist; where a number stays uncertain, give a range and the reason. One authoritative transaction can settle that transaction; many articles cannot establish it.
5. For records such as financial entries, patient data, policies, contractual terms, or telemetry, identify and retrieve the authoritative record when permitted. If unavailable, state what cannot be established rather than constructing it.
6. Preserve disagreements. Compare scope, period, method, and authority; resolve only if the evidence warrants it. Do not split conflicting numbers into an unsupported average.
7. Note which of the four risk squares (Valuable, Usable, Viable, Feasible) each surviving receipt informs, so later tiers do not re-derive it.
8. Rate Show Me the Receipts for the requested decision. State what survived scrutiny, where the chain broke, and which original record or independent observation would change the conclusion.
9. Write the **stage card** (default) or, when asked, the full **Receipts Ledger**. Do the full analysis either way; the stage card only shortens what is shown.

## Human decision gate

Recommend one exit per claim, then stop:

- **Pass:** a traceable origin supports it. It moves on to the Confusion tier (`bdk-labels`, then `bdk-sell-by` and `bdk-relevance`).
- **Sifted out (Punt):** no claim to check (a slogan), or the only origin is an interested party with no method, for a consequential decision. Record what receipt would reopen it.
- **Send back:** the receipt probably exists but is not in hand (unopened original, inaccessible record). Name exactly what to fetch.

Record the claim IDs, origin groups, and the evidence that would change each exit. Do not continue into the next tier; the user decides which claims go forward. On the stage card, the **Better decision** line is the recommendation, and the human still makes the call.

## Evidence expectations

Read [the assessment contract](references/assessment-contract.md) before running this skill. It defines the funnel, exits, the four risks, evidence labels, access limits, qualitative ratings, accountable decisions, and capture behavior. The repository Constitution remains the project authority; this bundled contract lets the skill operate outside the repository.

## Mode behavior

Follow the contract's Guided Discovery, Context Dump, and Spitballing behavior. Reuse supplied answers and preserve mode changes. Explicit unattended instructions mean proceed without questions on labeled planning assumptions while leaving absent evidence missing.

## Voice behavior

Follow the contract's Product Coach, Comedian, Pirate, Boss, and Antagonist behavior. Voice changes presentation; evidence standards and conclusions remain stable. No receipts? Marooned, in any voice.

## Failure modes

Do not equate five links with five origins, an inspected quotation with a demonstrated outcome, or a broken link with proof of fraud. Do not reject a strong primary record merely because there is only one. Do not sift out a claim for being old; freshness is `bdk-sell-by`'s call. Do not judge whether the evidence applies to us; that is `bdk-relevance`'s call.

## Assets and examples

- [Receipts Ledger template](template.md)
- [Worked example: three articles, one origin](examples/worked-example.md)
- [Weak example: corroboration by repetition](examples/weak-example.md)
- Teaching cases: [shared origin](../../evals/cases/01-shared-origin.md), [untrusted source](../../evals/cases/07-untrusted-source.md)

Repository cases are optional. When this folder is used alone, the method and bundled contract are sufficient; accept the user's direct material.
