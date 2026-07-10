# Recognized Entity Views

`Status: v1.0 (2026-07-10)` `Expands: spec §22` `License: CC BY 4.0`

Business plans, SWOTs, board reports, and roadmaps are not documents to be written — they are **views to be projected** from living entity knowledge. This document expands [§22 of the EIOS master documentation](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md); the specification wins on any divergence.

## 1. The core idea

A conventional business plan is written once, ages immediately, and diverges from reality until someone rewrites it. A **recognized entity view** inverts this: the underlying knowledge (customers, strategy, financials, risks, decisions, assumptions) lives and updates continuously; the familiar artifact is a *projection* over it, regenerable at any time.

Three levels (spec §22.2):

1. **Underlying entity knowledge** — the living layer.
2. **Structured canonical objects** — value propositions, segments, objectives, risks, capabilities, revenue models, assumptions, milestones.
3. **Recognized views** — the artifacts stakeholders actually ask for.

When the knowledge changes, views don't rot — they become *candidates for regeneration*.

## 2. The view families

| Family | Views |
| --- | --- |
| **Strategic** | Business plan, strategy document, annual plan, OKRs, roadmap, mission/vision/values statements, SWOT, scenario plan |
| **Market and value** | Value proposition canvas, customer segmentation, JTBD map, customer journey, market map, competitive analysis, positioning statement, go-to-market plan, business model canvas |
| **Governance and risk** | Board report, investor update, risk register, decision log, compliance register, policy register, approval matrix, stakeholder map |
| **Operating** | Operating model, capability map, responsibility matrix, process map, team structure, project portfolio, resource plan, meeting rhythm, agent role map |
| **Product and service** | Product strategy, product roadmap, PRD, feature map, release plan, service blueprint, architecture overview |
| **Financial** | Financial forecast, budget, actuals vs budget, viability view |

The families matter operationally: views in one family tend to share source objects, review cycles, and approving roles — a board report and a risk register draw on overlapping objects and both answer to governance.

## 3. Living, ratified, candidate

Every view exists in up to three version states (spec §22.3), and **the states must never be conflated**:

- **Living** — continuously updated from current knowledge; useful daily; *not approved*.
- **Ratified** — frozen and formally approved (e.g. "Business Plan v1.0, board-approved"); carries authority; used externally.
- **Candidate** — generated because underlying knowledge changed since ratification; awaiting review.

The practical loop: a segment definition changes → the living business plan updates silently → a candidate version is flagged for the next review → humans ratify (or not) → the ratified version becomes the new external truth. Agents may generate candidates freely; **only authorized roles ratify** (Principle 27 applies — ratification is a decision).

## 4. Anatomy of a view definition

A recognized view is defined by its metadata, not its layout (spec §22.4): view type, source objects, generation mode (manual / assisted / automated), version type, review cycle, approval requirement, and approving role. Layout and format are presentation choices made per audience; the same view definition can project a slide deck for the board and a markdown page for the team.

**Worked example — SWOT:** each quadrant is a *query*, not prose: Strengths ← capabilities, assets, IP, customer trust; Weaknesses ← gaps, constraints, open risks; Opportunities ← market signals, customer needs, regulatory shifts; Threats ← competitors, substitutes, funding risks. A SWOT regenerated this way is automatically evidence-linked: every entry traces to the object that produced it.

## 5. Adoption guidance

- **Start with the views the entity already owes someone**: a board report, an investor update, a funding application. Existing obligations make the projection habit stick.
- **Ratify sparingly.** Most views can stay living; ratify the ones that carry external authority.
- **Never let a ratified view be the only record.** If editing the artifact is the only way to update it, the underlying objects are missing — fix that first.
- **Assumptions belong in the objects.** A forecast whose assumptions live only in a spreadsheet cell cannot tell you when it went stale; an assumption object with confidence and validation method can (spec §20.4).

---

© 2026 Valto Loikkanen. Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to Valto Loikkanen / Entity Core.
