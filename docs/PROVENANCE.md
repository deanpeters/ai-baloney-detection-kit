# Local reference map

AI-BDK uses original prose organized around its own Constitution and five checks. The repositories below are Dean's authorized local reference set. Paths are relative to `~/Code`; they are lookup locations, not runtime dependencies. This map documents design influence, not proof that a method is effective.

| Local repository | Inspected reference | Contribution to this build |
|---|---|---|
| `productside-marketing-and-sales-design-system` | `README.md` | Direct, outcome-focused presentation; no brand assets, confidential POV source documents, or inferred visual tokens copied. No visual artifact was needed. |
| `product-manager-prompts` | `README.md`, `AGENTS.md`, `generative-guidance-pattern.md`, `interaction-modes.md` | Reuse supplied context, progressive questions, bulk-drop and best-guess bypasses. AI-BDK omits that project's mandatory confirmation and fixed final-options block. |
| `ai-product-operating-model-skills` | `README.md`, `AGENTS.md`, `docs/EVIDENCE-STATUS.md` | Accountability, economic and operational outcomes, and separation of structural/synthetic evidence from organizational-use evidence. |
| `Mitre-Skills` | `README.md`, `skills/itk-trimming/SKILL.md`, `skills/itk-system-map/SKILL.md` | Consider simplifying or eliminating work; examine dependencies and effects beyond a feature. No MITRE tool text or full method copied. |
| `product-manager-antagonist-skills` | `README.md`, `skills/pant-artifact-pressure-test/SKILL.md` | Challenge claims with reasons, prioritize consequential weaknesses, and state what survives scrutiny. |
| `product-manager-skills` | `README.md`, `skills/context-engineering-advisor/SKILL.md`, `skills/pol-probe-advisor/SKILL.md` | Decision-specific context and small revealing probes; useful methods should also teach. |
| `agent-research-captures` | `README.md` | Provenance/date fields and research gaps; private captures were not copied or treated as freely redistributable. |
| `AI-Augmented-Product-Discovery-Lab` | `README.md`, `skills/dlab-step07-solution-hypothesis/SKILL.md` | Falsifiable hypotheses, proposed criteria, direct notes accepted, plans distinct from validation. |
| `chaos-confusion-and-crapola` | `CLAUDE.md`, `slides/HANDOFF.md` | Terminology, audience promise, quick-check lineage, and humor. Keynote-specific reduced verification expectations do not transfer to AI-BDK. |
| `Productside/Productside-Precedents-Thinking` | `README.md`, `reference/evidence-and-attribution.md` | Context transfer needs testing; another context's success is not proof here. |
| `Productside/Productside-Evals-for-Product-Managers` | `README.md`, `AGENTS.md`, `reference/evidence-and-attribution.md`, `skills/ev-step6-validate-the-rubric/SKILL.md` | Test a rubric against known failure before trusting scores; judge verification is separate; do not invent human labels or sufficient sample sizes. |
| `Productside/Productside-ADLC-Skills` | `README.md`, `AGENTS.md`, `CLAUDE.md`, `skills/adlc-step4-validate-agent-behavior/SKILL.md` | Plan versus results, failure probes, authority boundaries, hard stops, rollback, and scoped readiness. |
| `Productside/Productside-Market-Intelligence-Skills` | `README.md`, `CONSTITUTION.md`, `AGENTS.md`, `CLAUDE.md`, `skills/mi-fuse-all-source/SKILL.md` | Inspection highlighted shared-origin and contradictory-source pitfalls. AI-BDK uses its existing independence rule; no ND-licensed skill text or fixed discipline-count ladder was ported. |

The six skills synthesize these design lessons in AI-BDK's terminology. They do not import the other projects' authority orders, label systems, launch rules, or numerical heuristics. AI-BDK keeps FACT / INFERENCE / ASSUMPTION / BEST GUESS; missing evidence remains an explicit status.

All new AI-BDK content and generated distributions use the repository's CC BY-NC-SA 4.0 license. Distribution includes the repository license. Attribution here records the lineage of original adaptations; it does not grant rights to redistribute the private reference libraries or their third-party source material.

## 2026-10-11 additions (the Baloney Funnel build)

| Local repository | Inspected reference | Contribution |
|---|---|---|
| `Productside/Productside-Precedents-Thinking` | `docs/SKILL-SPEC.md`, `catalog/INDEX.md`, `skills/ps-util-disassociate/` (SKILL, template, weak example), `.claude-plugin/`, `.codex-plugin/`, `scripts/skill_metadata.py`, `scripts/release_tools.py` | Repository shape: `skills/`, catalog with "these are not stages," the utility rule and six-utility ceiling, required teaching sections with violation signals, worked and weak examples, rich canonical frontmatter projected to a portable shape, generated `agents/openai.yaml`. BDK departs on purpose: funnel skills keep check names instead of `stepN` numbering. |
| `Productside/Productside-ADLC-Skills` | `catalog/INDEX.md`, `evals/README.md`, `evals/expected-behaviors.yaml`, `evals/cases/case-01-customer-support-assistant.yaml`, `skills/adlc-step6-observe-and-improve/SKILL.md`, `.claude-plugin/marketplace.json` | Use-case tests with gate answers written first, expected/forbidden behavior IDs, the learning loop and "do not silently restart," marketplace manifest shape. |
| `AI-Augmented-Product-Discovery-Lab` | `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` | `"skills": "./skills/"` and the Codex `interface` block. |
| `chaos-confusion-and-crapola` | `outline/deck-9-the-grid.md`, `notes/bdk-update-plan.md`, `images/AGENTS.md` (palette) | The Sort grid (Truth, the four moves, the square questions), the Monday four-risk 2×2, the hand-off list, and the `#00E874` accent. Read only; not edited. |
| `ai-product-operating-model-skills`, `product-manager-antagonist-skills`, `Mitre-Skills`, `Productside-Market-Intelligence-Skills` | Skill folder names only | Hand-off targets verified to exist: `workflow-to-skill-converter`, `human-aipom-work-contract`, `pant-executive-decision-review`, `pant-meeting-rehearsal`, `itk-trimming`, `mi-build-battle-card`, `adlc-step1-frame-intent`, `dlab-step03-persona`. No text copied. |

The four risks' questions are Dean's own wording (2026-10-11). The four-risk framing (value, usability, viability, feasibility) originates with Marty Cagan (SVPG), which Dean's Product Manager Skills also credit.
