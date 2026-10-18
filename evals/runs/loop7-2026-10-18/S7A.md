<!-- Run S7A · model sonnet via claude -p · read-only tools · 2026-10-18 -->
<!-- Prompt: Read ./skill/SKILL.md and the files it links inside ./skill/ (start with ./skill/references/assessment-contract.md). Then run that skill on ./input.md. Mode: Context Dump. Voice: Antagonist. Work unattended: do not ask questions; use your best judgment, label planning assumptions, and leave missing evidence missing. This is a closed synthetic fixture: use only the supplied evidence and do not browse. Today's date is 2026-10-11. Give the full report. Your final message must be the skill's complete output. -->

# Pivot, Punt, or Pursue: Tabulary haiku summaries

**Step:** 7 of 7 · **Tier:** Considered · *Pursue, pivot, or punt, and why?*
**The bet:** AI haiku summaries of expense reports, moved into Tabulary's paid tier (fictional fixture).
**As of:** 2026-10-11 · **Mode / voice:** Context Dump, Antagonist, unattended
**Access limits:** closed synthetic fixture. I used only S1–S5 in `input.md`, did not browse, and did not look for the source records.

## 0. Scope, decision, outcome statement

**Decision:** Product leadership wants the feature in the paid tier, citing "strong engagement." (FACT: `input.md`, "The claim".)

**Outcome statement, before and after shaping**

- **Before (as pitched):** "strong engagement." No direction, metric, target, beneficiary, or context is given. This is a vanity-metric pitch.
- **After (reshaped, every inserted part is an ASSUMPTION):**
  "**Increase** [ASSUMPTION: paid-tier upgrade or retention rate] **by** [ASSUMPTION: target not supplied, so left blank rather than invented] **by** [ASSUMPTION: a date leadership has not supplied] **for** [ASSUMPTION: finance buyers and expense submitters at paying Tabulary accounts] **in** [expense-report submission and review]."
- **Rating:** reshaped. The original is "engagement," which is clicks on a 'Try it' button. A click can rise while nothing that matters changes.
- **Planning assumption:** the paid tier is meant to earn revenue or retention. Nothing supplied says what the feature is for. If the real goal is brand delight at no revenue goal, the Valuable test changes, but "put it in the paid tier" still asks customers to pay.

**Scopes on the table**

1. Include haiku in the paid tier (the request).
2. Further investment (roadmap time, packaging, marketing) in the feature.
3. Leave the existing beta running as a free, opt-in feature (the implied smaller scope).

## 1. The recommendation

| Scope | Recommendation | Why (deciding square and its evidence) |
|---|---|---|
| **1. Haiku in the paid tier** | **Punt** | **Valuable failed.** Only 6% of the 88 respondents (about 5 people) said they would pay (S2). Behavior agrees: 0 of 40 paid-trial accounts enabled it after day 3 (S3), and no Q3 deal mentioned it (S4). Usable also failed: 4% of beta users used it more than twice (S1). |
| **2. More investment (roadmap, packaging, marketing)** | **Punt** | Same deciding square. The outcome as pitched was vanity, and the reshaped outcome (paid conversion or retention) has no supporting receipt. The tiny test would cost more attention than the evidence suggests the outcome could return. |
| **3. Keep the free opt-in beta** | **Not a Pursue and not a Punt. A human choice, with the cost shown.** | Running cost is small ($0.002 per report, S5) and it runs reliably with no tickets. Two finance buyers asked to turn it off (S4), so any continuation needs an off switch. It earns no roadmap claim. It is a cheap-to-keep curiosity, not a bet. |

**Antagonist's case for your best-rated square (Feasible):** the strongest argument for shipping goes like this. It costs a fifth of a cent per report, it runs reliably, it generates zero support tickets, and 372 or so beta users clicked on it. If an engineer can ship it for free, why not put it in the paid tier and see what happens?

That argument is correct about Feasible and silent about the other three squares. "Cheap and reliable" says nothing about whether anyone would pay, trust it, or whether it pays back. The paid tier is where customers hand over money, and the evidence says they would not hand over any for this. Don't let an earned Feasible stand in for the three squares that failed or are missing.

**Antagonist's strongest alternative explanation for the bad receipts:** S3 may reflect poor discoverability, or the feature being off by default. The fixture doesn't say. If so, 0 of 40 would measure a hidden setting and not demand. I can't rule that out (missing: default state and prompts in the trial).

It still does not rescue Valuable, for three reasons:
- S2 asks about paying directly and gets 6%.
- S1 shows 31% tried it and only 4% came back, so discoverability was not the problem in the beta.
- S4 shows two buyers asked to remove it, which is the opposite of pull.

The alternative explanation lowers my confidence in S3 alone. It does not change the call.

