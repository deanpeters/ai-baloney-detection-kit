# Skill Catalog

One mission: help product people sift AI claims, ideas, and products down to what has earned the next investment. Sort your work, then check your claims.

## The Baloney Funnel

A process of elimination by tiers. The cheapest sifts run first; most baloney should leave in minutes, and only survivors earn an expensive test. What comes out the bottom is **Truth**, scoped to the bet it earned, with a sell-by date of its own.

| Tier | Question | Skill | Invoke when | Produces | Human gate |
|---|---|---|---|---|---|
| — | *Whole funnel* | [`bdk-detector`](../skills/bdk-detector/SKILL.md) | One claim end to end, or a pile: a roadmap, a stack of pitches | Stage card by default (≤ 200 words, projector-readable); full funnel report on request | Which claims to act on, and who owns each |
| **1 Chaos** | Is it real, and is it still true? | [`bdk-receipts`](../skills/bdk-receipts/SKILL.md) | Citations, provenance, or "studies show" need checking | Stage card (default) or Receipts Ledger | Which claims go forward |
| **1 Chaos** | | [`bdk-sell-by`](../skills/bdk-sell-by/SKILL.md) | Models, prices, policies, or an earlier decision may have changed | Freshness Ledger with re-check triggers | Refresh, or go forward |
| **2 Confusion** | What do we actually know, and does it apply to us? | [`bdk-labels`](../skills/bdk-labels/SKILL.md) | Polished wording hides what's fact and what's hope | Labeled Claims | Which claims the decision rests on |
| **2 Confusion** | | [`bdk-context-pantry`](../skills/bdk-context-pantry/SKILL.md) | For whom, compared with what, at what cost to each side, is unclear | Context Inventory | Fill the gap, or stop |
| **3 Crapola** | Would reality disagree? | [`bdk-taste-test`](../skills/bdk-taste-test/SKILL.md) | A bet is about to advance on a demo or a promise | Taste Test: cheapest tests, thresholds first | Approve the test and its owner |
| **4 Considered** | Pursue, pivot, or punt? | [`bdk-four-risks`](../skills/bdk-four-risks/SKILL.md) | It's time to decide what the evidence has earned | Four-Risk Grid and decision record | Pursue, pivot, or punt, for a named scope |

Every claim leaves a tier one of four ways: **Pass** · **Sifted out** (punt) · **Send back** (missing or stale, so back to the top) · **Pivot** (change one thing, re-enter at that tier). Missing is not failed; stale is not false.

Use the tier skills on their own when you only need one check. Use `bdk-detector` for the whole funnel. No skill requires an upstream artifact.

### The four risks (Considered)

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **Valuable:** "Is this something someone would buy?" | **Viable:** "Is this good business?" (Is there ROI for both sides?) |
| **Can we?** | **Usable:** "Will users trust and adopt it?" | **Feasible:** "Can we even do this with what we know and have?" |

## Supporting utilities

**These are not tiers.** The funnel never calls them, nothing downstream requires them, and each stops with its own artifact. At most six may exist; a utility earns its place only by handing an artifact to a named tier or taking one from it. See [the skill spec](../docs/SKILL-SPEC.md).

| Utility | Supplements | Invoke when | Produces |
|---|---|---|---|
| [`bdk-util-slice-the-pitch`](../skills/bdk-util-slice-the-pitch/SKILL.md) | Into Chaos | You have a deck, release, or roadmap slide, not a list of claims | Claim list ready for the funnel, adjectives set aside |

Candidates, built only when a funnel case fails without them: `bdk-util-you-are-here` (Chaos: the vendor, analyst, and CFO pins argued down to one) and `bdk-util-cost-paradox` (Crapola → Viable: two-sided unit economics at scale).

## Quick checks (the keynote stage demos)

Outside the funnel. Their names are frozen because the keynote quotes them.

| Skill | Family | Invoke when | Produces |
|---|---|---|---|
| [`bdk-value-or-theater`](../skills/bdk-value-or-theater/SKILL.md) | Claims, in one breath | A one-minute verdict on a pitch, roadmap item, or hot take | Five questions, VALUE → PURSUE / THEATER → PUNT / NOT YET → PIVOT |
| [`bdk-skill-sorter`](../skills/bdk-skill-sorter/SKILL.md) | Work | A role, a calendar, a backlog, or a team's rituals | The Sort grid: Busywork → PASS-OFF · Beige → PIVOT · Theater → PUNT · Truth → PURSUE, plus Hired · Fired · Promoted and Monday |

## Hand-offs to sibling kits

The kit points to these instead of copying them.

| When the funnel finds… | Hand off to |
|---|---|
| Work, not a claim (a ceremony worth passing off) | AI Product Operating Model Skills → `workflow-to-skill-converter` |
| "The model said so" (no human decision rule) | AI Product Operating Model Skills → `human-aipom-work-contract` |
| An executive's weekend prototype | Product Manager Antagonist Skills → `pant-executive-decision-review`, `pant-meeting-rehearsal` |
| A synthetic persona standing in for customers | AI-Augmented Product Discovery Lab → `dlab-step03-persona`, plus a real interview |
| "Efficiency is our moat" | Market Intelligence Skills → `mi-build-battle-card`; Precedents Thinking |
| Theater to trim | Mitre Skills → `itk-trimming` |
| An agent idea that reaches Truth | ADLC Skills → `adlc-step1-frame-intent` |

Every skill supports Guided Discovery, Context Dump, and Spitballing modes, and the Product Coach, Comedian, Pirate, Boss, and Antagonist voices. See [MODES.md](../MODES.md) and [VOICES.md](../VOICES.md).
