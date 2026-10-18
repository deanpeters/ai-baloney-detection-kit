# CLAUDE.md

Claude Code reads this file automatically. The contract for every AI collaborator is in AGENTS.md:

@AGENTS.md

Read README.md (context) and CONSTITUTION.md (the non-negotiables) before changing anything.

## What this repo is

**AI Baloney Detection Kit (AI-BDK):** Dean Peters' open toolkit for walking an AI claim, idea or product from Peak Baloney to Safe to Serve. It's also the takeaway from his ProductFest 2026 closing keynote, "Getting Past the AI Chaos, Confusion, and Crapola" (Richmond, VA, Oct 22, 2026). The close slide's "Install the BDK" QR points here once the repo is published. The joke: "It's like an SDK, except it removes features. Mostly the fake ones."

The keynote lives in `~/Code/chaos-confusion-and-crapola`. **Its decks quote this repo, so changing a name here breaks a slide there.** Start with that repo's `slides/HANDOFF.md`.

## Names and vocabulary (don't drift)

- **Repo and skills:** the repo is `ai-baloney-detection-kit`, short "AI-BDK." Every skill uses the `bdk-` prefix.
- **Spelling:** US "baloney." Use "bologna" only for lunch-meat visuals.
- **The five checks** (= the Contract): Show Me the Receipts · Label the Lunch Meat · Check the Context Pantry · Check the Sell-By Date · Taste Before You Ship.
- **The Baloney Scale** is a rating: Real Deal · Mostly Meat · Real Imitation Baloney · Mystery Meat · Total Crapola.
- **The AI Hype Baloney Curve** is the path a claim travels:
  - axes: hype/claims against evidence/validation
  - landmarks: Peak Baloney → Safe to Serve
  - stops: Fresh From the Grinder · **Unlabeled Meat** (not "Mystery Meat," which is a Scale level) · Context-Free Cold Cuts · Past the Sell-By Date · Taste-Tested
- **Real Deal on the Scale = Safe to Serve on the Curve.**
- **The Baloney Funnel** is how the kit runs: seven steps in four tiers, a process of elimination, outcome first, then cheapest sift (Dean, 2026-10-18; the tier labels may be renamed later, the steps are what matter).
  - steps: 1 `bdk-outcomes` → 2 `bdk-receipts` → 3 `bdk-labels` → 4 `bdk-sell-by` → 5 `bdk-relevance` → 6 `bdk-taste-test` → 7 `bdk-pivot-punt-pursue`
  - tiers: **Chaos** (Outcomes + Receipts: "Is it a real outcome, with real receipts?") → **Confusion** (Labels + Sell-By + Relevance: "What do we actually know, is it still fresh, and does it apply to us?") → **Crapola** (Taste Before You Ship: "Would reality disagree?") → **Considered** (Pivot, Punt, or Pursue: "Pursue, pivot, or punt, and why?") → **Truth**
  - outcome statement: [direction] [metric] [by how much] [by when] for [beneficiary persona] in [problem context]. Outputs ("an AI interface") and vanity metrics ("feel 50% more confident") are sifted out at step 1. Optional guardrail: "without [a health metric] crossing [a limit]."
  - step 6 writes a **solution hypothesis**: If we / for / then we will [the outcome] · at least two tiny acts of discovery tagged by square · valid if within [timeframe] we observe a quantitative measure, a qualitative measure, and a hard stop.
  - sourcing (Dean, 2026-10-18): research public facts yourself (ask only for private ones; never browse a fictional fixture), bottom-up over top-down, a clickable URL for every major data point from credible source classes, ranges with reasons.
  - Productside's four-risk metrics and solution-hypothesis PDFs are licensed for internal use only: borrow the ideas, never the wording.
  - exits: Pass · Sifted out · Send back · Pivot. Missing is not failed; stale is not false.
  - the Curve is one claim's journey; the Funnel is how many claims get sorted. Truth on the Funnel = Safe to Serve on the Curve.