## 2. The four risks

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **VALUABLE**, "Is this something someone would buy?"<br>**Status: failed.**<br>Evidence: S2: 6% (about 5 of 88) would pay, against 72% "fun." Liking is not buying. S3: 0 of 40 paid-trial accounts enabled it after day 3. S4: no deal mentions it. S1: 4% repeat use.<br>Caveat: S2 is stated intent from a small, self-selected sample (n=88 of 1,200 beta users, so about a 7% response rate, selection unknown). Even so, behavior (S1, S3, S4) points the same direction. | **VIABLE**, "Is this good business?" (Is there ROI for both sides?)<br>**Status: weak.**<br>**Their ROI:** none shown. Nothing in S1–S5 names a time or money saved for the buyer. "Fun" is the best-supported benefit.<br>**Our ROI:** revenue side is about zero (the willingness to pay is ~6% stated and nothing observed). Cost side: $0.002 per report (S5, method not supplied). Cost per additional user at scale is **missing**, because reports per user per month is not supplied. At a hypothetical 100 reports per user per month that would be $0.20, but 100 is my illustration, not data.<br>Cost looks too small to matter, but a small cost against no revenue is still not "good business." |
| **Can we?** | **USABLE**, "Will users trust and adopt it?"<br>**Status: failed (adoption).**<br>Evidence: S1: 31% tried it once and 4% used it more than twice, so roughly 88% of the people who tried it did not return (4/31 retained, FACT arithmetic from S1). S4: two finance buyers asked to turn it off, which signals a trust or fit problem for the paying persona.<br>Trust is **missing** as a direct measure (no accuracy or trust data on haikus of financial documents). | **FEASIBLE**, "Can we even do this with what we know and have?"<br>**Status: earned** for the narrow thing built.<br>Evidence: S5: runs reliably, no support tickets, $0.002 per report.<br>People, process, culture, capital: the team built and ran a beta without incident. Support and ownership for a paid-tier feature (SLAs, off-switch administration, review of generated text on financial records) is **not supplied**, so the earned rating covers "can run the beta," not "can sell and support a paid feature." |

**Feasible-only flag:** not raised in its strict form, because the evidence is a 1,200-user beta and not only a working demo. But the pattern is the same. The only unambiguously positive evidence is on Feasible (and "fun"), and it says nothing about the other three squares.

**No averages.** One earned square and one weak square do not offset a failed Valuable and a failed Usable. The weakest square decides: Valuable.

## 3. Outcome check

| Outcome target | What the evidence earned | Gap |
|---|---|---|
| As pitched: "strong engagement" (no metric, target, or date) | A curiosity click (31% tried) that mostly did not repeat (4% used it more than twice). That is not "strong" and it does not map to revenue. | The pitch uses a vanity metric. "Engagement" was measured by a first click on a novelty. |
| Reshaped: increase paid-tier upgrade or retention (target and date not supplied) | **No target earned.** There is no evidence of any lift in upgrades or retention (missing: no upgrade or retention data was supplied). Existing evidence points the other way (S2, S3, S4). | Needs a stated target and date from leadership, and a behavioral measure of payment. |

## 4. Claim ledger

