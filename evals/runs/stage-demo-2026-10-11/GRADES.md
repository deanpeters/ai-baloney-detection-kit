# Grades: deck 9 stage demo, 2026-10-11

The live demo in deck 9 is `/bdk-detector @examples/launch-week.md`. The slides show **10 → 6 → 2 → 1**, ending with #9 PIVOT and #10 PURSUE, and the output must read on a projector in under a minute. All runs: OpenAI `gpt-5.5` via `codex exec`, read-only, skill folder without examples, fixture without its answer key. Graded by the authoring assistant (not blind, not human) against [case 10](../../loop-cases/loop-10-launch-week.yaml).

| Runs | Fixture / skill | Output size | Counts | Ending (#9 / #10) | Notes |
|---|---|---|---|---|---|
| [D1](D1.md), [D2](D2.md) | Original fixture; detector printed full report | 1,600–2,100 words | 10 → 5 → 2 → 1 (both) | #9 held for a test | Too long for the stage; #5 sifted at Chaos, #8 at Confusion |
| [E1](E1.md)–[E3](E3.md) | Claims 2, 5, 9 sharpened; stage card added | 178–197 words | E2, E3 exact; E1 10 → 5 → 3 → 1 (#7 at Chaos) | Pivot / Pursue, all three | |
| [E4](E4.md)–[E6](E6.md) | #7 given a case-study receipt | 190–203 words | none exact; two runs double-listed a claim | Pivot / Pursue | The receipt invited a "narrow it" pivot, and Pivot counting was ambiguous |
| [E7](E7.md)–[E9](E9.md) | **Final:** #7 has real shipping features; skill states the counting rule | 180–201 words | **E7, E9 exact**; E8 10 → 6 → 3 → 1 (#7 one tier late), counts consistent | **Pivot / Pursue, all three** | Shipping configuration |

**Result for the shipping configuration:** stage card every time; exact slide counts in 2 of 3 runs; the scripted ending in 3 of 3. The deck's demo notes now carry a recovery line for an off-by-one count.

Voice checks for the wheel segment: [haiku](value-or-theater-haiku.md) and [CFO mode](value-or-theater-cfo.md) both return THEATER → PUNT with identical grades; only the words around the table change. **Pass.**