- **The four risks** (Considered), Dean's questions verbatim, on a 2×2 of Should we? / Can we? × For them / For us: **Valuable** "Is this something someone would buy?" · **Usable** "Will users trust and adopt it?" · **Viable** "Is this good business?" (Is there ROI for both sides?) · **Feasible** "Can we even do this with what we know and have?" Stage shorthand: "Would they buy it? Would they trust it? Would it pay, both sides? Can we do it with what we've got?" (never "Can we build it?"). What each means (Dean, 2026-10-18): Valuable = they'd take money out of their wallets and put it into ours, not just like it · Usable = ensures and expands adoption, removes obstacles, creates advocates · Viable = a good business model for us (SaaS is; add generative or agentic AI and you can go broke adding users) · Feasible = the people, process, culture, and capital
- **Decisions:** Pursue / Pivot / Punt for claims. Pursue = so much proof we go forward as planned · Pivot = adjust based on the data and discoveries · Punt = the orange is not worth the squeeze, say no. **Pass-off** is a fourth move for *work* only (the Sort grid), never a verdict on a claim.
- **Two families:** *Your work* (the Sort grid: Busywork → Pass-off · Beige → Pivot · Theater → Punt · **Truth** → Pursue; "Truth is your leverage," formerly "Leverage". **Open drift:** deck 11's slide 38 is back to **Leverage**; Dean to pick one, see docs/HANDOFF.md) and *claims and ideas* (the Funnel). Bridge line: "Sort your work, then check your claims."
- **Three lenses:** You · Your People · Your Market (deck 9's three acts; an optional tag, not a framework).
- **Modes:** Guided Discovery · Context Dump · Spitballing.
- **Voices:** Product Coach (default) · Comedian · Pirate · Boss · Antagonist.
- **The chain:** Chaos → Confusion → Crapola. In deck 11 each C is a **missing question**: Chaos "What are the unknown unknowns?" · Confusion "What decision is this actually for?" · Crapola "Yes, we can. But should we?" The funnel slides pair each tier's two skills with that question. Earlier decks answered with Context → Contract → Constitution.
- **The keynote's throughline:** AI is an answer machine; a PM is a question machine. On stage it's always **better questions, better decisions**. In skill text, "judgment" is fine wherever asking the right questions and making the right decisions doesn't fit (Dean, 2026-10-15).
- **The PM Code** is the stage name for three short forms of the Constitution (I "Is the ORANGE worth the squeeze?", never "juice" · II AI proposes, humans decide · III no receipts, no roadmap); the mapping is at the end of CONSTITUTION.md. Deck 11 calls it **the 7 Arrrguments** and shows two: "AI proposes. The crew decides." and "Ship slop? Get marooned." The rest point to Dean's Substack article "AI Orchestrator or Pirate Captain?"
- **Never** use Gartner Hype Cycle art or the "Gartner" name in assets. The curve is ours.

## Who builds what

- **What the keynote runs from this repo (deck 11, 2026-10-15):**
  - **Live:** `/bdk-receipts @examples/deck-fatigue-index.md` (ready 2026-10-15: the example is mirrored from the keynote's `demos/fixtures/`, and `bdk-receipts` prints a stage card by default; see `evals/runs/stage-demo-2026-10-15/`).
  - **Optional, hidden:** `/bdk-value-or-theater @examples/pitch-theater.md`.
  - **On slides only:** the six funnel commands.
  - `bdk-value-or-theater` and `bdk-skill-sorter` were ported from earlier decks' live demos.
  - Keep every stage skill's output projector-readable.
- **Skills live in `skills/`** (the sibling-repo layout); `.claude/skills` is a symlink to it so the keynote's `/bdk-…` commands work from this folder. Plugin manifests are in `.claude-plugin/` and `.codex-plugin/`. The catalog is `catalog/INDEX.md`; the authoring rules are `docs/SKILL-SPEC.md`.
- **Funnel skills:** `bdk-detector` (whole funnel); the seven steps above; and two deep dives, `bdk-context-pantry` (beside Relevance) and `bdk-four-risks` (beside Pivot-Punt-Pursue). **Don't let the slide decks decide the library's design** (Dean, 2026-10-18): the library is judged by whether it works; Dean updates the decks. **Utility:** `bdk-util-slice-the-pitch` (max six utilities). Read `docs/HANDOFF.md` for maintenance and `evals/VERIFICATION.md` for actual evidence. Shared behavior is authored in `reference/assessment-contract.md`; bundled copies are generated, not edited independently.
- **What changed on 2026-10-11 and why** is in `docs/UPDATE-LOG.md`; open questions for Dean are at the end of it.
- **`examples/` holds fictional inputs only,** never a real company or person. They mirror the keynote's `demos/fixtures/`, so edit them there first, then copy over.
- **`assets/`** holds the curve images (pins and stops) and the cost-paradox chart. They're exported from the keynote decks (rendered slides), so regenerate them there.

## House rules

- **License:** CC BY-NC-SA 4.0, the same as Product Manager Skills and Product Manager Antagonist Skills. One license for everything.
- **Funny ≠ mean:** punch up at hype, vendors and weak logic, never at users, customers, affected workers or people learning.
- **Don't explain the joke.**
- **Public since 2026-10-17** at https://github.com/deanpeters/ai-baloney-detection-kit (branch `main`). Raw `transcript.jsonl` session dumps are gitignored; keep links repo-relative, never `/Users/...`. Ask before pushing.
