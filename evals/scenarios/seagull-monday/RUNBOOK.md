You are running the AI Baloney Detection Kit's **Seagull Monday** scenario, end to end, and capturing a session Dean Peters can show on stage and scroll through afterward. Work from the repository root.

## The situation

Read `examples/seagull-monday.md` (an SVP's Monday-morning Slack message) and every file in `examples/seagull-monday/roadmapgpt/` (the code he vibe-coded over the weekend). Everything is fictional. Your job is the product person on that team: walk his claims through the Baloney Funnel with the kit's own skills, then write him a reply.

## Rules

- **Use the kit's skills** with the Skill tool, in the order below. Give each skill the fixture paths and what earlier stages found. Save each skill's output, verbatim, to the stage file named below. Keep each skill's own format.
- **The code is evidence.** Read it. Where a claim and the code disagree, the code wins, and say exactly which line.
- **Don't run `app.py`.** It would send customer data to an outside service. Reading it is enough.
- **Never repeat the API key.** Refer to it as "a hard-coded key (redacted)."
- **Don't open anything under `evals/`** (no peeking at expected answers), except `evals/scenarios/seagull-monday/card.css` and `snap.sh`, which you'll need for the cards.
- **Punch at the hype, not the person.** Gordon is senior, enthusiastic, and wrong about the evidence. Stay respectful.
- Session folder: `{{SESSION}}`. Write everything there.

## The loop, with screenshots

After each stage, make **one** stage card, an HTML file that teaches or visualizes that stage's key idea in under five seconds, and screenshot it. Each card starts with `<link rel="stylesheet" href="../../../scenarios/seagull-monday/card.css">` (that path is relative to the `cards/` folder). Use its classes: `eyebrow`, `h1` with `<em>` for the green highlight, `rows`/`row`/`tag`, `cols`/`col`, `pre` with `<mark>`, `grid`/`cell`, `stamp`, and the color classes `ok`, `warn`, `bad`, `q`. Big type, few words, no walls of text. Save cards to `{{SESSION}}/cards/NN-name.html` and snap each with:

`bash evals/scenarios/seagull-monday/snap.sh {{SESSION}}/cards/NN-name.html {{SESSION}}/shots/NN-name.png`

1. **The swoop.** Read the message and the code. Card `01-swoop`: the eyebrow "Seagull Monday · 8:02 AM", and Gordon's seven claims, each in five words or fewer.
2. **Strip the glitter.** `bdk-util-slice-the-pitch` → `02-claims.md`. Card `02-claims`: the testable claims, numbered.
3. **Chaos, step 1: name the outcome.** `bdk-outcomes` → `03-outcomes.md`. Card `03-outcome`: the pitch as he said it, then the outcome statement ([direction] [metric] [by how much] [by when] for [beneficiary] in [context]), or SIFTED OUT if there isn't one.
4. **Chaos, step 2: the code tells on him.** `bdk-receipts` → `04-receipts.md`. Card `04-code`: two columns, "He said" vs. "The code says," with the two or three sharpest contradictions, quoting at most three short code lines each, `<mark>`ed. (Redact the key.)
5. **Confusion, step 3: label the lunch meat.** `bdk-labels` → `05-labels.md`. Card `05-labels`: each claim tagged FACT / INFERENCE / ASSUMPTION / BEST GUESS, and the label mix.
6. **Confusion, step 4: the sell-by date.** `bdk-sell-by` → `06-sell-by.md`. Card `06-sell-by`: each piece of evidence with its date and FRESH / STALE / UNKNOWN.
7. **Confusion, step 5: does it apply to us?** `bdk-relevance` → `07-relevance.md`. Card `07-ranking`: what "AI-powered prioritization" actually ranks first and last in `sample_tickets.csv` (work it out from the code's scoring function by hand), and the question nobody asked.
8. **Crapola, step 6: taste before you ship.** `bdk-taste-test` → `08-taste.md`. Card `08-tests`: the tiniest tests, each with its threshold and cost in days.
9. **Considered, step 7: pursue, pivot, or punt.** `bdk-pivot-punt-pursue` → `09-decision.md`. Card `09-decision`: the 2×2 grid (Valuable, Usable, Viable, Feasible, each with its status) and the recommendation as a `stamp` (PURSUE / PIVOT / PUNT), with the why in one line.
10. **The reply.** Write Gordon's Slack reply → `10-reply.md`: under 120 words, warm, specific, no baloney, with one concrete next step and a role for him. Card `10-reply`: the reply itself.

## Finish

Write `{{SESSION}}/SESSION.md`:
- one line on the scenario;
- a table: stage, skill, exit or finding, screenshot file;
- the decision and why, in three lines;
- "What each screenshot teaches": one line per shot.

Then stop. Don't grade yourself.