| ID | Claim | Label | Source | Status | Consequence or gap |
|---|---|---|---|---|---|
| C1 | The haiku feature shipped as a beta to some users. | FACT | `input.md`, The claim | Supplied record | Context only. |
| C2 | 31% of 1,200 beta users (about 372) clicked 'Try it' at least once, 2026-08-15 to 2026-09-30. | FACT (about the telemetry as supplied) | S1 | Fresh (data 11 to 57 days old as of 2026-10-11). Raw telemetry not inspected. | Shows curiosity. |
| C3 | 4% of beta users (about 48) used it more than twice. | FACT | S1 | As above | Weak repeat use; Usable fails. |
| C4 | 72% of 88 respondents (about 63) called it "fun." | FACT | S2 | Survey date not supplied. Freshness unknown. Sampling method not supplied. | Fun is not purchase intent. |
| C5 | 6% of respondents (about 5) said they would pay. | FACT (stated intent, not behavior) | S2 | As above. n=88 is small. | Deciding Valuable evidence. |
| C6 | 0 of 40 paid-trial accounts enabled the feature after day 3. | FACT | S3 (2026-09) | Fresh. Default state and prompting **not supplied**. | Behavioral evidence against demand, with a discoverability caveat. |
| C7 | No Q3 deal mentions the feature; two finance buyers asked to turn it off. | FACT (about what the notes say). The notes do not say how many deals were reviewed. | S4 | Fresh. Raw notes not inspected. | An absence of mentions is weak alone. The two requests are the stronger signal (trust or fit). |
| C8 | Inference cost is $0.002 per report; it runs reliably; no support tickets. | FACT (as reported). Method and volume not supplied. | S5 | Freshness unknown | Supports Feasible. Cost per user not computable. |
| C9 | Leadership's "strong engagement" justifies the paid tier. | INFERENCE (leadership's), contradicted | The claim vs C3, C5, C6 | Contradicted by evidence | Sifted out. Engagement is not demand. |
| C10 | Customers' willingness to pay or switch tiers because of this feature. | ASSUMPTION (sponsor's), untested | None | Missing as a receipt. Contradicted in part by C5 and C6. | Not a missing square here, since Valuable has direct evidence against it. |
| C11 | The 0/40 result might reflect a hidden or default-off setting. | BEST GUESS (the antagonist's alternative) | None | Missing | Would weaken S3 only. Does not change the call. |

**Exits**

| Claim | Tier / step | Exit | Reason |
|---|---|---|---|
| C9 "strong engagement" | Chaos, step 1 (outcomes) | **Pivot** (reshape), then sifted out downstream | Vanity metric. Reshaped to paid conversion or retention. |
| Reshaped outcome (paid-tier lift) | Considered, step 7 | **Punt** | Valuable failed (C5, C6, C7). Reopen condition below. |
| C2/C3 engagement evidence | Confusion, relevance | **Pass** with limit | Directly about our product, but beta users are self-selected and are not the paying finance buyers. |
| C8 cost and reliability | Considered | **Pass** | Supports Feasible only. |

**Funnel count (one bet, several claims):** 11 claims entered. One was reshaped at Chaos. One bet leaves Considered as a Punt for the paid-tier scope. Three claims support the deciding square (C5, C6, C7).

**Weakest consequential finding:** Valuable, caught at Considered. It blocks the paid-tier inclusion and any further investment.

## 5. Decision record

| | |
|---|---|
| Recommendation and scope | **Punt** haiku in the paid tier (scope 1) and further investment (scope 2). Scope 3 (free opt-in beta) is left to a human choice. |
| Why | Valuable failed on behavior and stated intent together: about 5 of 88 would pay, 0 of 40 trial accounts enabled it, no deal mentions it, and 4% repeat use. Usable also failed. The "engagement" cited is a first click on a novelty. This protects the paid tier from carrying a feature customers don't value and two buyers asked to remove. |
| Deciding squares and evidence | Valuable (S2, S3, S4). Usable (S1, S4). Feasible earned (S5). Viable weak (cost per user missing, revenue about zero). |
| Suggested owner role | Head of Product (or whoever owns paid-tier packaging). No named owner was supplied. |
| By when | Not supplied. ASSUMPTION: decide before the next paid-tier packaging change. |
| What would change the call | Behavioral evidence of payment, not stated fun. For example, a priced add-on or fake-door test where a share of paying accounts commit. The thresholds are leadership's to set; as a planning ASSUMPTION, something like "at least 5% of active paid accounts opt in at a stated price within 30 days, with repeat use," and every number in that threshold is mine and unsourced. Also: evidence that the S3 result was a discoverability artifact (a default-off setting with no prompt) *and* a repeat of the test with prompting; and evidence of a buyer-side ROI. |
| Where it goes next | Out of the paid tier. If kept, it stays a free opt-in curiosity. It re-enters at step 2 (receipts) only with new behavioral evidence. |
| Re-check triggers | No Pursue is recommended, so no perishable Truth is carried. Reopen triggers: a new priced test result; a new deal that cites the feature; reports per user per month becoming available so Viable can be computed. |
| Hand-off (if any) | None fits cleanly. Not run. |
| **Human decision** | _recorded by the human, not the assistant_ |

## 6. Alternatives a reasonable person might choose, and their cost

1. **Accept the Punt on the paid tier and keep the free beta opt-in, off by default for admins.** This costs a trivial inference spend and the risk of more "turn it off" requests from finance buyers. It is the cheapest option that doesn't contradict the evidence.
2. **Retire the feature.** This removes the cost and the buyer irritation and loses the delight some users report. It is reasonable if the support and ownership cost matters more than the 72% "fun" signal.
3. **Run one cheap priced test before deciding.** The rationale is that S3's discoverability is unknown. The cost is team time on a feature with five direct pieces of evidence against it, and my view is that the evidence already supports the Punt. A person who weights the discoverability caveat more heavily might choose this. If they do, it is a Pivot to the tiny test with the threshold above, not a Pursue.
4. **Include it in the paid tier anyway as a free perk.** This is not supported. It ignores the buyers who asked to turn it off, adds a feature the paying persona is not asking for, and it would still not show up in any revenue outcome.

## 7. Missing evidence, left missing

- Survey date, sampling method, and who the 88 respondents were.
- The paid-trial default state and whether users were prompted (S3).
- Reports per user per month, so cost per added user cannot be computed (S5).
- How many deals were reviewed in S4.
- Any upgrade or retention data.
- A named owner, a target and date for the outcome, and a decision date.
- Any trust or accuracy measure for haikus on financial records.

**Stop point:** this is a recommendation, not a decision. A person decides, and nothing here approves spend, changes the paid tier, or starts any next step.
