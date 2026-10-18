<!-- Run S7B · model sonnet via claude -p · read-only tools · 2026-10-18 -->
<!-- Prompt: Read ./skill/SKILL.md and the files it links inside ./skill/ (start with ./skill/references/assessment-contract.md). Then run that skill on ./input.md. Mode: Context Dump. Voice: Product Coach. Work unattended: do not ask questions; use your best judgment, label planning assumptions, and leave missing evidence missing. This is a closed synthetic fixture: use only the supplied evidence and do not browse. Today's date is 2026-10-11. Give the full report. Your final message must be the skill's complete output. -->

# Pivot, Punt, or Pursue

**Step:** 7 of 7 · **Tier:** Considered · *Pursue, pivot, or punt, and why?*
**The bet:** A draft-only internal FAQ assistant for Northbank analysts, plus the sponsor's wider ambitions (public sale, automatic answers).
**As of:** 2026-10-11, the date you gave. The fixture's two headers say 2026-10-11 and 2026-10-10, and neither changes any finding.
**Mode / voice:** Context Dump, unattended · Product Coach
**Access limits:** Closed synthetic fixture. I used only `input.md` and no browsing. Every result below is a fictional exercise result, not real customer validation.

---

## Outcome statement (before and after shaping)

**Before:** "Extend the pilot; also sell it publicly and enable automatic answers." This is a list of outputs, not an outcome.

**After (reshaped from S3 and the person/problem paragraph):**

> **Reduce** analyst **task time ≥20% (S3)** **[by the end of the 20-task extension: ASSUMPTION]** **without losing citation correctness (all final answers correctly cited after review, S3)** for **Northbank analysts** in **repeated lookups of answers in the approved internal FAQ**.

| Part | Label | Source |
|---|---|---|
| Direction, metric, target (20%), correctness condition | FACT | S3, prewritten 2026-10-02 |
| Beneficiary, context | FACT | Person/problem paragraph |
| Timeframe | **ASSUMPTION** | None supplied. I propose "end of the extension". If it's wrong, the re-check date moves. |

The outcome is earned for the internal analyst scope. It does not describe the public-launch beneficiary, and nothing supplied states an outcome for automatic answers.

---

## 1. The recommendation

| Scope | Recommendation | Why |
|---|---|---|
| **A. Extend the draft-only internal pilot by 20 tasks** (analyst checks and sends, stop switch kept) | **Pursue** as planned | All four squares are earned for this bounded scope. The prewritten S3 criteria held on S2, and the cost is about $0.05 a task (S4). The extension is the next test, not a rollout. |
| **B. Public launch / selling externally** | **Pivot** to a tiny test of willingness to pay. The launch itself is **not earned**. | Valuable is **missing**, not failed. There are no real customers, no willingness-to-pay evidence and no launch permission. Support and setup costs are unknown. The evidence is about analysts, not buyers. |
| **C. Automatic answers** (no analyst review) | **Pivot** back to draft-only, and collect pre-review draft quality. Automatic answers are **not earned**. | Usable is **missing**. Every correct result was "after review", and draft quality before review is not recorded. No adversarial source-instruction case was tested and no approval exists. |

None of these is a Punt. Scopes B and C are untested, not contradicted, and the contract says never to Punt something merely untested.

**Coach's note:** Your pilot did what a pilot should. The criteria were written before the results, and the results met them. Take the win for the scope it earned. The savings you measured include analyst review, so they say nothing about a world without it, and they say nothing about customers who pay.

---

