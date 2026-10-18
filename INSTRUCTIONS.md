# INSTRUCTIONS.md

## Start here

Got an AI idea, claim, product concept, pitch, workflow, agent, feature, or “holy crap this changes everything” moment?

Good.

Let's see whether you've got lunch or fertilizer.

## Use the Skills

**Claude Code, from this folder:** open this repository as your working folder. The skills live in `skills/` (`.claude/skills` points there, so commands are discovered). Invoke `/bdk-detector` for the whole funnel, or choose a step skill from [the catalog](catalog/INDEX.md). Start with `/bdk-outcomes` if you only want to know whether a pitch has a real outcome. Attach a file using your assistant's file picker, or paste the material after the command. If the command is not discovered, ask the assistant to read `skills/bdk-detector/SKILL.md` and its linked assessment contract directly.

**Claude Code or Codex, as a plugin:** this folder is a plugin (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, both pointing at `skills/`). Installed that way, commands carry the plugin name: `/bdk:bdk-detector`. Plugin installation has not been verified in this build; see [verification](evals/VERIFICATION.md).

**Other assistants:** provide the relevant `SKILL.md` and its `references/assessment-contract.md` together. If file access is unavailable, attach those two files or paste their text. Do not provide only the description and expect the complete method.

**Portable ZIPs:** [download all thirteen skills](dist/ai-bdk-skills.zip), or choose an individual ZIP named for its skill in `dist/`. Each contains a skill folder, its template and examples, required references, linked teaching cases, a generated `agents/openai.yaml`, and the license. Extract a folder into the skill location supported by your assistant. For Codex, the personal skill location is `~/.codex/skills/`; preserve existing folders and use a candidate location if a name conflicts. No installation is performed by this repository's build commands. Assistant-specific installation and discovery have not been verified in this build.

Generate or refresh downloads locally with `python3 scripts/build-distribution.py` (Python 3 and PyYAML required). See [the handoff](docs/HANDOFF.md) for maintenance.

### Try a complete assessment

```text
Read skills/bdk-detector/SKILL.md and its linked assessment contract.
DUMP + BOSS: Assess evals/cases/06-bounded-pilot.md.
Use the supplied fictional evidence only. Work unattended on labeled
planning assumptions; leave absent evidence missing. Recommend the next
level of investment and distinguish it from deployment approval.
```

All files in `evals/cases/` are synthetic. Their results teach the method; they are not real customer evidence.

### Sift a whole roadmap

```text
/bdk-detector DUMP: Run every item in evals/loop-cases/loop-09-roadmap-funnel.yaml
(claim and supplied_evidence only) through the funnel. Unattended. Give me the
funnel report: what left at each step, why, and what earned investment.
```

### Start with one check

```text
Read skills/bdk-receipts/SKILL.md and its linked contract.
DUMP: Trace the support for this claim. Use what I supply, distinguish
inspected sources from supplied URLs, and preserve evidence gaps.
```

To work without questions, add: “I cannot respond. Use your best judgment, label planning assumptions, and keep missing records and results missing.” Guided Discovery normally asks progressively; this explicit preference bypasses waiting. It does not authorize purchases, launches, or external actions.

---

# Step 1 — Pick a Mode

## GUIDED

**Walk me through it.**

Best when:

- the idea is fuzzy,
- you are new to the method,
- you are facilitating a workshop,
- or you want the system to teach while it helps.

Start with:

> **GUIDED: Help me run this through the AI Baloney Detection Kit.**

Then describe the idea in a sentence or two.

---

## DUMP

**Here's the mess. Sort it out.**

Best when:

- you already have lots of context,
- you have research, notes, links, metrics, transcripts, documents, or a PRD,
- or you do not want to answer twenty intake questions.

Start with:

> **DUMP: Run the following material through the AI Baloney Detection Kit. Use what is already here before asking me for more.**

Then paste or attach the material.

---

## SPITBALL

**Kick this around with me.**

Best when:

- the idea is early,
- you want intellectual sparring,
- you are exploring alternatives,
- or you want to poke holes without filling out a canvas.

Start with:

> **SPITBALL: Kick this idea around with me using the AI Baloney Detection Kit. Don't formalize it yet.**

Then throw the idea on the table.

---

# Step 2 — Pick a Voice, If You Want One

Default is **Product Coach**.

Optional voices:

- **COMEDIAN** — make the weak logic hurt a little
- **PIRATE** — no treasure without receipts
- **BOSS** — what changes, what costs, what pays off?
- **ANTAGONIST** — argue with the idea before reality does

Example:

> **SPITBALL + ANTAGONIST:** We want to replace quarterly planning with AI agents.

See `VOICES.md`.

---

# Step 3 — Run the Funnel

Seven steps in four tiers, outcome first, then the cheapest checks, as a process of elimination:

1. **Chaos**: *Is it a real outcome, with real receipts?* (1) **Name the Outcome**: [direction] [metric] [by how much] [by when] for [beneficiary] in [context] · (2) **Show Me the Receipts** for that outcome
2. **Confusion**: *What do we actually know, is it still fresh, and does it apply to us?* (3) **Label the Lunch Meat** · (4) **Check the Sell-By Date** · (5) **Check the Context Pantry: Relevance** (direct, adjacent, or analog)
3. **Crapola**: *Would reality disagree?* (6) **Taste Before You Ship**: the tiniest test that returns the most brutal truth
4. **Considered**: *Pursue, pivot, or punt, and why?* (7) **Pivot, Punt, or Pursue**, read from the four risks: **Valuable** "Is this something someone would buy?" · **Usable** "Will users trust and adopt it?" · **Viable** "Is this good business?" · **Feasible** "Can we even do this with what we know and have?"

Each claim leaves a step by **Pass**, **Sifted out**, **Send back** (missing or stale, back to the step that can fetch it), or **Pivot**. **Pursue** means so much proof we go forward as planned; **Pivot** means adjust based on the evidence; **Punt** means the orange is not worth the squeeze. What survives is **Truth**.

---

# Step 4 — Check the Damage

Assess where the idea may create:

### Chaos initiation

What new mess, coordination cost, workflow breakage, governance burden, operational risk, technical dependency, or organizational churn could this create?

### Confusion induction

What becomes harder to understand, explain, measure, own, govern, or decide?

### Crapola instantiation

Where are unsupported claims, stale assumptions, fuzzy metrics, weak evidence, or unvalidated promises being turned into product decisions?

---

# Step 5 — Rate the Baloney

Use the Baloney Scale:

1. **Real Deal** — slice it up, put it on a hoagie, good to go
2. **Mostly Meat** — probably edible, pick out the pimentos
3. **Real Imitation Baloney** — looks real, still junk food
4. **Mystery Meat** — nobody knows exactly what went into this
5. **Total Crapola** — put it in the garden, it's fertilizer now

Do not stop at the overall rating.

Show which check produced which problem.

---

# Step 6 — Decide What Happens Next

A useful assessment should end with one of three moves, scoped to a named investment, read off the four-risk grid:

### PURSUE

Enough evidence exists to move forward to the next sensible level of investment.

### PIVOT

Something may be worth pursuing, but the current problem, audience, approach, assumption, economics, or validation path needs to change.

### PUNT

The idea has not earned further investment right now.

“Not yet” is a valid product decision.

---

# The Shortest Possible Version

If you remember nothing else:

**Chaos → Confusion → Crapola → Considered → Truth**

Start with the outcome: what changes, for whom, by how much? Then ask:

> **Is this the Real Deal, or are we about to put Total Crapola on a roadmap?**
