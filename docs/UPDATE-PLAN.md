# AI-BDK update plan: the Baloney Funnel

Revision 2, 2026-10-11. **Built on 2026-10-11** with Dean's open decisions resolved by recommendation; see [UPDATE-LOG.md](UPDATE-LOG.md) for what was done, what differs from this plan, and how to reverse each decision. It merges three sources:

- This repo's design session: follow the sibling skill repos, use utilities, and add the four risks.
- The keynote's deck 9 sync plan and deck 9 (`notes/bdk-update-plan.md` and `outline/deck-9-the-grid.md` in the keynote repository).
- Dean's new presentation outline (2026-10-11), which turns the loop into a **funnel**: Chaos → Confusion → Crapola → Considered → Truth.

**Ownership:** the BDK work lives here, and the keynote session owns the decks. Where this plan and the keynote note disagree, this plan wins for the BDK. The test cases are in [evals/loop-cases/](../evals/loop-cases/README.md).

**Revision 2 changes** from the six-step loop of revision 1:
- Four tiers instead of six steps.
- Claims can drop out at any tier.
- Many claims go in, not one.
- The skills keep their check names.
- The Considered tier gets its own skill.

---

## 1. What's decided

| Decision | Source |
|---|---|
| Follow the layout of the sibling skill repos (ADLC, Precedents, Market Intelligence, Discovery Lab) | Dean, 2026-10-11 |
| Baloney detection is a repeatable process with utilities, not one monolithic skill | Dean, 2026-10-11 |
| **The process is a funnel, a process of elimination by tiers:** Chaos (widest, sifted first) → Confusion → Crapola → Considered → **Truth** | Dean's presentation outline, 2026-10-11 |
| **Four risks**, each with Dean's exact question (§4) | Dean, 2026-10-11 |
| The four risks sit on a 2×2: **Should we? / Can we?** × **For them / For us** | Deck 9, Monday grid |
| The Sort grid is Busywork · Beige · Theater · **Truth**. "Truth is your leverage." | Deck 9 |
| The four moves for **work** are Pass-off · Punt · Pivot · Pursue | Deck 9 |

## 2. Two families

The kit judges two different things. The bridge line: **"Sort your work, then check your claims."**

| Family | Judges | Tools | Moves |
|---|---|---|---|
| **Your work** | What you spend your week on | The Sort grid (`bdk-skill-sorter`), Monday | Pass-off · Punt · Pivot · Pursue |
| **Claims and ideas** | What you're being sold or asked to build | **The funnel**, the five checks, the four risks, the Scale | Pursue · Pivot · Punt *(D4)* |

**Truth is the word that joins them.** It's the Sort grid's fourth square, and it's what comes out of the bottom of the funnel.

**Three lenses: You · Your People · Your Market.** These are the three acts of deck 9, used as an optional tag. They are not a new framework. Dean's new outline doesn't show the Sort grid or the sorter demo *(D5)*.

## 3. The Baloney Funnel

Pour in every AI claim, pitch or roadmap idea. Each tier asks one question and sifts out what fails it. **The cheapest sifts run first,** so nobody spends a week on a taste test for something whose only source is a press release.

```text
  CHAOS        Is it real, and is it still true?           Show Me the Receipts · Check the Sell-By Date
    CONFUSION    What do we actually know, and does it       Label the Lunch Meat · Check the Context Pantry
                 apply to us?
      CRAPOLA      Would reality disagree?                    Taste Before You Ship (the four risks)
        CONSIDERED   Pursue, pivot or punt?                   The four-risk grid
          TRUTH        What survived, scoped to the bet it earned
```

| Tier | Question | Checks | Sifts out | Typical cost |
|---|---|---|---|---|
| **1. Chaos** | Is it real, and is it still true? | Receipts, Sell-By *(D1)* | No traceable origin. Five articles echoing one press release. A slogan with no claim in it. A benchmark on a retired model. | Minutes |
| **2. Confusion** | What do we actually know, and does it apply to us? | Labels, Context Pantry | Assumptions dressed as facts. "40%" for nobody in particular. No named user, outcome or owner. | An hour or two |
| **3. Crapola** | Would reality disagree? | Taste Before You Ship | Buildable, but nobody would buy it, trust it or profit from it | Days to a week |
| **4. Considered** | Pursue, pivot or punt? | The four-risk grid (§4) | Bets bigger than the evidence earned | A decision meeting |
| **Truth** | — | — | — | — |

