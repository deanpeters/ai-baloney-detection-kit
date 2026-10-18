# SKILLS.md

# Skill Architecture

The AI Baloney Detection Kit has **funnel skills**, **utility skills**, and two **quick checks** from the keynote.

All skills use the **`bdk-` prefix** (like an SDK, except it removes features, mostly the fake ones) and live in `skills/<skill-name>/SKILL.md`. `.claude/skills` points at the same folder so `/bdk-…` commands work when this repository is your working folder. The [catalog](catalog/INDEX.md) lists them in funnel order; the [skill spec](docs/SKILL-SPEC.md) is the authoring source of truth.

The goal is composability, not a zoo of overlapping prompts.

---

# Funnel Skills

The [Baloney Funnel](README.md#the-baloney-funnel) is a process of elimination: seven steps in four tiers, outcome first, cheapest sift next. Each step skill owns one step's question; `bdk-detector` runs them all.

| Step · Tier | Question | Skill | Job |
|---|---|---|---|
| — | Whole funnel | [bdk-detector](skills/bdk-detector/SKILL.md) | One idea or a pile (a roadmap, vendor pitches) through all seven steps; a funnel report |
| 1 · Chaos | Is there a real, measurable outcome here? | [bdk-outcomes](skills/bdk-outcomes/SKILL.md) | Shape the pitch into an outcome statement, or sift out outputs and vanity metrics |
| 2 · Chaos | What evidence supports that outcome's metric and direction? | [bdk-receipts](skills/bdk-receipts/SKILL.md) | Source support, provenance, independence |
| 3 · Confusion | How much is fact, inference, assumption, or best guess? | [bdk-labels](skills/bdk-labels/SKILL.md) | Labels and the label mix |
| 4 · Confusion | Is it fresh enough for this decision? | [bdk-sell-by](skills/bdk-sell-by/SKILL.md) | Freshness, and re-check triggers so Truth gets sent back when it spoils |
| 5 · Confusion | Does it apply to us: directly, adjacent, or by analog? | [bdk-relevance](skills/bdk-relevance/SKILL.md) | Relevance to our pantry of product, user, business, and market data |
| 6 · Crapola | What's the tiniest test that returns the most brutal truth? | [bdk-taste-test](skills/bdk-taste-test/SKILL.md) | A solution hypothesis (If we / for / then we will) and tiny tests of the riskiest open squares, measures and a hard stop written first |
| 7 · Considered | Pivot, punt, or pursue, and why? | [bdk-pivot-punt-pursue](skills/bdk-pivot-punt-pursue/SKILL.md) | The recommendation, its why, and a scoped decision record |
| Deep dive · Confusion | For whom, which workflow, at what cost to each side? | [bdk-context-pantry](skills/bdk-context-pantry/SKILL.md) | Workflow, ownership, and both sides' economics |
| Deep dive · Considered | Which square decides? | [bdk-four-risks](skills/bdk-four-risks/SKILL.md) | The four-risk grid on its own |

Every claim leaves a step one of four ways: **Pass**, **Sifted out**, **Send back** (missing or stale, back to the step that can fetch it), or **Pivot** (change one thing, re-enter that step).

The four risks, Dean's questions verbatim:

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **Valuable:** "Is this something someone would buy?" | **Viable:** "Is this good business?" (Is there ROI for both sides?) |
| **Can we?** | **Usable:** "Will users trust and adopt it?" | **Feasible:** "Can we even do this with what we know and have?" |

Each funnel skill accepts direct notes or partial context; no upstream artifact is required. Each bundles a generated copy of [the assessment contract](reference/assessment-contract.md), so it works on its own outside this repository.

Use [INSTRUCTIONS.md](INSTRUCTIONS.md) for setup and kickoff messages. [Verification](evals/VERIFICATION.md) distinguishes structural checks from synthetic model tests and human-use evidence.

---

# Quick Checks (the keynote stage demos)

Demoed live in the ProductFest 2026 keynote, "Getting Past the AI Chaos, Confusion, and Crapola." Their names are frozen because the keynote quotes them.

## `bdk-value-or-theater` (claims, in one breath)

The one-minute verdict: five questions (whose problem, what changes, compared to what, how would we know it failed, who owns it when it's wrong) rule a pitch, initiative, or hot take **NOT YET → PIVOT**, **THEATER → PUNT**, or **VALUE → PURSUE**. Escalate to `bdk-detector` when the stakes are real.

## `bdk-skill-sorter` (your work)

Sorts a role's work onto the Sort grid, **Busywork → PASS-OFF · Beige → PIVOT · Theater → PUNT · Truth → PURSUE**, then says what that means for getting hired, fired, and promoted, and what to do Monday. It judges *work*; the funnel judges *claims and ideas*. Sort your work, then check your claims.

Try both on the fictional samples in `examples/`.

---

# Utility Skills

A utility earns its place only if it hands an artifact to a named tier or takes one from one. Utilities never continue into the funnel, `depends-on` stays empty, and **at most six may exist**, so the supporting cast never outnumbers the method.

| Utility | Supplements | Job |
|---|---|---|
| [bdk-util-slice-the-pitch](skills/bdk-util-slice-the-pitch/SKILL.md) | Into Chaos | Turn a deck, release, or roadmap into the atomic claims the funnel can sift |

Candidates, built only when a funnel case fails without them: `bdk-util-you-are-here` (Chaos: argue the vendor, analyst, and CFO pins down to one) and `bdk-util-cost-paradox` (Crapola → Viable: two-sided unit economics at scale).

Parked ideas: `bdk-evidence-table-builder`, `bdk-assumption-register`, `bdk-experiment-designer`, `bdk-confidence-scorer`. Do not create a utility skill merely because a function can be named.

---

# Hand-offs

The kit points to sibling kits instead of copying them. See the [catalog](catalog/INDEX.md#hand-offs-to-sibling-kits).

---

# Plugins and Connectors

The repository ships plugin manifests: `.claude-plugin/plugin.json` (with `marketplace.json`) and `.codex-plugin/plugin.json`, both pointing at `skills/`. Installed through a plugin, commands appear as `/bdk:bdk-…`.

Use connectors where they improve access to deterministic or authoritative information: document stores, email, project systems, analytics, customer research repositories, financial or operational systems, code repositories, CRM, search and research systems.

Rules:

- Do not use a generative answer when the authoritative system can provide the record directly.
- Retrieve first, synthesize second.
- Preserve provenance.
- Respect permissions and privacy.

---

# Skill Shape

See [docs/SKILL-SPEC.md](docs/SKILL-SPEC.md). In short: rich canonical frontmatter (generated into portable form for the ZIPs), twelve required sections with violation signals for each key concept, a `template.md`, and a worked and a weak example per skill. `python3 scripts/check-library.py` enforces the mechanics.

Keep skill documentation pedagogical enough to teach and practical enough to execute.

---

# One Method, Multiple Surfaces

Do not create separate versions of the same skill for:

- different voices,
- different LLM vendors,
- different chat surfaces,
- or every interaction mode.

Prefer:

**Skill = what we are doing**  
**Mode = how we engage**  
**Voice = how we sound**  
**Plugin/connector = where we retrieve or act**

That separation keeps the repo usable instead of turning it into Frankensoft.
