---
name: bdk-skill-sorter
description: Sort a product role's work onto the Sort grid (busywork, beige, theater, truth), give every item its move (pass-off, pivot, punt, pursue), then say what it means for getting hired, fired, and promoted, and what to do Monday. Use with a job description, a role, a calendar, or a list of what someone does all week; it was demoed live in the ProductFest 2026 keynote.
argument-hint: "[job description, role title, calendar, backlog, or 'what I did this week' list]"
license: CC-BY-NC-SA-4.0
family: work
---

# The Skill Sorter

> **Relationship to the kit:** the sorter judges *work* (busywork, beige, theater, truth); the Baloney Funnel judges *claims and ideas*. Sort your work, then check your claims. Use the sorter on a role, and `bdk-detector` on whatever that role is being asked to build.

## Purpose

Answer the question under every job title: **which of my skills just went worthless, and which just became my leverage?** Truth is your leverage.

AI isn't coming for the people who know what problem is worth solving. It's coming for the busywork, the beige, and the theater. This skill sorts a real role's work onto a 2×2, out loud, in a way a room can argue with, and gives every item a move.

This is a **live demo skill**. The output goes on a projector, in front of product people, and has to land in under a minute of reading.

## Input

Accept any of:
- A pasted job description
- A role title plus seniority ("Senior PM, B2B SaaS")
- A list of what someone actually did last week, a calendar, a backlog, or a team's rituals
- An example file from `examples/`

If you only get a role title, infer 8–12 typical activities, and **say you inferred them**.

## The Sort grid

Two questions sort anything. **Could anyone (or any AI) do it?** And **does it move an outcome?**

| | **Anyone could do it** | **Only you could do it** |
|---|---|---|
| **Moves an outcome** | 🥱 **BEIGE → PIVOT**: add judgment until it's yours | 🎯 **TRUTH → PURSUE**: do more of this |
| **Moves nothing** | 🗑️ **BUSYWORK → PASS-OFF**: hand it to the robot | 🎭 **THEATER → PUNT**: cancel the show |

Each square has a gut-check question. Use these exact words:

| Square | The question | The probe | Move |
|---|---|---|---|
| **Busywork** | "Would anyone notice if the robot did this?" | Is it needed, and does it need *me*, or just my hours? | **PASS-OFF** |
| **Beige** | "Would anyone know this was mine?" | If your name came off it, could anyone (or any AI) have made it just as well? | **PIVOT** |
| **Theater** | "Who's this for, the customer or the audience?" | If nobody were watching, would we still do it? | **PUNT** |
| **Truth** | "What do we know that the model can't?" | And is it real enough to change what we do next? | **PURSUE** |

**Truth** is judgment, customer knowledge, craft, influence, and taste: knowing something about *these* customers, *this* context, or *these* people that isn't written down. AI makes the person who has it faster, so it's worth more. (Earlier versions of the talk called this square **Leverage**. Same square.)

An item can move between squares depending on how it's done. "Writing a PRD" is beige when it's a template fill and truth when it captures a hard tradeoff nobody else saw. Call that out when it happens. It is the most important teaching moment in the demo.

## Steps

1. Pull out the activities and skills from the input. Use the person's own words.
2. Put each one in a square by asking the two questions, with a one-line reason. No hedging, no "it depends" without saying *what* it depends on.
3. Flag 1–3 **swing items** that could land in either beige or truth depending on how they're done.
4. Translate the sort into career consequences.
5. End with Monday: one move for each of the four risks.

## Output format

Keep it tight. It has to be readable from row 15.

```
## Sorting: <role>

### The grid
|  | Anyone could do it | Only you could do it |
|---|---|---|
| **Moves an outcome** | 🥱 BEIGE → PIVOT (<n>) | 🎯 TRUTH → PURSUE (<n>) |
| **Moves nothing** | 🗑️ BUSYWORK → PASS-OFF (<n>) | 🎭 THEATER → PUNT (<n>) |

### 🗑️ Busywork → PASS-OFF  (hand it to the robot)
- <item>: <why>

### 🥱 Beige → PIVOT  (add judgment until it's yours)
- <item>: <why>

### 🎭 Theater → PUNT  (cancel the show)
- <item>: <why>

### 🎯 Truth → PURSUE  (do more of this)
- <item>: <why>

### ⚖️ Swing items
- <item>: beige when <X>, truth when <Y>

### Hired · Fired · Promoted
- **Hired for:** your Truth square: <what a hiring manager will screen for now>
- **Fired for:** the theater you keep performing: <what becomes indefensible>
- **Promoted for:** what you pass off: <the hours you free, and what you spend them on>

### Monday
- **Pass it off (Feasible):** <one ceremony to automate this week>
- **Call one customer (Valuable):** <who, and what to ask>
- **Watch one person use it, and shut up (Usable):** <what to watch>
- **Say the hard "why not" (Viable):** <the question everyone is avoiding>
```

## Rules

- Be blunt and specific. The talk's promise is "less doom, fewer buzzwords, more clarity."
- Don't use the buzzwords the talk mocks ("10x," "game-changer," "unlock," "supercharge," "AI-native") unless you're mocking them.
- Don't predict job loss percentages or invent statistics. This is a sorting exercise, not a forecast.
- **Truth should never be empty.** If the input has no truth items, say so plainly and name what's missing. That's the punchline.
- Theater should rarely be empty either. Every role has some.
- Punt the theater before you pass it off: automating a ritual nobody needs is still theater, just faster.
- Pass-off is a move for work. It is not a verdict on a claim; claims go through `bdk-detector`.
- Funny is not mean. The rituals are the target, never the people stuck performing them.

## Examples

- [Worked example: Senior PM, Platform](examples/worked-example.md)
- [Weak example: everything is leverage](examples/weak-example.md)
