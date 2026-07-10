# The Entity Glossary

`Status: v1.0 (2026-07-10)` `Expands: spec §19` `License: CC BY 4.0`

The entity glossary is the shared vocabulary humans and agents use to interpret the entity's world consistently — and one of the highest-leverage continuity assets EIOS produces. This document expands [§19 of the EIOS master documentation](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md); the specification wins on any divergence.

## 1. Why glossaries matter more for entities

People leave, and their vocabulary leaves with them. The project codename nobody wrote down, the customer always called by a nickname, the internal shorthand that meant something precise in 2024 — these are how ten years of records become unreadable. A maintained glossary lets a new employee, a new agent, or a future owner correctly interpret the entity's accumulated record. It is also what makes agent behavior consistent: two agents using two names for the same customer will fragment that customer's history.

## 2. What belongs in — and out

**In** (spec §19.1): terms unique to the entity (products, codenames, shorthand, team and process names); customer/partner/market vocabulary with entity-specific meaning; role, decision-type, and governance vocabulary; broadly known concepts that carry a *specific local meaning*; jurisdiction- or industry-specific terms the entity must use precisely.

**Out** (spec §19.2): the general business dictionary. "Revenue" does not need an entry — unless this entity recognizes revenue in a specific way worth pinning down, in which case *that* is the entry.

The test: **would a competent newcomer misunderstand records without this entry?** If yes, in. If no, out.

## 3. The term lifecycle

```
candidate → active → merged / deprecated
```

- **candidate** — detected (usually by an agent) but not yet confirmed by an authorized role. Candidates are cheap; confirmation is the quality gate.
- **active** — the current accepted term, used in metadata, retrieval, and views.
- **merged** — connected to a preferred term that now carries the meaning; the alias trail is preserved so old records still resolve.
- **deprecated** — no longer used, retained for interpreting historical records. Deprecated terms are never deleted: they are the decoder ring for the archive.

Agents propose; authorized roles confirm (Principle 27 applies to vocabulary too — a glossary confirmation is a small decision).

## 4. Anatomy of a good entry

Per spec §19.4, an entry carries: stable ID, term, definition, aliases, status, sensitivity, related terms, related objects, source references, and an owner role. In practice the qualities that matter:

- **The definition states the entity-specific meaning**, not the dictionary meaning.
- **Aliases are collected aggressively** — every nickname and abbreviation found in real records belongs on the canonical entry.
- **Source refs point at first/defining use** — where the term was coined or fixed.
- **Sensitivity is honored**: a codename for an unannounced initiative is itself sensitive; its glossary entry inherits that.
- **Owner role, not owner person** — vocabulary stewardship must survive turnover.

## 5. Operating the glossary

- **Capture at ingestion.** The inbound flow is where unknown terms surface; the classifying agent proposes candidates as part of normal triage (spec §21.4 agent rule) rather than as a separate chore.
- **Confirm in batches.** A short recurring review by the owning roles keeps the candidate queue moving without making vocabulary a meeting topic.
- **Bind retrieval to the glossary.** Search and agent context should expand aliases to canonical terms — that is where consistency pays off.
- **Watch for drift.** When usage in new records stops matching a definition, that is a signal: either the meaning evolved (update, with the change trail) or the organization is fragmenting its language (surface it).
- **Keep it small.** A glossary of 60 precise entries outperforms 600 vague ones. Prune by the newcomer test.

---

© 2026 Valto Loikkanen. Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to Valto Loikkanen / Entity Core. Sibling concept: the PIOS Personal Glossary — inherited pattern; the subject shifts from personal nuance to institutional vocabulary and continuity.