**How a claim leaves a tier.** Missing evidence is not failed evidence. Every exit says which of the four it is:

| Exit | Meaning | Where it goes |
|---|---|---|
| **Pass** | It survived this tier's question | Down to the next tier |
| **Sifted out (Punt)** | It failed the question | Out, with the reason recorded |
| **Send back** | Evidence is missing or stale, not failed | Back to the top: go get receipts, or refresh |
| **Pivot** | Change one thing and try again | Back in at the tier where it failed |

**The return chute makes it a loop.** Pivots drop back in at the tier where they failed. Truth has a sell-by date too: when a re-check date expires (a new model version, a price change, a new policy), the claim goes back into the top of the funnel. There are no silent restarts.

**One claim or many.** A single claim is a funnel of one. A roadmap or a pile of vendor pitches is the real use, and the **funnel report** shows how many entered and left each tier, and why each one left.

**`bdk-detector` runs the whole funnel** in one command for Context Dump and unattended use. It produces the funnel report and points to the tier skill for each finding.

## 4. The four risks (the Crapola and Considered tiers)

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **Valuable:** "Is this something someone would buy?" | **Viable:** "Is this good business?" (Is there ROI for both sides?) |
| **Can we?** | **Usable:** "Will users trust and adopt it?" | **Feasible:** "Can we even do this with what we know and have?" |

- Keep these questions word for word everywhere. The Monday grid on stage uses the same ones.
- **"Buy"** includes *choose*. For internal tools, ask whether someone would pick it over what they do now. This note goes in the skill text only.
- The Chaos and Confusion tiers already sort evidence into the four squares, labeled **earned / weak / missing / stale**. The Crapola tier tests only the riskiest open squares. Considered reads the grid.
- **The feasible-only flag:** raise it when the only evidence is a working demo. "AI made *building* cheap. The demo proves buildable, not feasible."

**Reading the grid in Considered:**

| Grid state | Move |
|---|---|
| All four squares earned for *this size of bet* | **Pursue** the named investment, which may be a pilot, not a rollout. This is **Truth.** |
| A **Can we?** square fails and the others hold | **Pivot** the how (workflow, review burden, scope, or what we lack), then back in at Crapola |
| **Viable** fails and Valuable holds | **Pivot** the price, scope or cost, for whichever side's ROI fails |
| **Valuable** fails, or no cheap test could move the riskiest square | **Punt** |
| A square is **missing or stale** rather than failed | **Send back** to the top |

There is never a single averaged score. Show which tier and which square the baloney was caught in.

## 5. Skills

**Skills keep their check names.** You demo two or three on stage at a time, and `/bdk-receipts` reads on a projector where `/bdk-step1-show-me-the-receipts` doesn't. The tier goes in the frontmatter (`tier: 1-chaos`) and orders the catalog. This departs from the Precedents step numbering on purpose: the stage beats sort order.

| Tier | Skill | Status | Produces |
|---|---|---|---|
| — | `bdk-detector` | Rework | The funnel report: one or many claims, run through every tier |
| 1 Chaos | `bdk-receipts` | Rework | Receipts Ledger: origin, independence, support |
| 1 Chaos | `bdk-sell-by` | Rework | Freshness Ledger, **with a re-check date for each piece of evidence** |
| 2 Confusion | `bdk-labels` | Rework | Labeled Claims: fact / inference / assumption / best guess |
| 2 Confusion | `bdk-context-pantry` | Rework | Context Inventory: for whom, compared with what, the gaps and contradictions |
| 3 Crapola | `bdk-taste-test` | Rework, adding **Usable** | The cheapest tests for the open squares, thresholds written first, or a review of results |
| 4 Considered | `bdk-four-risks` *(D7)* | **New** | The four-risk grid, a Scale rating for each square, and a decision record: move, owner, by-when, what would change the call, where it goes next |

"Rework" means each skill adds:
- its tier
- its sift question
- the four exits
- a human gate
- the four-risk squares it informs
- a `template.md` and `examples/`

**On stage, two or three skills at a time:**
- Chaos: `/bdk-receipts` + `/bdk-sell-by`
- Confusion: `/bdk-labels` + `/bdk-context-pantry`
- Crapola → Considered: `/bdk-taste-test` + `/bdk-four-risks`