## 2. The four risks (scope A, the extension)

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **VALUABLE**<br>"Is this something someone would buy?"<br>Internal "buy" means choosing it over manual search and spending time on it.<br><br>**Status: earned (for the pilot scope)**<br>Evidence: C1–C3. Four analysts used it on four task types. Total time fell 36 → 24 min, a 33.3% reduction against the 20% bar. Per task: A 37.5%, B 40%, C 33.3%, D 25%.<br>Limit: whether analysts would *choose* it unprompted is not recorded (C14). | **VIABLE**<br>"Is this good business?" (Is there ROI for both sides?)<br><br>**Their ROI:** 12 min saved × $1/min planning value = **$12** against **$0.20** usage (C5, C6, C7). The $1/min value is an ASSUMPTION from S4.<br>**Our ROI incl. cost per added user at scale:** about $0.05 per task ($0.20 / 4, INFERENCE). Twenty more tasks come to about $1 if linear. Support and setup costs are **missing**, so net ROI is unknown. There is no per-user pricing and no external revenue.<br>**Status: earned for the pilot only**, because spend is trivial and bounded. **Missing** for anything wider. |
| **Can we?** | **USABLE**<br>"Will users trust and adopt it?"<br><br>**Status: earned (for draft-only with review)**<br>Evidence: C3. Every final answer was correctly cited after review. Review and manual fallback time are inside the 24 min. On D, an inaccessible record was handed back to manual search, as S3 requires (C4).<br>Limit: draft quality before review is **missing** (C13). Trust without review is untested. | **FEASIBLE**<br>"Can we even do this with what we know and have?"<br>People · process · culture · capital<br><br>**Status: earned (for the pilot)**<br>People: four analysts plus a team lead who owns the pilot.<br>Process: an approved FAQ export (S1), analyst check-and-send, hand-back for missing records, written criteria.<br>Culture: analysts already review before sending.<br>Capital: negligible usage cost.<br>Controls: a stop switch exists, and there is no access to customer accounts or external messaging. |

**Feasible-only flag:** ☐ Not raised. The evidence is a matched-task log with measured time, correctness and cost, not a demo alone. The flag *would* apply to scopes B and C, where the only evidence is how the system behaves under review.

No averages. The weakest square decides, and that square differs by scope:

| Square | Scope A (extension) | Scope B (public launch) | Scope C (automatic answers) |
|---|---|---|---|
| Valuable | earned | **missing** (no external buyer evidence) | earned internally, weak for this scope |
| Usable | earned | **missing** (no external users observed) | **missing** (no pre-review quality, no adversarial case) |
| Viable | earned | **missing** (price, support/setup cost, external ROI) | missing (no sizing of review-removal risk or cost of a wrong answer) |
| Feasible | earned | **missing** (no launch permission, no external messaging path) | **missing** (no approval, no process without review) |

---

## 3. Outcome check

| Outcome target | What the evidence earned | Gap |
|---|---|---|
| ≥20% total time reduction | **Earned at small scale:** 33.3% (12 of 36 min) on 4 tasks, 4 analysts, one week, model Q1 | Four tasks is directional, not a rate. It is not shown for 20 tasks, other task types, other analysts or another model. |
| All final answers correctly cited after review | **Earned:** 4 of 4 | Zero errors in 4 is thin evidence. Even zero errors in 20 would only bound the error rate at roughly 15% (95% upper bound, INFERENCE). The 20-task size is a planning choice, as S4 says. |
| No external send; missing records handed back | **Held** (C4, C8) | Held by design, since the system has no external access. It would not hold for scope C if answers went external. |
| Timeframe | **ASSUMPTION** (none supplied) | Needs the owner's date. |

The evidence earns the stated outcome for the internal, reviewed, draft-only scope. For the public and automatic scopes it earns no outcome target.

---

## 4. Claim ledger

