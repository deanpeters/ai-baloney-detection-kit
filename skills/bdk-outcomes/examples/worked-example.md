# Worked Example: The Accountant Copilot

**Synthetic.** Ledgerline, its product, and its people are invented. From [funnel case 13](../../../evals/loop-cases/loop-13-output-to-outcome.yaml).

**Step:** 1 Outcomes · **Tier:** Chaos · **As of:** 2026-10-18 · **Mode:** Context Dump

**Decision asked for:** fund a two-squad, two-quarter build of an "AI close copilot."

## Before and after

**As supplied:** "Build an AI copilot for the close so our accounting customers stop dreading month-end."

**Shaped:** *Reduce* *median days-to-close* *from 6 to 4* *by end of Q2 2027* for *corporate-accounting controllers at mid-market customers* in *the month-end close inside Ledgerline*, *without raising close-module support tickets or cost to serve above $1 per entity per close*.

## Parts check

| Part | Value | Status | Label / basis |
|---|---|---|---|
| Direction | Reduce | inserted | ASSUMPTION: "stop dreading" read as "spend less time and pain on" |
| Metric | Median days-to-close | inserted | FACT that it is observable: the product already logs close start and sign-off (supplied telemetry note) |
| How it is observed | Close-period start and controller sign-off timestamps | stated | Supplied telemetry note |
| By how much | 6 → 4 days | inserted | ASSUMPTION: baseline 6 is from the supplied Q3 dashboard; the target of 4 is a planning proposal |
| By when | End of Q2 2027 | inserted | ASSUMPTION: matches the two-quarter build ask |
| Beneficiary persona | Corporate-accounting controllers, mid-market | stated | The pitch names "accounting customers"; the supplied segment list narrows it |
| Problem context | Month-end close in Ledgerline | stated | The pitch |
| Guardrail | Close-module tickets don't rise; cost to serve ≤ $1 per entity per close | inserted | ASSUMPTION: a copilot can shorten the close by pushing work into support or model spend; this keeps it honest |

**Output set aside:** the copilot. It might be the right how; it is not the outcome.
**Vanity check:** "Dread" could fall in a survey while the close stays six days long. Days-to-close cannot.

## Other outcomes set aside

- Increase net revenue retention among close-module customers (a lagging, Viable-side outcome; worth tracking, too slow to steer this bet).
- Reduce close-related support tickets (useful secondary measure).

**Square this outcome speaks to most:** Usable (adoption and obstacles in the close), with Valuable next: would controllers pay more for a shorter close?

## Exit

**Pass**, carrying the shaped statement to `bdk-receipts`, with three inserted parts labeled. Receipts should look for evidence that a copilot moves days-to-close, and what actually makes closes long today.

Open question for the VP of Product: is 4 days the bar you'd fund, or is it 5? The answer changes the Taste Test threshold, not this exit.

## Why this is good

The pitch was all output and feeling, but the material held an outcome. The skill reshaped instead of rejecting, and labeled every part it inserted so nobody mistakes the proposal for the sponsor's commitment.