## 6. Utilities

They follow the Precedents rule. A utility hands an artifact to a named tier or takes one from it. It never continues into the funnel. There are **at most six.**

| Utility | Supplements | Status | Produces |
|---|---|---|---|
| `bdk-util-slice-the-pitch` | Into Chaos | **Build first** | The real claims pulled out of a deck, demo, roadmap or vendor page, ready to pour in. The funnel needs claims, not documents. |
| `bdk-util-you-are-here` | Chaos | Candidate | The vendor, analyst and CFO pins, argued down to one |
| `bdk-util-cost-paradox` | Crapola → Viable | Candidate | Two-sided unit economics at scale: their ROI and ours |

The four-risks canvas from revision 1 becomes the main skill `bdk-four-risks`.

**Not utilities:**
- **The decision record and four moves** are shared text in `reference/assessment-contract.md`.
- **The Sort grid** stays inside `bdk-skill-sorter`.

**Parked:** `bdk-evidence-table-builder`, `bdk-assumption-register`, `bdk-experiment-designer`, `bdk-confidence-scorer`.

## 7. Quick checks

They sit outside the funnel. Their names stay exactly as they are because the keynote quotes them 83 times *(D2)*.

**`bdk-skill-sorter`** (the work family). If the sorter stays in the talk, it has to be updated before the first rehearsal *(D5)*.
- Bins: Busywork · Beige · Theater · **Truth**, each with its question and move:
  - Busywork: "Would anyone notice if the robot did this?" → PASS-OFF
  - Beige: "Would anyone know this was mine?" → PIVOT
  - Theater: "Who's this for, the customer or the audience?" → PUNT
  - Truth: "What do we know that the model can't?" → PURSUE
- A 2×2 that reads on a projector, plus swing items.
- Hired · Fired · Promoted on the grid.
- Monday uses the four-risk moves.
- "Truth should never be empty."

**`bdk-value-or-theater`** (claims triage): the funnel in one breath. Keep value / theater / not yet, and add the move under each: PURSUE / PUNT / PIVOT. Name PASS-OFF when the initiative is really just automating busywork.

**`bdk-monday`:** only if the sorter stays and its output gets too long *(D5)*.

## 8. Layout (matches the sibling repos)

```text
skills/<name>/SKILL.md, template.md, examples/{worked-example,weak-example}.md, references/ (generated contract)
catalog/INDEX.md                      # funnel tiers, then "Supporting utilities: these are not tiers", then quick checks
docs/SKILL-SPEC.md                    # naming, the tier field, frontmatter, required sections, the utility rule
.claude-plugin/plugin.json + marketplace.json   # "skills": "./skills/", CC-BY-NC-SA-4.0
.codex-plugin/plugin.json
evals/loop-cases/                     # funnel cases, with expected exits written down first
```

**Stage commands:** keep `.claude/skills` as a symlink to `../skills`, so `/bdk-receipts` and the rest work when the repo is open on stage, and also ship the plugin (which installs as `/bdk:bdk-…`). Test this on the stage laptop *(D2)*. Since the skills keep their names, nothing on stage gets renamed.

## 9. Hand-offs to the sibling repos

All the paths below were checked on 2026-10-11.

| When the funnel finds… | Hand off to |
|---|---|
| Work, not a claim (a ceremony worth passing off) | `ai-product-operating-model-skills` → `workflow-to-skill-converter` |
| "The model said so" (no human decision rule) | `ai-product-operating-model-skills` → `human-aipom-work-contract` |
| An exec's Saturday prototype | `product-manager-antagonist-skills` → `pant-executive-decision-review`, `pant-meeting-rehearsal` |
| A synthetic persona standing in for customers | `AI-Augmented-Product-Discovery-Lab` → `dlab-step03-persona`, plus a real interview |
| "Efficiency is our moat" | `Productside-Market-Intelligence-Skills` → `mi-build-battle-card`; `Productside-Precedents-Thinking` |
| Theater to trim | `Mitre-Skills` → `itk-trimming` |
| An agent idea that reaches Truth | `Productside-ADLC-Skills` → `adlc-step1-frame-intent` |

## 10. Files to change