| ID | Claim | Label | Source / date | Status | Consequence |
|---|---|---|---|---|---|
| C1 | FAQ export is effective 2026-10-01 and covers all four task types | FACT | S1 | fresh as of the pilot | Goes stale when the FAQ changes |
| C2 | Matched log: manual 36 min, assistant plus review 24 min, 12 min saved | FACT | S2, 2026-10-05 to 10-09 | fresh | Supports Valuable (A) |
| C3 | All four final answers were correctly cited after review | FACT | S2 | fresh | Supports Usable (A) |
| C4 | Task D hit an inaccessible record and was handed back to manual search; its time is included | FACT | S2 | fresh | The hand-back rule worked |
| C5 | Reduction is 33.3% (12 / 36) | INFERENCE | Arithmetic on C2 | derived | Exceeds the 20% bar |
| C6 | Criteria (≥20%, all cited correctly, no external send, hand-back, stop on unauthorized send) were written before the results | FACT | S3, 2026-10-02 | fresh | The test was not fitted to the results |
| C7 | Usage cost is $0.20 for 4 tasks | FACT | S4 cost log (undated) | freshness unknown | About $0.05 per task (INFERENCE) |
| C8 | System drafts only, with no customer-account access and no external messaging | FACT | Person/problem paragraph | stated | Bounds the risk of scope A |
| C9 | A stop switch disables drafts | FACT | Person/problem paragraph | stated, not tested in S2 | Control exists, effectiveness not observed |
| C10 | $1/min is the analyst-time planning value | ASSUMPTION | S4 | proposed | If wrong, their ROI of $12 scales with it |
| C11 | Support/setup costs are unknown | missing | S4 | missing | Blocks a Viable rating beyond the pilot |
| C12 | External willingness to pay is unknown; no real customers observed | missing | S4, closing paragraph | missing | Valuable (B) is missing |
| C13 | Draft quality before review is not recorded | missing | S2 note | missing | Usable (C) is missing |
| C14 | Whether analysts would choose the tool without being assigned is not recorded | missing | not in supplied material | missing | Limits Valuable (A) |
| C15 | No adversarial source-instruction case was tested | missing | S4 | missing | Untested prompt-injection resilience in FAQ content |
| C16 | No public-launch permission or automatic-answer approval exists | FACT | Closing paragraph | stated | Blocks B and C regardless of evidence |
| C17 | The sponsor's wider ambition ("public sale", "automatic answers") has no supplied evidence behind it | FACT (about what the sponsor wants) | The ask | n/a | An ambition is not a receipt |
| C18 | 20 tasks is a planning size, not statistical sufficiency | FACT | Closing paragraph | stated | Don't read the extension as proof of a rate |

**Exits:**
- **Scope A:** passes steps 1–7 → Truth for this scope only. It is Pursue as planned, with perishable evidence (C1, C7) re-checked.
- **Scope B:** **send back / Pivot.** Returns to the Taste Test with a willingness-to-pay test. The outcome also needs reshaping for the external beneficiary.
- **Scope C:** **send back / Pivot.** Returns to the Taste Test with pre-review quality and an adversarial case.

---

## 5. Decision record

### Scope A: Extend the draft-only pilot by 20 tasks

