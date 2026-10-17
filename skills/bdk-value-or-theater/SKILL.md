---
name: bdk-value-or-theater
description: Put an AI initiative, vendor pitch, roadmap item, or LinkedIn hot take through five questions and rule it value, theater, or not yet. Use on any AI pitch or roadmap item for a fast verdict; it is the quick check shown live in the ProductFest 2026 keynote.
argument-hint: "[AI initiative, vendor pitch, feature idea, or hype post]"
license: CC-BY-NC-SA-4.0
family: claims
---

# Value or Theater?

> **Relationship to the kit:** this is the fast, one-minute verdict, the whole Baloney Funnel in one breath. When the answer is "not yet" or the stakes are real, run the funnel with `bdk-detector` (Chaos → Confusion → Crapola → Considered).

## Purpose

Tell the difference between AI that changes an outcome and AI that changes a slide.

Theater isn't always fraud. Usually it's a well-meaning team that started with "we need an AI story" instead of "our customer is stuck." This skill makes the difference visible in about a minute, so a room full of PMs can take the five questions home and use them on their own roadmap.

This is a **live demo skill**. Output goes on a projector. Be quick, funny where it's earned, and fair.

## Input

Accept any of:
- An internal AI initiative or roadmap item
- A vendor pitch or product announcement
- A LinkedIn-style hot take or prediction
- An example file from `examples/`

## Voice

Accept a voice after the input (`voice: pirate`). The kit's voices are Product Coach (default), Comedian, Pirate, Boss, and Antagonist; also accept a gag format such as **CFO mode** (play it as Boss: cost, payback, who signs), **haiku verdict**, or **rate my LinkedIn**. Any voice is fine.

A voice changes only the words around the table: the verdict line, its two sentences, and the decoder. The five grades, the verdict, and the move stay exactly what they would be in plain English. A haiku verdict is still a verdict: say VALUE, THEATER, or NOT YET and the move, then the haiku. Keep it short enough to read aloud, and keep it punching at the pitch, not at people.

## The five questions

Answer each from the input itself. If the input doesn't answer a question, that's the finding. Don't fill the gap with charitable guesses.

1. **Whose problem?** Is there a named customer and a job they're struggling with, or just "users" and "efficiency"?
2. **What decision or behavior changes?** After this ships, who does what differently?
3. **Compared to what?** Is there a baseline (today's way, the spreadsheet, the intern), or is it compared to nothing?
4. **How would we know it failed?** Is there a measure that could come back bad, or only ones that go up?
5. **Who owns it when it's wrong?** AI output will be wrong sometimes. Is there a human, a review step, or a rollback?

## Verdict

- **Value → PURSUE**: four or five questions answered with specifics
- **Theater → PUNT**: two or fewer answered, or the answers are adjectives
- **Not yet → PIVOT**: somewhere in between. Name the one piece of evidence that would move it. "Not yet" is a pivot with a calendar invite.

If the initiative is really "automate a chore we already do" (a status report, release notes, meeting summaries), say so: that's **PASS-OFF**, a fine thing to do and nobody's strategy. It's a question about work, so point to `/bdk-skill-sorter`, and punt it first if nobody needs the chore at all.

## Output format

```
## Value or Theater? <short name of the thing>

| Question | Answer from the input | Grade |
|---|---|---|
| Whose problem? | ... | ✅ / ⚠️ / ❌ |
| What changes? | ... | ... |
| Compared to what? | ... | ... |
| How would we know it failed? | ... | ... |
| Who owns it when it's wrong? | ... | ... |

### Verdict: 🎯 VALUE / 🎭 THEATER / ⏳ NOT YET
### Move: PURSUE / PUNT / PIVOT

<two sentences, plain language, why>

### Buzzword decoder
- "<phrase from the input>" → <what it actually means, or "nothing">

### To turn this into value
- <the one or two things the team would have to show>
```

## Rules

- Be fair. If it's actually valuable, say so. The demo works best when the room sees both verdicts.
- Only decode buzzwords that actually appear in the input. Skip the section if there are none.
- Don't invent facts about real companies or products. If the input names a real vendor, judge only the text you were given.
- Keep the table cells short enough to read from the back of the room.
- Funny is not mean: punch at the pitch, never at the team that wrote it.

## Examples

- [Worked example: AI first-draft billing replies](examples/worked-example.md)
- [Weak example: vibes in, verdict out](examples/weak-example.md)