- **Vocabulary** (CLAUDE.md, README, SKILLS):
  - the funnel and its tiers, Considered, Truth
  - the Sort grid and pass-off for work
  - the four risks, three lenses
  - the PM Code name *(D8)*
- **Chaos / Confusion / Crapola definitions:** README lines 9–13 define them as damage *("what mess does this create")*. The funnel uses them as tiers *("what does this tier sift out")*. Rewrite them to match the wording on the three definition panels *(D9)*. The chain line ("capability gets cheaper faster than organizations can absorb it…") still works as the reason the funnel's top is so wide.
- **Places that list three risks and need Usable added:**
  - `CONSTITUTION.md` Article VI
  - README check 5
  - `BALONEY-SCALE.md`
  - `BALONEY-CURVE.md` stop 5
  - `AGENTS.md` §9
  - `SKILLS.md`
  - the shared contract
  - `bdk-taste-test`, `bdk-detector`
- **Places that say "Leverage":**
  - `bdk-skill-sorter`, 9 places
  - README line 287
  - SKILLS line 127
- **`BALONEY-CURVE.md`:** the funnel and the curve need a stated relationship *(D3)*.
- **Scripts:** `check-library.py` and `build-distribution.py` need the new paths, the tier field check, and a check for the six-utility ceiling.
- **Docs:** `docs/HANDOFF.md`, `BUILD-DECISIONS.md`, `INSTRUCTIONS.md`, `evals/VERIFICATION.md`.
- **The keynote repo:** this session doesn't edit it.
  - Its `slides/HANDOFF.md` line 71 is stale.
  - Its `notes/bdk-update-plan.md` should point here.

## 11. Order of work

0. **Stage fixes,** if the sorter stays in the talk: `bdk-skill-sorter` and `bdk-value-or-theater`.
1. **Spec and catalog:** `docs/SKILL-SPEC.md` and `catalog/INDEX.md`, organized by tier. Dean reviews before any files move.
2. **Layout:** move to `skills/`, add the symlink and the plugin manifests, update the scripts, and confirm the structural check passes.
3. **The funnel:**
   - rework the five check skills by tier
   - build `bdk-four-risks`
   - rework `bdk-detector` to produce the funnel report
   - add the four risks, the exits and the decision record to the shared contract
4. **Utilities:** `bdk-util-slice-the-pitch`, then candidates only as the cases show a need.
5. **Evals:** run [the funnel cases](../evals/loop-cases/README.md) with fresh context, keep the runs, and update VERIFICATION.md.
6. **Docs and dist:** README, SKILLS, CLAUDE.md, INSTRUCTIONS, HANDOFF, then rebuild the ZIPs.

**Not in scope:** `git init`, publishing, installing anything on Dean's machine, and editing the keynote repo.

## 12. Open decisions for Dean

| # | Question | Recommendation (used in this draft) |
|---|---|---|
| D1 | Where Sell-By sits | **Chaos**, because a date check is cheap and should run first. Alternative: keep the curve's order (Chaos: Receipts; Confusion: Labels, Context; Crapola: Sell-By, Taste), since spoiled meat is crapola. |
| D2 | Stage commands after the move to `skills/` | Keep the names, add the `.claude/skills` symlink, and also ship the plugin |
| D3 | The curve and the funnel | The curve is one claim's journey; the funnel is how many claims get sorted. Keep both, or retire the curve if the talk drops it. |
| D4 | What PASS-OFF means for a claim | It doesn't apply. Claims keep three moves; work gets four. |
| D5 | Is the Sort grid / sorter in the new talk? | Keep it in the kit either way. If it's in the talk, it's the first job before rehearsal. |
| D6 | Decks 1–8 still say "leverage" | Add a compatibility note only if those decks stay alive |
| D7 | Name of the Considered skill | `bdk-four-risks` (it reads on a projector). Alternatives: `bdk-considered`, `bdk-pursue-pivot-punt`. |
| D8 | "PM Code" on stage vs "Constitution" in the repo | Keep the file as `CONSTITUTION.md` and add "the PM Code" as its stage name, or rename it everywhere |
| D9 | Wording of the chaos, confusion and crapola definitions | Take it from the three definition panels once they're written |
| D10 | Which candidate utilities to build | `slice-the-pitch` first. Add others when a funnel case fails without them. |