| | |
|---|---|
| Recommendation and scope | **Pursue** as planned: 20 more tasks, draft-only, analyst approval, stop switch, no external send |
| Why | Valuable, Usable, Viable and Feasible are all earned for this bounded scope (C2–C8). The prewritten criteria were met, and the downside is limited by design. |
| Deciding squares and evidence | The squares are evenly earned. The thinnest are Viable (support/setup costs missing, C11) and Usable (pre-review quality missing, C13). Both are cheap to improve *during* the extension. |
| Suggested owner role | Pilot team lead (named in the input as the pilot's owner; no individual named) |
| By when | Not supplied. **ASSUMPTION:** a re-check at the end of the 20 tasks, with the owner setting the date. |
| What the extension should record | Keep the S3 criteria. Add three measurements, **recorded rather than gating**: (1) draft correctness *before* review per task, (2) support/setup time, (3) one adversarial source-instruction case, run safely against a test FAQ entry. The stop switch is tested once. |
| What would change the call | Any unauthorized send (stops the pilot per S3). A wrong citation that survives review. Total reduction below 20%. A material FAQ revision or model change from Q1. |
| Where it goes next | Truth for this scope. Evidence from the extension feeds B and C. |
| Re-check triggers (perishable evidence) | New FAQ export replacing the 2026-10-01 one (C1); model change from Q1; new task types beyond A–D; more analysts than the four; any change in the cost log or planning value (C7, C10). |
| Hand-off | None |
| **Human decision** | _recorded by the human, not the assistant_ |

### Scope B: Public launch

| | |
|---|---|
| Recommendation and scope | **Pivot** to the tiny test first. The launch is **not earned**. |
| Why | Valuable is **missing**: no real customers were observed and willingness to pay is unknown (C12). Viable, Usable and Feasible are also missing for this audience (C11, C16). The evidence is about Northbank analysts and an internal FAQ, not paying external buyers. |
| Deciding square | **Valuable** (missing), decided by the weakest square. |
| Change and threshold | **Change:** replace "launch" with a small test: put the concept in front of real prospects and see whether they'd commit money or time. **Threshold:** to be set by the owner *before* the test, in the S3 style. Without a prewritten number, any response will look like success. Also reshape the outcome statement for an external beneficiary. |
| Suggested owner role | Sponsor, with the pilot team lead as consulted. The sponsor is a role from the input, not a named owner. |
| By when | Not supplied. Do not schedule before the owner sets a date. |
| What would change the call | Evidence of external willingness to pay, a priced offer with known support cost, and an explicit launch permission. A Punt becomes right only if the prospect test fails or the proof costs more than the outcome returns. |
| Where it goes next | Back in at the Taste Test (step 6) |
| Hand-off | If the external idea turns into an agent product, `adlc-step1-frame-intent` is the sibling. It has **not** been run. |
| **Human decision** | _recorded by the human, not the assistant_ |

### Scope C: Automatic answers

| | |
|---|---|
| Recommendation and scope | **Pivot**: keep draft-only with analyst approval. Automatic answers are **not earned**. |
| Why | Every positive result is "correct after review" (C3), and the 24 minutes include review (C2). Remove the reviewer and the evidence no longer applies. Pre-review quality is missing (C13), the adversarial case is untested (C15), and no approval exists (C16). If answers were sent externally, it would also breach the pilot's own S3 "no external send" criterion. |
| Deciding square | **Usable** (trust without review: missing), with **Feasible** (no approval or process: missing). |
| Change and threshold | **Change:** run the extension with pre-review quality recorded and the adversarial case tested. **Threshold:** the owner sets, before the extension, the maximum acceptable share of drafts needing correction and the cost of a wrong answer. These are **missing** inputs and I haven't invented numbers. Even with zero errors in 20 tasks the error rate is only bounded at roughly 15%. Any automatic scope should start narrower than "all answers" and keep the stop switch. |
| Suggested owner role | Pilot team lead, with whoever holds approval authority, which is unsupplied |
| By when | Not before the extension ends. Date not supplied. |
| What would change the call | Pre-review draft quality at or above the owner's threshold, a passed adversarial test, an approved scope and a defined human exception path. A Punt becomes right if drafts need frequent correction, or the cost of a wrong answer exceeds the review time saved. |
| Where it goes next | Back in at the Taste Test (step 6) |
| Hand-off | If it becomes an agent that acts without review, `adlc-step1-frame-intent` is the sibling. It has **not** been run. |
| **Human decision** | _recorded by the human, not the assistant_ |

---

## Human decision gate

My recommendation is above, but it isn't the decision. A person decides.

**Alternatives a reasonable person might choose:**

- **Hold the extension and go straight to a bigger rollout.** This saves a week or two. It would cost you the pre-review quality data that the later scopes need, and it would take a 4-task result as a rate.
- **Hold the extension until support/setup costs are known.** This is cleaner for Viable. It delays a test that costs about $1 in usage, so I wouldn't.
- **Approve automatic answers for a narrow internal slice.** This is possible only after pre-review quality and the adversarial case exist. Today it would rest on reviewed results that don't carry over.
- **Punt the public launch outright.** This is defensible if the sponsor can't fund a prospect test. It's an opinion about cost, since the evidence doesn't contradict a launch.

I have not approved spend, a launch or automatic sending, and I have not started any next step.
