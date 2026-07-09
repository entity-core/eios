# EIOS 1.0, Keel, and Weave

A unified master document for the Entity Information Operating System framework, the Weave Entity Context Blueprint, and the Keel implementation — the durable information foundation for entity continuity, governance, value creation, and self-improving operations.

`Generated: 2026-07-08` `Status: Working master v1.0` `Framework: EIOS` `Implementation: Keel` `Context Blueprint: Weave` `License: CC BY 4.0`

---

**Contents**

- [1. Purpose](#1-purpose)
- [2. Origins and Relationship to PIOS](#2-origins-and-relationship-to-pios)
- [3. Product Model](#3-product-model)
- [4. Governing Principles](#4-governing-principles)
- [5. Definition of EIOS](#5-definition-of-eios)
- [6. The Entity as the Center of Gravity](#6-the-entity-as-the-center-of-gravity)
- [7. Entity Viability](#7-entity-viability)
- [8. Entity DNA: Purpose, Mission, Vision, Values, Strategy](#8-entity-dna-purpose-mission-vision-values-strategy)
- [9. Served World, Customers, and Market Context](#9-served-world-customers-and-market-context)
- [10. Stakeholder Model](#10-stakeholder-model)
- [11. Financial and Economic Context](#11-financial-and-economic-context)
- [12. Agreements and Obligations](#12-agreements-and-obligations)
- [13. Entity Actors](#13-entity-actors)
- [14. Entity Circles and Access Layers](#14-entity-circles-and-access-layers)
- [15. Hard Boundaries and Soft Boundaries](#15-hard-boundaries-and-soft-boundaries)
- [16. Information Zones](#16-information-zones)
- [17. Inbound Flow](#17-inbound-flow)
- [18. Event Model](#18-event-model)
- [19. Entity Glossary](#19-entity-glossary)
- [20. Knowledge Model](#20-knowledge-model)
- [21. Weave — Entity Context Blueprint](#21-weave--entity-context-blueprint)
- [22. Recognized Entity Views](#22-recognized-entity-views)
- [23. Governance](#23-governance)
- [24. Meetings and Communications](#24-meetings-and-communications)
- [25. Self-Improving Entity Loops](#25-self-improving-entity-loops)
- [26. Customer Signal to Value Improvement Loop](#26-customer-signal-to-value-improvement-loop)
- [27. Product, Service, and Capability Information](#27-product-service-and-capability-information)
- [28. Intellectual Property and Assets](#28-intellectual-property-and-assets)
- [29. Operating System Layer](#29-operating-system-layer)
- [30. Lifecycle Models](#30-lifecycle-models)
- [31. Retrieval and Use](#31-retrieval-and-use)
- [32. Security, Sensitivity, and Guarded Handling](#32-security-sensitivity-and-guarded-handling)
- [33. Cross-Entity Collaboration](#33-cross-entity-collaboration)
- [34. Implementation Considerations](#34-implementation-considerations)
- [35. Portability and Continuity](#35-portability-and-continuity)
- [36. Minimum Viable EIOS](#36-minimum-viable-eios)
- [37. Naming and Terminology Mapping](#37-naming-and-terminology-mapping)
- [38. Conclusion](#38-conclusion)
- [39. License and Attribution](#39-license-and-attribution)

---

## 1. Purpose

An Entity Information Operating System is a foundational information architecture for an entity. Its purpose is to preserve, organize, govern, and operationalize the information that allows an entity to exist, act, learn, improve, create value, and remain viable over time.

EIOS treats the entity as the primary subject. The entity may be a company, cooperative, association, foundation, public body, ecosystem organization, project organization, business unit, or other structured entity.

An entity is different from a human individual. A human does not need to justify the right to exist through value creation. An entity does. An entity continues to exist because stakeholders continue to support it. That support may come through customer revenue, owner funding, member contribution, investment, public mandate, legitimacy, labor, trust, participation, or other resources.

Therefore, EIOS must model not only information and knowledge, but also purpose, mission, stakeholder value, customers, markets, financials, agreements, governance, decision rights, capabilities, operating loops, and continuity.

> **Foundational statement:** EIOS is the open framework. Keel is the usable implementation. An entity's Keel is its durable operating memory: not a knowledge base, not a CRM, not an intranet, but the place where everything the entity is, knows, owes, decides, and learns can be preserved and made usable by its people and its agents.

EIOS is not merely a knowledge base, document repository, CRM, ERP, project management system, intranet, data warehouse, or AI agent platform. It is the entity-level information foundation that connects these systems and preserves the entity's durable operating memory.

EIOS supports both human and AI actors as role-bearing participants in the entity. People, teams, departments, AI agents, tools, systems, partners, advisors, customers, and governance bodies can all be represented as actors or related entities with roles, responsibilities, access, authority, and accountability.

The long-term purpose of EIOS is **entity continuity**: the ability of the entity to continue operating, improving, and creating value beyond dependence on any single founder, employee, manager, partner, tool, AI agent, meeting, document, or undocumented process.

The system intentionally separates three things that many enterprise products collapse together:

- **What happened:** canonical events and immutable originals.
- **What it means:** knowledge objects, entity context, glossary terms, interpretations, summaries, and patterns.
- **How it is used:** retrieval APIs, agents, applications, dashboards, entity views, and governance surfaces.

## 2. Origins and Relationship to PIOS

EIOS originated as a sibling framework to PIOS, the Personal Information Operating System. As of 2026-07-08, EIOS is an independent framework: it recognizes its roots, inherits freely with attribution, and evolves on its own terms.

### 2.1 PIOS

PIOS is centered on an individual person. It is concerned with the person's information, context, memory, relationships, goals, projects, communications, life domains, knowledge, agents, and personal continuity. Its central question is: *How can an individual preserve, organize, understand, retrieve, govern, and use their information over time?*

### 2.2 EIOS

EIOS is centered on an entity. It is concerned with the entity's purpose, mission, stakeholders, customers, market, strategy, governance, financials, agreements, people, agents, products, services, operations, decisions, communications, knowledge, intellectual property, and viability. Its central question is: *How can an entity preserve, organize, understand, govern, operationalize, and improve its information over time so it can continue creating value for stakeholders?*

### 2.3 Independence and inheritance model

EIOS and PIOS are independent frameworks with a shared origin. The relationship is governed by four rules:

- **Copy at fork, not shared dependency.** Principles, terms, and patterns inherited from PIOS are copied into EIOS and owned here. Neither framework references the other as a live dependency.
- **Attribution carries lineage.** Recognition of origins is expressed through attribution, not through name matching or structural coupling.
- **No backwards compatibility.** Neither framework constrains the other. Inherited terms may be redefined in EIOS without coordination, and vice versa.
- **Divergence is documented, not accidental.** The [Naming and Terminology Mapping](#37-naming-and-terminology-mapping) section records which terms were inherited, from where, and how their EIOS meaning differs.

### 2.4 Shared architectural ancestry

EIOS inherits the following architectural principles from its PIOS origin:

- One central information core
- Capture first, organize later
- Preserve originals
- Maintain an event log
- Create living knowledge objects
- Treat derived summaries and dashboards as rebuildable views
- Maintain system definitions, agents, permissions, and governance rules as first-class information
- Use common language and structured context
- Allow both human-readable and machine-usable forms
- Support agents as information users and operators
- Separate raw events from interpreted meaning and applied use

The main difference is the subject:

| Dimension | PIOS | EIOS |
| --- | --- | --- |
| Center of gravity | Individual person | Entity |
| Primary owner | Person | Entity or entity governance |
| Core continuity | Personal continuity | Entity continuity |
| Main context | Person's life and world | Entity's purpose, stakeholders, market, operations, and governance |
| Main actors | Person, trusted people, AI agents | People, teams, departments, AI agents, systems, stakeholders |
| Access model | Personal circle | Entity circles and stakeholder layers |
| Governance | Personal authority and delegated trust | Role-based authority, decision rights, approvals, policies |
| Value logic | Personal meaning, goals, wellbeing, work | Stakeholder value, viability, financial sustainability, mission |
| Market/customer layer | Optional or entrepreneur-specific | First-class |
| Financial layer | Personal finance domain | Core viability and governance domain |
| Agreements | Personal legal/admin records | Binding entity obligations and relationships |
| Meetings | Personal planning and conversations | Primary source of decisions, actions, and institutional memory |
| Self-improvement | Personal learning and agent support | Entity-level recursive improvement loops |

## 3. Product Model

The EIOS distribution stack mirrors the shape of an operating system ecosystem: an open specification, a practical implementation, an organizing blueprint, and deployment profiles.

| Layer | Name | Role |
| --- | --- | --- |
| Open framework | **EIOS** | Entity Information Operating System: the open architecture, concepts, rules, information model, event model, glossary model, circle model, governance model, and portability requirements. |
| Implementation | **Keel** | The packaged implementation and product built according to EIOS. Keel runs the entity information core. |
| Context blueprint | **Weave** | The non-technical organizing canon for how entity information is named, grouped, interpreted, related, titled, summarized, tagged, and made understandable to humans and agents. |
| Entity instance | **Entity Keel** | An entity's own running Keel: its private source of truth, agent context, entity glossary, event log, originals, and knowledge projections. |
| Managed service | **Keel Managed** | Entity information management as a service, where infrastructure, backups, updates, connectors, security, and operations are managed for the entity. |
| Portable distribution | **Keel Self-Hosted** | A VM/server package that can run on any cloud provider, a company server, or on-premise infrastructure. |

### 3.1 Why "Keel"

The name Keel is intentionally structural rather than cognitive or organizational. The keel is the structural spine of a vessel. A vessel outlives its crew, gets refitted, changes flag, replaces its engines and instruments — but the keel is what makes it the same ship. That is entity continuity in one word:

- **Structural meaning:** the keel is laid first; everything else is built on and around it.
- **Continuity meaning:** crews change, cargo changes, routes change; the keel persists.
- **Stability meaning:** the keel keeps the vessel upright through changing conditions.

### 3.2 Why "Weave"

The name Weave describes how an entity's many threads — people, agents, agreements, decisions, customers, finances, obligations — are structured into one coherent fabric. A weave looks like plain material at a distance, but close up it is a deliberate structure of interlocking threads. Entity information behaves the same way: it looks like documents, meetings, contracts, and metrics on the surface, but underneath it is a structured, layered, contextual mesh that gives the entity its strength.

### 3.3 Framework, implementation, and blueprint

EIOS should not depend on any specific cloud provider, database, or storage technology. EIOS defines what a compliant entity information core should do. Weave defines the conceptual information organization used inside that core. Keel implements both in a concrete, usable stack.

> **Core distinction:** EIOS defines the open entity information architecture. Keel implements it. Weave defines the information organization logic inside it: the principles, categories, metadata conventions, terminology, examples, and decision rules agents use when entity information enters the system.

## 4. Governing Principles

> **Principle 1 — The entity is the center of gravity.** All information is organized according to how it relates to the entity's identity, value creation, governance, stakeholders, operations, and continuity.

> **Principle 2 — EIOS and PIOS share an origin but live independently.** PIOS is centered on a person. EIOS is centered on an entity. They share information operating system ancestry but apply it to different centers of gravity, with no compatibility requirement between them.

> **Principle 3 — Entity existence depends on sustained value creation.** An entity must eventually justify continued existence through stakeholder value, stakeholder support, and sustainable operation.

> **Principle 4 — Purpose, mission, and value are first-class information.** Purpose, mission, vision, values, strategy, stakeholders, and value propositions are not decorative. They guide entity reasoning and decision-making.

> **Principle 5 — The served world is first-class.** Customers, users, buyers, beneficiaries, members, communities, and market context are part of the entity's operating memory.

> **Principle 6 — Financials are first-class entity information.** Financials describe how the entity captures value, funds operations, invests in development, manages risk, maintains reserves, and demonstrates accountability.

> **Principle 7 — Agreements are first-class entity information.** Agreements define binding relationships, rights, obligations, risks, permissions, economic terms, and governance constraints.

> **Principle 8 — Originals are preserved.** Source materials remain intact where possible and are policy-immutable: protected through append-only handling, versioning, retention, and corrective events rather than silent mutation.

> **Principle 9 — Events are the canonical timeline.** The event log records what happened and provides the machine-readable spine of the entity's history.

> **Principle 10 — Knowledge is living and source-linked.** Knowledge is maintained as current interpretation, but connected to sources, events, decisions, and evidence.

> **Principle 11 — Derived views are rebuildable.** Summaries, dashboards, reports, indexes, and public views must not become the only source of truth.

> **Principle 12 — Humans and AI agents are role-bearing actors.** People, AI agents, teams, systems, and external parties are modeled as actors with roles, responsibilities, access, and authority.

> **Principle 13 — Governance is information.** Roles, authority, approvals, policies, responsibilities, and decision rights are represented explicitly.

> **Principle 14 — Discussion is not decision.** EIOS must distinguish dialogue, proposal, recommendation, approval, commitment, and action.

> **Principle 15 — Notification is not approval.** Approval must be explicit and traceable.

> **Principle 16 — Holding information does not imply sharing information.** Soft boundaries require need-to-know behavior and contextual abstraction.

> **Principle 17 — Hard boundaries are system-enforced.** Some information and actions require strict technical separation.

> **Principle 18 — Self-improving loops are governed loops.** EIOS connects signals, decisions, actions, outcomes, and updates into recursive improvement loops, but these loops require boundaries, approvals, measurement, and review.

> **Principle 19 — Institutional memory must compound.** Each meeting, decision, customer signal, project, financial update, agreement, and agent output should strengthen the entity's future understanding.

> **Principle 20 — EIOS reduces dependency on single individuals or tools.** Critical knowledge, values, strategy, IPR, processes, and operating logic become embedded in the entity's durable information core.

> **Principle 21 — Capture first, organize later.** Information should enter quickly and safely before perfect classification is attempted. Required metadata stays rare; richer Weave attributes can be added, backfilled, or reprocessed later.

> **Principle 22 — The event log is complete; entity History is curated.** Communications, captures, system activity, processing steps, corrections, and completed work all enter the canonical event log. The readable History surface is derived from selected events, structured updates, summaries, and retained artifacts.

> **Principle 23 — Weave guides meaning before technology chooses format.** Agents should first understand what kind of information an item represents, where it fits in the entity, and which terms should describe it. Only then should they choose storage format, event type, metadata structure, or processing route.

> **Principle 24 — An Entity Keel must be portable.** A complete Entity Keel must be exportable, recoverable, and runnable outside the infrastructure provider currently hosting it. Continuity through provider change, ownership change, and wind-down is a design requirement, not a feature.

## 5. Definition of EIOS

An Entity Information Operating System is a foundational information layer that allows an entity to manage its information as a durable, governed, agent-usable, and human-understandable operating foundation.

EIOS organizes entity information across:

- Identity
- Purpose
- Mission
- Vision
- Values
- Strategy
- Stakeholders
- Customers
- Users
- Buyers
- Beneficiaries
- Markets
- Products
- Services
- Capabilities
- Financials
- Agreements
- Intellectual property
- Assets
- People
- Teams
- AI agents
- Meetings
- Communications
- Decisions
- Approvals
- Projects
- Processes
- Tools
- Governance
- Customer signals
- Market signals
- Operating loops
- Performance metrics
- Risks
- Reserves and buffers
- Operating history

> **EIOS is not one application.** It is an information operating layer that may be implemented through multiple tools, databases, repositories, agents, APIs, dashboards, and workflows. Keel is its reference implementation.

## 6. The Entity as the Center of Gravity

### 6.1 Entity-centered information

In EIOS, all information is interpreted according to how it relates to the entity. Information may describe:

- What the entity is
- Why the entity exists
- Whom the entity serves
- What value the entity creates
- How the entity captures value
- What the entity owns
- What the entity knows
- What the entity has promised
- What the entity must do
- Who acts for the entity
- Who decides for the entity
- What the entity has learned
- What the entity is trying to become
- What threatens the entity
- What enables the entity to continue

The entity is not merely an account, workspace, tenant, folder, company profile, or database namespace. It is the primary subject of the system.

### 6.2 Entity as artificial continuity

An entity is an artificial structure that can outlive individual people. It may continue when founders leave, employees change, managers are replaced, ownership changes, tools are replaced, partners change, customers change, markets change, AI agents are upgraded, strategies evolve, products are rebuilt, and operating models are redesigned.

For this to happen, critical information must become embedded into the entity itself. This includes:

- Purpose
- Values
- Strategy
- Governance
- Customer understanding
- Market knowledge
- Financial logic
- Operating practices
- Intellectual property
- Decision history
- Product knowledge
- Relationship history
- Agreement obligations
- Cultural norms
- Agent roles
- Institutional memory

EIOS provides the information architecture for this embedding. Keel provides the running system that holds it.

## 7. Entity Viability

### 7.1 The viability principle

A human being does not need to justify existence through value creation. An entity does. An entity continues to exist only if it can create sufficient value for its stakeholders relative to the cost of operating, maintaining, governing, and developing the entity.

> **The basic viability relationship:** stakeholder value created and captured must eventually justify the cost of entity existence.

This does not mean every entity must be profitable every day. It means the entity must eventually maintain a credible balance between value creation, value capture, operating cost, development cost, stakeholder support, governance cost, risk, reserves, future potential, and continued legitimacy.

### 7.2 Stakeholder support

Stakeholders may sustain an entity through:

- Paying for products or services
- Funding development
- Investing capital
- Paying membership fees
- Contributing work
- Providing legitimacy
- Granting mandate
- Providing resources
- Participating in governance
- Sharing infrastructure
- Providing distribution
- Providing knowledge
- Accepting coordination costs
- Supporting future value creation

In some entity types, the same stakeholder may be both value recipient and value funder. This is common in cooperatives, associations, member-owned entities, public-private initiatives, and ecosystem organizations.

### 7.3 Cost of entity existence

Entity cost includes more than financial expense. It may include:

- Operating cost
- Development cost
- Management effort
- Governance effort
- Coordination cost
- Legal responsibility
- Compliance cost
- Reputation risk
- Infrastructure cost
- Communication overhead
- Decision-making burden
- Cultural maintenance
- Stakeholder trust expenditure
- Technical maintenance
- Agent supervision and monitoring
- Opportunity cost

### 7.4 Reserves and buffers

Entities require buffers to survive transition, uncertainty, delay, and disruption. Buffers may include:

- Financial reserves
- Human capability reserves
- Knowledge redundancy
- Strategic optionality
- Customer diversity
- Partner diversity
- Technical resilience
- Operational slack
- Reputation capital
- Trust reserves
- Intellectual property
- Data assets
- Market insight
- Legal continuity
- Governance clarity

EIOS should support visibility into both current viability and transition capacity.

### 7.5 Entity viability model

```
Entity Viability
Purpose
Stakeholder value
Value creation
Value capture
Revenue
Funding
Operating cost
Development cost
Governance cost
Stakeholder support
Reserves and buffers
Transition capacity
Risks
Continued legitimacy
```

## 8. Entity DNA: Purpose, Mission, Vision, Values, Strategy

### 8.1 Entity DNA

Entity DNA contains the information that defines who the entity is and what should guide its decisions. It includes purpose, mission, vision, values, principles, strategy, strategic objectives, cultural commitments, identity statements, and long-term direction.

> **Entity DNA should not be treated as decorative text.** It should be used as a decision lens by both humans and agents.

#### Purpose — why the entity exists

Reason for existence, founder intent, societal purpose, customer problem to solve, cooperative need, public mandate, ecosystem role, community commitment, value creation rationale.

#### Mission — what value, to whom

Connects served stakeholders, value created, activities performed, outcomes pursued, and boundaries of action.

#### Vision — the future being created

What should the entity become? What should be true in 5 to 10 years? What larger change does the entity seek? What would success look like from the outside? How should future stakeholders experience the entity?

#### Values and principles — expected behavior

Should influence hiring, partnerships, customer treatment, product design, pricing, governance, internal behavior, conflict handling, communication, use of AI, risk decisions, and public statements. EIOS preserves both declared values and evidence of values in action.

### 8.2 Strategy

Strategy answers how the entity creates, delivers, sustains, and captures value. Strategy may include:

- Market position
- Customer focus
- Competitive advantage
- Capabilities
- Resource allocation
- Partnerships
- Pricing logic
- Product direction
- Operating model
- Growth logic
- Risk posture
- Differentiation
- Timing
- Execution priorities

## 9. Served World, Customers, and Market Context

### 9.1 Served world

An entity does not merely exist in an external environment. It exists in relation to a **served world**: the people, organizations, markets, communities, or systems for whom the entity creates value.

Depending on entity type, the served world may include customers, users, buyers, citizens, members, patients, students, developers, ecosystem participants, beneficiaries, communities, public-sector stakeholders, and industry actors.

### 9.2 Customers and users

For a commercial entity, customers, users, and buyers are first-class EIOS concepts. They may be different actors:

| Role | Meaning |
| --- | --- |
| User | Uses the product or service. |
| Buyer | Makes the purchase decision. |
| Customer | Pays or contracts. |
| Beneficiary | Receives value. |
| Recommender | Influences adoption. |
| Administrator | Manages use. |
| Champion | Promotes internally. |
| Blocker | Prevents adoption. |

EIOS should preserve these distinctions.

### 9.3 Jobs to be done

Jobs to be done describe the progress a stakeholder is trying to make in a given context. A job may include situation, trigger, desired progress, functional need, emotional need, social need, current alternative, pain, risk, desired outcome, success criteria, budget logic, and decision context.

```yaml
job_to_be_done:
  id: jtbd_example
  stakeholder_segment: founder_led_sme
  situation: trying_to_apply_ai_to_business_operations
  desired_progress: move_from_tool_experimentation_to_operational_capability
  current_alternatives:
    - ad_hoc_chat_ai_use
    - isolated_workflow_automation
  pains:
    - lack_of_clarity
    - too_many_tools
    - unclear_next_steps
  desired_outcomes:
    - operational_confidence
    - practical_use_cases
    - safe_first_agentic_workflows
  evidence_refs:
    - customer_interview_001
    - workshop_feedback_003
```

### 9.4 Value propositions

A value proposition defines why a stakeholder should care about the entity's product, service, initiative, or existence. It may include target stakeholder, problem addressed, desired outcome, offered solution, differentiation, evidence, cost or tradeoff, value capture logic, proof points, and risks and assumptions.

### 9.5 Market signals

Market signals are observations from the served world that may affect strategy, product, operations, or viability. Sources may include:

- Customer conversations
- Support requests
- Sales calls
- Lost deals
- Churn analysis
- Competitor activity
- Industry news
- Policy changes
- Technology shifts
- Partner feedback
- Community discussion
- Usage data
- Surveys
- Public reports
- Analyst notes
- Social media
- Field observations

> **Rule:** market signals should be source-linked, time-stamped, and connected to strategy, product, customer segments, and decisions.

## 10. Stakeholder Model

### 10.1 Stakeholders

Stakeholders are actors or groups who affect or are affected by the entity. Typical stakeholders include:

- Customers
- Users
- Buyers
- Beneficiaries
- Shareholders
- Owners
- Members
- Board of directors
- Management
- Employees
- Teams
- Partners
- Advisors
- Investors
- Suppliers
- Regulators
- Funders
- Communities
- Ecosystem participants
- Public audiences

### 10.2 Stakeholder roles

Stakeholders may relate to the entity through different roles:

| Stakeholder | Role pattern |
| --- | --- |
| Customer | Value recipient and payer |
| User | Value user |
| Buyer | Purchase decision-maker |
| Owner | Value funder and economic beneficiary |
| Shareholder | Owner of economic interest |
| Board | Governance authority |
| Management | Operational authority |
| Employee | Execution and knowledge actor |
| Partner | External capability contributor |
| Advisor | External knowledge contributor |
| Regulator | Compliance authority |
| Community | Legitimacy environment |

A single stakeholder can hold multiple roles. For example: a cooperative member may be owner, customer, user, and governance participant. A founder may be owner, board member, manager, employee, and product visionary. A public body may be funder, regulator, customer, and policy stakeholder. A strategic partner may be supplier, customer, and co-developer.

## 11. Financial and Economic Context

### 11.1 Financials as first-class entity information

Financials are central to entity viability. For a person, financials may be one life domain. For a business entity, financials are part of the entity's survival logic. Financials answer: Can the entity continue existing? Can it create value sustainably? Can it capture enough value? Can it fund operations and development? Can it survive transition? Can stakeholders trust it? Can commitments be met? Can reserves be maintained?

### 11.2 Financial layers

EIOS represents financials across four layers:

#### Accounting truth

Formal financial records: chart of accounts, general ledger, trial balance, profit and loss, balance sheet, cash flow statement, accounts receivable/payable, invoices, receipts, payroll, tax records, depreciation, accruals, assets, liabilities, equity, debt.

#### Management finance

Internal decision layer: budget, forecast, actuals versus budget, cash runway, burn rate, gross margin, contribution margin, unit economics, CAC, LTV, MRR/ARR, churn, expansion revenue, cost centers, profit centers, scenario plans.

#### Value economics

Strategic value layer: who pays, why they pay, what value is created and captured, what delivery/improvement/growth cost, what reserves are needed, what the transition buffer is, and the long-term sustainability logic.

#### Governance and reporting

Authority and accountability layer: board reports, investor reports, tax reports, audit records, approval thresholds, spending authority, financial policies, funding decisions, dividend or surplus decisions, capital allocation, financial risk register.

### 11.3 Standards and terminology

Financial information should use common and established terminology wherever possible: IFRS, IAS, local accounting terminology, GAAP concepts where relevant, chart of accounts structures, financial statement categories, management accounting terms, SaaS metrics where applicable, startup finance terms, banking and payment terminology, tax and VAT terminology, and audit and compliance terminology.

> **Standards are mappings and references, not rigid masters.** EIOS preserves jurisdiction-specific requirements, entity-specific meanings, and source records.

### 11.4 Financial objects

Financial objects may include: financial account, transaction, invoice, payment, revenue stream, cost category, cost center, profit center, budget, forecast, actual, cash position, runway, reserve, funding source, investment need, financial risk, financial KPI, financial policy, approval threshold, tax obligation, report, and scenario.

```yaml
financial_metric:
  id: metric_cash_runway
  metric_type: cash_runway
  value: 8.5
  unit: months
  calculation_basis:
    cash_balance: latest_verified_cash_position
    monthly_net_burn: average_last_3_months
  source_refs:
    - bank_balance_2026_06
    - pnl_actuals_2026_q2
  confidence: medium
  reviewed_by: finance_lead
  last_reviewed_at: 2026-06-30
```

### 11.5 Financial version states

Financial information may be: draft, preliminary, estimated, unaudited, management-reviewed, board-approved, filed, audited, superseded, scenario-based, forecast, or actual.

> **These states must not be collapsed.** A living forecast, a board-approved budget, a filed financial statement, and a scenario plan are different objects with different authority.

## 12. Agreements and Obligations

### 12.1 Agreements as first-class entity information

Agreements define binding relationships, rights, obligations, risks, permissions, economic terms, and governance constraints. EIOS should understand agreement types and common agreement topics without treating itself as a legal authority.

> **The actual signed agreement remains the source of truth.** EIOS helps classify, summarize, extract obligations, track dates, identify risk, and route legal or governance review to authorized roles.

### 12.2 Common agreement types

- Customer agreement
- Sales contract
- Terms of service
- Privacy policy
- Data processing agreement
- Non-disclosure agreement
- Employment agreement
- Contractor agreement
- Consulting agreement
- Service agreement
- SaaS agreement
- License agreement
- IP assignment agreement
- Shareholder agreement
- Founders agreement
- Investment agreement
- Partnership agreement
- Reseller agreement
- Supplier agreement
- Lease agreement
- Loan agreement
- Grant agreement
- Memorandum of understanding
- Service level agreement
- Statement of work
- Purchase order
- Framework agreement
- Board or advisory agreement

### 12.3 Common agreement topics

- Parties
- Purpose
- Scope
- Term and renewal
- Price and payment
- Deliverables
- Responsibilities
- Service levels
- Confidentiality
- Data protection
- Intellectual property
- Licensing
- Ownership
- Warranties
- Liability
- Indemnity
- Termination
- Governing law
- Dispute resolution
- Audit rights
- Non-compete
- Non-solicit
- Subcontracting
- Assignment
- Publicity rights
- Reporting obligations
- Security requirements
- Change management
- Acceptance criteria
- Support obligations
- Survival clauses

### 12.4 Agreement model

EIOS models agreements at three levels:

1. **Agreement type reference** — what kind of agreement this is and what topics usually matter.
2. **Specific agreement record** — the actual agreement the entity has entered into.
3. **Extracted obligation and governance layer** — what the entity must do, may do, must not do, should monitor, or must review.

```yaml
agreement_record:
  id: agreement_customer_001
  agreement_type: customer_service_agreement
  parties:
    - own_entity
    - customer_entity
  status: active
  effective_date: 2026-06-01
  renewal_date: 2027-06-01
  source_refs:
    - signed_contract_pdf_001
  topics_present:
    - payment_terms
    - confidentiality
    - data_protection
    - service_levels
    - termination
    - limitation_of_liability
  obligations:
    - provide_monthly_report
    - maintain_response_time
    - notify_security_incident
  sensitivity: guarded
  review_required_by: legal_or_authorized_role
```

### 12.5 Agreement lifecycle

```
template → draft → under_review → negotiation → approved_for_signature → signed → active
→ renewal_pending → amended → terminated → expired → archived → disputed
```

## 13. Entity Actors

### 13.1 Actor model

An actor is any human, AI agent, team, group, system, or external party that can observe, decide, communicate, act, or hold responsibility within the entity context. Actors may include:

- Founder
- Owner
- Board member
- Managing director
- Executive
- Department head
- Employee
- Contractor
- Advisor
- Partner
- Customer representative
- AI agent
- Software system
- Team
- Committee
- Working group

### 13.2 Humans and AI agents as role-bearing actors

EIOS represents both humans and AI agents as role-bearing actors. This does not mean humans and AI agents are identical legally, morally, or socially. It means the information architecture can represent their roles, responsibilities, permissions, channels, and decision relationships in a shared structure.

```yaml
actor:
  id: actor_example
  actor_type: human | ai_agent | team | external_party | system
  name: Example Actor
  role: innovation_manager
  title: Innovation Manager
  department: strategy
  responsibilities:
    - monitor_market_signals
    - prepare_monthly_update
  authority:
    can_recommend:
      - new_initiatives
    can_decide:
      - internal_research_priorities
    requires_approval:
      - budget_commitment
      - external_publication
  access:
    hard_boundary_groups:
      - strategy_workspace
    soft_boundary_rules:
      - generalize_customer_names_by_default
```

### 13.3 Roles

A role describes a responsibility pattern. Roles may include CEO, managing director, founder, board chair, product manager, sales lead, customer success lead, finance lead, legal advisor, project manager — and agent roles such as governance agent, research agent, customer insight agent, documentation agent, and meeting synthesis agent.

Roles should be connected to responsibilities, authority, access, decision rights, communication channels, reporting relationships, approval requirements, and knowledge areas.

## 14. Entity Circles and Access Layers

### 14.1 Entity circle model

EIOS represents actor proximity and access through entity circles:

```
Entity Core
Internal Circle
Extended Circle
Served World
Outer Circle
```

The circle vocabulary is inherited from the PIOS Circle model (Core Self → Inner → Extended → Outer). EIOS inserts the Served World as its own circle layer, because for an entity the stakeholders it creates value for are a distinct proximity band between close collaborators and the general public.

### 14.2 Entity Core

The Entity Core is the private source of truth for the entity. It contains originals, the event log, knowledge objects, derived views, governance rules, agent definitions, permissions, and system state.

> **Not every internal actor has access to all Entity Core information.** The Entity Core is a trust boundary, not a shared drive.

### 14.3 Internal Circle

The Internal Circle includes internal people, teams, departments, management, and internal AI agents: founders, employees, management, departments, teams, internal agents, internal systems, and internal committees. The Internal Circle usually requires granularity by role, function, team, and project.

### 14.4 Extended Circle

The Extended Circle includes close external actors: partners, advisors, contractors, investors, suppliers, professional service providers, strategic collaborators, and external project members. Extended Circle actors may require controlled access to selected projects, documents, decisions, and summaries.

### 14.5 Served World

The Served World includes the stakeholders for whom the entity creates value: customers, users, buyers, members, citizens, beneficiaries, and communities. The Served World may both receive value and provide feedback, data, revenue, legitimacy, or participation.

### 14.6 Outer Circle

The Outer Circle includes the broader public environment: public audiences, media, prospects, ecosystem observers, public regulators, the general market, social media, and website visitors. Outer Circle information is typically public, published, generalized, or intentionally exposed.

## 15. Hard Boundaries and Soft Boundaries

### 15.1 Hard boundaries

Hard boundaries are system-enforced restrictions. If a hard boundary applies, an actor cannot access the information. Examples:

- A contractor cannot access internal financial records.
- A customer-facing AI agent cannot access private employee records.
- A product agent cannot access acquisition discussions.
- A department workspace cannot access board-only documents.
- A partner view cannot access internal strategy notes.

Hard boundaries may be enforced through identity and access management, role-based access control, attribute-based access control, tenant boundaries, encryption, tool restrictions, query filters, data separation, network boundaries, agent runtime permissions, and API scopes.

### 15.2 Soft boundaries

Soft boundaries are context-aware sharing rules. An actor may technically have access to information but should only share what is appropriate for the audience, purpose, sensitivity, and need-to-know context. Soft boundaries reflect how responsible human actors behave.

> **The key rule:** holding information does not mean distributing information.

### 15.3 Need-to-know sharing

Need-to-know sharing means an actor shares only what is necessary for the recipient's legitimate purpose. Examples:

- Use "a team member" instead of naming an employee when the name is unnecessary.
- Use "an enterprise customer" instead of naming the customer when identity is not needed.
- Share the conclusion of a meeting without exposing the full transcript.
- Share a risk category without exposing private legal detail.
- Share a roadmap dependency without exposing confidential product plans.
- Share an approved public statement instead of internal deliberation.

### 15.4 Contextual abstraction

Contextual abstraction is the practice of preserving specificity internally while generalizing details for broader sharing when appropriate.

Example source detail: *"Anna from Customer X said the integration failed after their internal security review."*

Possible abstraction levels:

1. A customer contact reported an integration issue during a security review.
2. A customer-side security review surfaced an integration concern.
3. A security-review-related integration issue should be investigated.

EIOS supports such abstraction as an explicit information-handling behavior.

## 16. Information Zones

### 16.1 Five information zones

EIOS organizes information into five core zones. These zones are conceptual: they do not need to correspond directly to physical databases, folders, storage buckets, or applications.

| Zone | Purpose | Mutability |
| --- | --- | --- |
| **Originals** | Preserved source materials exactly as received: contracts, emails, chat exports, meeting recordings and transcripts, board decks, strategy documents, financial records, invoices, customer records, product specifications, research reports, design files, policies, legal documents, data exports, agent outputs, screenshots, audio, video. | Policy-immutable |
| **Events** | Append-only canonical entity event log recording what happened: meeting held, email received, contract signed, decision proposed/approved, roadmap updated, customer feedback received, market signal captured, invoice sent, employee onboarded, policy updated, agent recommendation created, access permission changed, public statement approved, product release completed. | Append-only |
| **Knowledge** | The living semantic layer: entity profile, strategy, product profile, customer profile, partner profile, market segment profile, decision record, policy, role description, project page, process description, risk register, glossary term, customer insight, value proposition, capability description, meeting summary, research synthesis. | Mutable but traceable |
| **Derived** | Rebuildable outputs: summaries, dashboards, reports, search indexes, embeddings, graph views, analytics, stakeholder summaries, board updates, product documentation views, market intelligence reports, customer segment summaries, public pages, redacted views, agent briefings. | Rebuildable |
| **System** | Definitions that operate EIOS: agent definitions, actor profiles, permission rules, access policies, soft-boundary rules, hard-boundary configurations, governance rules, approval workflows, connector states, processing manifests, data schemas, glossary rules, classification rules, source mappings, audit settings, retention policies, API permissions. | Controlled/versioned |

Originals should be preserved as received where possible. Events form the canonical timeline of the entity. Knowledge can be updated, but updates should remain traceable to sources and events. Derived information should not become the only source of truth. System information should be controlled, versioned, and auditable.

### 16.2 Information stability layers

Weave separates information by how stable it is, because storage, review cadence, agent confidence, and retrieval behavior differ by stability:

| Layer | Description | Entity examples | Agent handling |
| --- | --- | --- | --- |
| Stable | Information that rarely or never changes. | Founding facts, legal identity, registration data, purpose, articles of association. | Store with strong provenance; change only through explicit correction or versioned update. |
| Slowly changing | Profile-like information that evolves but should not churn daily. | Strategy, values in action, capability map, org structure, product positioning, key relationships. | Maintain as living profile notes with last-reviewed dates and source-linked updates. |
| Dynamic | Operational information that changes frequently. | Tasks, projects, meetings, customer signals, financial actuals, support tickets, campaign metrics. | Represent as events, records, logs, status views, and derived summaries. |

## 17. Inbound Flow

All information enters through a universal inbox, regardless of source. The source can be a file upload, API call, connected system, recurring stream, meeting recording, email, calendar feed, agent output, or manual note.

### 17.1 Universal inbox rule

The inbox is the only normal path into an Entity Keel. The agent responsible for the inbox performs triage, preservation, initial event creation, and routing. Information can be processed at different speeds:

- **Immediate triage:** identify source, type, time, original reference, sensitivity, and basic event.
- **Background enrichment:** extract text, metadata, glossary terms, actors, stakeholders, obligations, topics, and links.
- **Periodic interpretation:** build patterns, aggregates, summaries, recognized entity views, and retrieval indexes.

### 17.2 Connected systems

An Entity Keel connects to the systems where entity work already happens: email, calendar, Slack, Microsoft Teams, Google Drive, SharePoint, Notion, Confluence, Jira, Linear, GitHub, CRM, ERP, accounting systems, HR systems, customer support systems, product analytics, data warehouses, meeting transcription tools, and AI agent platforms.

> **Connected systems remain operational systems of record for their own current workflows.** A connected system is an input channel, not the long-term owner of the entity's accumulated record. The Entity Keel becomes the aggregated entity information foundation across all of them.

### 17.3 Source promotion lifecycle

Not everything a connected system emits deserves equal standing. Sources and their items move through promotion states so that low-value, high-volume noise does not corrupt the curated entity knowledge base:

```
parked → analyzed → mapped → enriched → history_included
```

| State | Meaning |
| --- | --- |
| parked | Received and preserved, but not yet interpreted. Safe default for bulk imports and new connectors. |
| analyzed | Type, structure, volume, and sensitivity understood; processing policy assigned. |
| mapped | Connected to entity concepts: stakeholders, projects, agreements, products, actors, glossary terms. |
| enriched | Summaries, extracted obligations, signals, and knowledge updates produced. |
| history_included | Curated into the entity's owner-facing History as meaningful updates, decisions, and milestones. |

### 17.4 Transition-time disposition

When an entity adopts EIOS over an existing tool landscape, each source, folder, app, or record needs a recorded disposition toward the Entity Keel:

| Disposition | Meaning |
| --- | --- |
| canonical | The Entity Keel retains the source or object as part of the entity's durable information foundation. |
| derived_projection | Useful as a view, summary, dashboard, or index, but regenerable from retained sources and events. |
| external_referenced | Truth remains in the external system (e.g. the accounting ledger, the code repository). The Keel records a reference, source rule, or event trail without copying the full source. |
| staged | Temporarily present for intake, screening, transformation, or review; not yet promoted. |
| excluded | Deliberately not imported, with the exclusion reason recorded so agents do not rediscover the same boundary. |
| guarded_pending | May belong in the Keel later, but sensitivity, privacy, legal, retention, or approval questions must be resolved first. |

## 18. Event Model

### 18.1 Event log

The event log is the canonical machine-readable timeline of the entity. It records what happened, when, where it came from, who was involved, which sources support it, and how it relates to entity knowledge.

### 18.2 Event envelope

```yaml
event:
  event_id: event_001
  event_type: decision_approved
  event_time: 2026-06-29T14:00:00+03:00
  recorded_time: 2026-06-29T14:05:00+03:00
  source:
    source_type: meeting_transcript
    source_ref: source_123
  actors:
    - actor_id: managing_director
      role: approver
    - actor_id: governance_agent
      role: recorder
  entity_context:
    project: project_example
    department: strategy
    stakeholder_scope:
      - internal_circle
  sensitivity: sensitive
  approval:
    approval_required: true
    approval_status: approved
  related_objects:
    - decision_001
    - roadmap_item_002
```

Time field hierarchy: `source_original_time` is the immutable timestamp asserted by the originating source; `event_time` is the best-effort chronological placement of the event (defaults to `source_original_time`); `recorded_time` is the system time of Keel ingestion.

### 18.3 Event types

- file_uploaded
- source_connected
- meeting_held
- meeting_transcribed
- meeting_summary_created
- email_received
- message_received
- customer_feedback_received
- market_signal_captured
- decision_proposed
- decision_discussed
- decision_approved
- decision_rejected
- approval_requested
- approval_granted
- approval_denied
- policy_updated
- project_created
- project_status_changed
- task_completed
- roadmap_updated
- feature_created
- contract_signed
- invoice_sent
- access_changed
- agent_definition_updated
- public_statement_published
- state_reverted

### 18.4 Correction and reversion events

Because the event log is append-only, rollback is expressed as new events rather than destructive edits. If an ingestion, parser, enrichment run, human correction, or agent action is later found to be wrong, the Keel writes a correction or reversion event that references the affected records and tells projections how to treat them.

```yaml
event:
  event_id: event_state_reverted_001
  event_type: state_reverted
  event_time: 2026-06-29T17:10:00+03:00
  recorded_time: 2026-06-29T17:11:03+03:00
  actor: organizer_agent
  target_event_ids:
    - event_bad_extraction_001
  target_object_ids:
    - knowledge:customer_profile_x
  reason: extraction_error
  reversion_scope: derived_projection_only
  replacement_event_id: event_reprocessed_001
  projection_instructions:
    - exclude_from_current_state
    - rebuild_summaries
    - refresh_indexes
```

> **Reversion events do not erase originals or hide the audit trail.** They tell current-state views, indexes, summaries, and retrieval systems which records are superseded, invalidated, or excluded from active interpretation. The original evidence remains available for audit and repair. For an entity this is also a compliance property: the correction itself becomes part of the governed record.

### 18.5 History

History is the human-readable projection of selected events. The event log should be more complete than the History view. Not every email, transcript line, system action, or internal trace should appear in human-facing History. History should be curated into meaningful updates, decisions, milestones, and summaries.

## 19. Entity Glossary

The entity glossary provides the shared vocabulary that humans and agents use to interpret the entity's world consistently. It should remain simple at first: stable IDs, definitions, aliases, status, and relationships.

### 19.1 What belongs in the glossary

- Terms unique to the entity: product names, project codenames, internal shorthand, team names, process names.
- Customer, partner, and market vocabulary with entity-specific meaning.
- Role names, department names, decision types, approval categories, and governance vocabulary.
- Concepts that are broadly known but have a specific meaning inside this entity.
- Jurisdiction- or industry-specific terms the entity must use precisely.

### 19.2 What should not be over-captured

The glossary should not become a general business dictionary. Widely known concepts should only be included when the entity needs a stable local meaning, mapping, or policy for them.

### 19.3 Term lifecycle

| Status | Use |
| --- | --- |
| candidate | Detected by an agent but not yet confirmed by an authorized role. |
| active | Current accepted term used in metadata, retrieval, and views. |
| merged | Term has been connected to another preferred term; the preferred term carries the meaning. |
| deprecated | No longer in active use, retained for interpreting historical records. |

### 19.4 Example glossary term

```yaml
glossary_term:
  id: term_northstar_program
  term: Northstar
  definition: Internal codename for the 2026 platform consolidation program.
  aliases:
    - NS
    - the consolidation
  status: active
  sensitivity: sensitive
  related_terms:
    - term_platform_team
  related_objects:
    - project_northstar
  source_refs:
    - meeting_2026_03_12
  owner_role: product_lead
```

> **Why the glossary matters more for entities:** people leave, and their vocabulary leaves with them. A maintained entity glossary is one of the highest-leverage continuity assets EIOS produces — it lets a new employee, a new agent, or a future owner correctly interpret ten years of records.

## 20. Knowledge Model

### 20.1 Knowledge objects

A knowledge object represents a living entity concept:

- Entity
- Stakeholder
- Customer
- Segment
- Product
- Service
- Capability
- Process
- Policy
- Decision
- Project
- Role
- Actor
- Team
- Market signal
- Value proposition
- Job to be done
- Partner
- Risk
- Opportunity
- IP asset
- Financial model
- Meeting summary
- Glossary term

### 20.2 Knowledge object structure

```yaml
knowledge_object:
  id: object_001
  object_type: value_proposition
  title: Value proposition for owner-led SMEs
  summary: Structured value statement for a target segment.
  status: active
  owner_actor: product_strategy_lead
  related_stakeholders:
    - founder_led_sme_segment
  related_events:
    - customer_interview_001
    - strategy_meeting_003
  related_sources:
    - transcript_001
    - workshop_feedback_002
  sensitivity: normal
  last_reviewed_at: 2026-06-29
  confidence: medium
```

### 20.3 Source-linked knowledge

Knowledge should be connected to its source evidence. A strategy statement, customer insight, product decision, financial assumption, risk, or value proposition should be traceable to a meeting, interview, document, research, market signal, decision record, customer feedback, approval, owner statement, operational data, financial data, agreement, legal source, or agent output.

This improves accountability, continuity, and trust — and it is what allows recognized entity views to be regenerated rather than rewritten from memory.

## 21. Weave — Entity Context Blueprint

### 21.1 Purpose

Weave is the organizing layer that tells humans and agents how entity information should be understood, named, grouped, related, and applied.

Weave is not primarily a database schema, folder tree, or application-specific taxonomy. It is a conceptual and operational blueprint that guides classification, retrieval, sharing, governance, and action. It answers questions such as:

- What type of information is this?
- Is it about the entity itself, the served world, the entity's operations, its viability, or its memory?
- Which stakeholder, project, agreement, product, decision, or time frame does it relate to?
- Which title, category, tag, summary, metadata, event type, and knowledge projection should an agent use?
- Which external standard or common vocabulary should be mapped where relevant?

### 21.2 Core areas

| Area | Contains |
| --- | --- |
| **The Entity** | Identity, purpose, mission, vision, values, strategy, ownership, governance, people, capabilities, products, services, assets. |
| **The Served World** | Customers, users, buyers, beneficiaries, members, markets, partners, competitors, ecosystem, regulators, communities. |
| **The Entity Operating System** | Processes, workflows, meetings, tools, agents, permissions, decisions, approvals, reporting, routines, metrics, systems. |
| **Entity Viability** | Financials, value creation, value capture, costs, reserves, buffers, risks, stakeholder support. |
| **Entity Memory** | Originals, events, knowledge, derived views, system rules. |

These areas are organizing lenses over one connected Entity Keel, not isolated containers. The same item may involve several areas at once; agents should preserve those relationships instead of copying items into disconnected silos.

### 21.3 Standards as mappings, not masters

Weave uses established standards, common terms, industry models, accounting language, agreement categories, and domain vocabularies wherever useful: accounting standards, financial statement terminology, legal agreement categories, project and product management terminology, customer experience terminology, CRM and ERP schemas, risk management terminology, industry-specific vocabularies, public standards, common business frameworks, and historical internal schemas.

> **External standards are treated as mappings and references, not as masters.** The entity's own language, context, jurisdiction, governance, and operating reality must be preserved.

### 21.4 Weave classification template

Weave includes concrete templates so agents can apply the principles consistently. A first-pass template for classifying an incoming item:

```yaml
weave_classification:
  entity_area: entity | served_world | entity_operating_system | entity_viability | entity_memory
  stability_layer: stable | slowly_changing | dynamic
  core_disposition: canonical | derived_projection | external_referenced | staged | excluded | guarded_pending
  related_concepts:
    stakeholders:
      - founder_led_sme_segment
    projects:
      - project_northstar
    agreements:
      - agreement_customer_001
    products:
      - product_main
  source:
    source_type: manual_upload | connected_system | meeting | agent_output | imported_archive | application_record
    origin_class: authored | observed | imported | inferred | generated
    source_ref: original-or-event-reference
  axes:
    sensitivity: normal | sensitive | guarded
    time_relevance: immediate | active | reference | archival
    technical_form: text | image | audio | video | structured_data | binary | code
  glossary_terms:
    - term_id: term_northstar_program
      relationship: primary_subject
  standards_mapping:
    external_vocabularies:
      - vocabulary: ifrs
        mapped_term: revenue_recognition
  recommended_storage:
    original: preserve_raw
    event_type: contract_signed
    knowledge_projection: agreements/agreement_customer_001.md
  confidence:
    classification: 0.82
    needs_review_by: authorized_role
```

Templates are guidance, not rigid schemas. Agents may leave fields empty, mark uncertainty, or propose new taxonomy values, but they should preserve the reason for each classification decision. Required fields stay rare; richer Weave metadata can be added, backfilled, or reprocessed later.

> **Agent rule:** when classification is uncertain, preserve the original, attach the best available metadata, explain the uncertainty, and ask whether the missing concept should become a glossary term, taxonomy value, area extension, or implementation detail.

## 22. Recognized Entity Views

### 22.1 Views as structured projections

Many common business artifacts should not be treated only as static documents. They should be understood as **recognized entity views** over living entity knowledge:

- Business plan
- SWOT
- Strategy document
- Board report
- Investor update
- Annual plan
- OKRs
- Risk register
- Business model canvas
- Value proposition canvas
- Customer segmentation
- JTBD map
- Customer journey
- Market map
- Competitive analysis
- Go-to-market plan
- Operating model
- Capability map
- Responsibility matrix
- Approval matrix
- Product roadmap
- PRD
- Service blueprint
- Architecture overview
- Financial forecast
- Budget
- Scenario plan

### 22.2 Three levels

1. **Underlying entity knowledge** — customers, mission, strategy, financials, risks, capabilities, market signals, decisions, assumptions.
2. **Structured canonical objects** — value proposition, customer segment, strategic objective, risk, capability, product, revenue model, cost structure, assumption, milestone.
3. **Recognized organizational views** — business plan, SWOT, board update, strategy document, investor deck, annual plan, roadmap, value proposition canvas.

### 22.3 Living, ratified, and candidate versions

#### Living version

Continuously updated from current knowledge. Example: a Living Business Plan updated from latest strategy, customer evidence, financials, roadmap, and market signals. Not formally approved until reviewed.

#### Ratified version

Frozen and approved. Example: Business Plan v1.0, approved by the board, used for investor discussions.

#### Candidate version

Generated from changes and awaiting review. Example: Business Plan v1.1 Candidate, generated because customer segment, revenue model, and roadmap changed. Needs management review.

### 22.4 Entity view metadata

```yaml
entity_view:
  view_type: business_plan
  source_objects:
    - mission
    - customer_segments
    - value_propositions
    - financial_model
    - roadmap
  generation_mode: manual | assisted | automated
  version_type: living | snapshot | approved
  review_cycle: quarterly
  approval_required: true
  approving_role: board | ceo | management_team
```

### 22.5 Example: SWOT

A SWOT should be a structured view composed from underlying objects:

```
SWOT
Strengths → linked to capabilities, assets, intellectual property, customer trust, team skills
Weaknesses → linked to gaps, risks, constraints, missing capabilities
Opportunities → linked to market signals, customer needs, regulatory shifts, technology changes
Threats → linked to competitors, substitutes, market risks, funding risks, regulation
```

## 23. Governance

### 23.1 Governance as first-class information

Governance is not external administration. It is part of the entity information system. Governance includes authority, responsibility, accountability, decision rights, approval rules, escalation paths, access rights, delegation, revocation, policy, compliance, auditability, verification, and risk handling.

### 23.2 Governance from entity information

EIOS derives governance from the entity's own information where possible. Governance sources may include legal documents, articles of association, board records, employment contracts, role descriptions, department structures, financial policies, delegation rules, project ownership records, HR systems, CRM ownership, meeting records, approval history, internal norms, and operating manuals.

### 23.3 Decision rights

Decision rights define who can decide what:

```yaml
decision_right:
  id: decision_right_budget_approval
  decision_type: budget_commitment
  threshold: 5000_eur
  responsible_role: managing_director
  consulted_roles:
    - finance_lead
  informed_roles:
    - leadership_team
  approval_required: true
  evidence_required:
    - purpose
    - budget_context
    - expected_outcome
  source_refs:
    - finance_policy_001
```

### 23.4 Approval

Approval must be explicit:

> **A notification is not approval. A meeting discussion is not approval. A comment is not necessarily approval. A dashboard view is not approval.**

Approval should have a requester, approver, scope, decision type, time, source, conditions, limitations, evidence, and status.

```yaml
approval_event:
  id: approval_001
  approval_type: external_publication
  requested_by: content_agent
  approved_by: managing_director
  approved_at: 2026-06-29T15:10:00+03:00
  scope:
    - publish_customer_case_summary
  limitations:
    - no_customer_name
    - no_financial_figures
  source_refs:
    - draft_document_456
    - approval_thread_123
```

### 23.5 Governance agent

A governance agent is an actor that observes, tracks, interprets, and routes governance-relevant information. It may participate in email threads, chat channels, meeting transcripts, board workflows, project spaces, CRM updates, document review, and agent-to-agent workflows.

A governance agent may:

- Detect possible decisions
- Distinguish discussion from decision
- Identify required approvals
- Route approval requests
- Record decision events
- Flag missing authority
- Track commitments
- Monitor guarded contexts
- Maintain audit trails
- Generalize details when sharing
- Escalate unclear cases

### 23.6 Proposals, rules, and earned autonomy

EIOS treats AI autonomy as earned and scoped. An agent may observe, detect, draft, classify, and suggest — but structured suggestions that affect durable knowledge, entity truth, sharing, cost, external commitments, or governance should be recorded as **proposals** before they become canonical changes, unless a **standing rule** already covers the exact class of action.

| Object | Purpose | Governance rule |
| --- | --- | --- |
| Proposal | A structured suggestion with rationale, evidence, confidence, expected result, and response state. | Rejected, edited, expired, and superseded proposals remain signal for future agent behavior. |
| Rule | A confirmed standing permission for a defined class of future action. | Created only through confirmation by a role holding the matching decision right. |
| Rule fire log | An audit record that a rule acted autonomously. | Every autonomous rule execution should be inspectable, reversible where possible, and linked to its resulting object. |
| Confidence fallback | Behavior when a rule match is weak or ambiguous. | Fall back to a proposal and escalate to the responsible role instead of acting. |

In an entity context, earned autonomy composes with decision rights: a rule can never grant an agent more authority than the role that confirmed the rule holds. Rules inherit thresholds, scopes, and evidence requirements from the decision rights they operationalize.

## 24. Meetings and Communications

### 24.1 Meetings as primary information sources

In entities, much operational truth emerges through human-to-human and human-to-agent communication: meetings, calls, workshops, board discussions, department meetings, customer meetings, partner meetings, email threads, chat channels, document comments, project management updates, and agent conversations.

EIOS treats communication records as primary sources for events, decisions, tasks, knowledge, governance, and history.

### 24.2 Meeting record structure

```yaml
meeting:
  id: meeting_001
  title: Strategy review
  time: 2026-06-29T10:00:00+03:00
  participants:
    - actor_ceo
    - actor_product_lead
    - governance_agent
  agenda:
    - review_market_signals
    - approve_next_roadmap_priority
  sources:
    - calendar_event_001
    - transcript_001
    - recording_001
  outputs:
    decisions:
      - decision_001
    action_items:
      - task_001
    open_questions:
      - question_001
    knowledge_updates:
      - market_summary_001
```

### 24.3 Conversation processing

A conversation may produce event records, decision records, approval requests, action items, knowledge updates, risk flags, customer insights, market signals, project updates, follow-up tasks, and history entries. EIOS preserves the original conversation while producing structured outputs.

### 24.4 Discussion versus decision

EIOS must distinguish:

```
mention → idea → question → concern → proposal → recommendation
→ agreement → decision → approval → commitment → action → publication
```

This distinction is essential for governance and accountability.

## 25. Self-Improving Entity Loops

### 25.1 Purpose

EIOS supports recursive improvement loops where entity information does not only accumulate but continuously improves the entity's products, services, processes, decisions, documentation, agents, and operating model.

A self-improving entity loop captures signals, interprets them in entity context, routes decisions or actions, measures outcomes, and updates the entity's knowledge, workflows, tools, prompts, policies, or product behavior.

### 25.2 General loop structure

```
Observe → Interpret → Decide → Act → Measure → Improve → Repeat
```

| Stage | Meaning |
| --- | --- |
| Observe | Collect signals from customers, users, products, support, sales, operations, financials, agreements, meetings, agents, or markets. |
| Interpret | Use entity context to understand what the signal means. |
| Decide | Choose an action, recommendation, experiment, escalation, approval request, or process change. |
| Act | Execute a bounded action, create a task, update a document, call a tool, draft a response, modify a workflow, or request human approval. |
| Measure | Record whether the action worked. |
| Improve | Update knowledge, process, prompt, tool, policy, product behavior, or documentation. |
| Repeat | Use the improved loop for the next instance. |

### 25.3 Loop object example

```yaml
entity_improvement_loop:
  id: loop_support_to_product_improvement
  loop_area: customer_support
  purpose: convert recurring support issues into product and documentation improvements
  observe:
    sources:
      - support_tickets
      - customer_calls
      - product_usage_events
  interpret:
    agents:
      - customer_insight_agent
      - product_triage_agent
    context:
      - product_knowledge
      - customer_segments
      - roadmap
      - known_issues
  decide:
    decision_type:
      - bug_fix
      - documentation_update
      - feature_request
      - escalation
    approval_required_for:
      - roadmap_change
      - customer_commitment
  act:
    allowed_actions:
      - create_ticket
      - update_internal_summary
      - draft_customer_reply
      - propose_doc_update
  measure:
    outcomes:
      - reduced_ticket_volume
      - faster_resolution_time
      - improved_activation
      - customer_satisfaction
  improve:
    update_targets:
      - product_knowledge
      - documentation
      - triage_rules
      - agent_prompt
      - roadmap_candidate_items
  governance:
    sensitivity: sensitive
    hard_boundaries:
      - no_access_to_private_hr_or_finance
    soft_boundaries:
      - generalize_customer_names_in_internal_broad_summaries
```

### 25.4 Loop governance

Self-improving loops must be governed loops. Each loop should define purpose, allowed sources, allowed actions, actors and agents, human approval requirements, boundary rules, metrics, failure conditions, escalation rules, review cadence, rollback path, and audit trail.

## 26. Customer Signal to Value Improvement Loop

### 26.1 Purpose

Customer and stakeholder interactions should be treated as first-class operating signals. The purpose of the customer signal loop is to turn real customer needs into owned actions and verified improvements.

### 26.2 Listening by helping

A strong customer signal model does not depend only on surveys or periodic research. Customers reveal high-quality information when they ask for help, seek clarification, try to use a product, report an issue, compare alternatives, request a feature, or express confusion. This creates a "listening by helping" pattern:

```
Customer asks for help
→ need is revealed
→ signal is captured
→ response helps the customer
→ entity learns from the interaction
```

### 26.3 Signal-to-action lifecycle

```
Signal captured → Session formed → Theme detected → Action proposed → Owner assigned
→ Dependencies mapped → Decision needed if required → Work executed → Outcome recorded
→ Recurrence monitored → Knowledge updated → Loop improved
```

### 26.4 Multidisciplinary routing

Customer experience issues rarely belong to only one team. A single signal may require product change, documentation change, support process change, pricing clarification, sales enablement, operational improvement, management decision, policy change, technical fix, or customer communication.

EIOS supports one signal creating multiple actions, cross-team ownership, dependency mapping, sequencing, escalation, management decision points, evidence attached to actions, and duplicate prevention by attaching new evidence to existing work.

### 26.5 Closing the loop

> **Completion is not the same as resolution.** A task is completed when work is marked done. A problem is resolved when the originating signal, need, risk, or friction declines or disappears.

EIOS supports recurrence monitoring. Examples:

- A support issue is resolved only if repeated support contacts decline.
- Documentation is improved only if repeated questions decline.
- Product onboarding is improved only if activation improves.
- An operational process is improved only if error rate declines.
- A financial control is improved only if variance or leakage declines.
- An agreement obligation is handled only if recurring risk is reduced.

### 26.6 Insight-heavy and action-light

Organizations often collect feedback but fail to convert insight into owned work and verified outcomes. EIOS prevents the entity from becoming insight-heavy and action-light by connecting signals to ownership, prioritization, decisions, dependencies, execution, outcome validation, and knowledge updates.

## 27. Product, Service, and Capability Information

### 27.1 Product and service knowledge

Products and services are ways the entity creates value for stakeholders. EIOS represents product and service information as structured knowledge, not only as documents. Product and service knowledge may include:

- Purpose
- Target stakeholders
- Value proposition
- User personas
- Jobs to be done
- Features
- Requirements
- Roadmap
- Pricing
- Positioning
- Customer evidence
- Usage data
- Support feedback
- Technical architecture
- Related decisions
- Risks
- Dependencies
- Intellectual property
- Release history

### 27.2 Capabilities

A capability is something the entity can reliably do: product development, customer acquisition, service delivery, research, manufacturing, data processing, AI agent operation, regulatory compliance, partner coordination, market intelligence, support, training, sales, governance, financial control.

EIOS connects capabilities to people, agents, processes, tools, knowledge, costs, and value creation.

## 28. Intellectual Property and Assets

### 28.1 Intellectual property

Intellectual property may include:

- Code
- Designs
- Trademarks
- Patents
- Copyrighted material
- Trade secrets
- Product concepts
- Data assets
- Documentation
- Methods
- Processes
- Models
- Training materials
- Brand assets
- Research outputs
- Proprietary datasets
- Agent configurations

EIOS preserves IPR context, ownership, provenance, restrictions, and usage rights.

### 28.2 Assets

Assets may include financial assets, physical assets, digital assets, data assets, customer relationships, contracts, licenses, domains, accounts, tools, repositories, infrastructure, brand assets, knowledge assets, and agent definitions.

Assets should be connected to responsibility, access, lifecycle, risk, and continuity.

## 29. Operating System Layer

### 29.1 Entity operating system

The entity operating system layer contains the information that describes how the entity operates: processes, workflows, meetings, routines, reporting cycles, governance cycles, decision flows, approval paths, project management, agent workflows, tool usage, communication patterns, dashboards, metrics, reviews, planning rhythms, and execution rhythms.

### 29.2 Entity operating rhythm

An entity has operating rhythms across time:

- Daily operations
- Weekly team meetings
- Monthly reporting
- Quarterly planning
- Annual strategy
- Board meetings
- Product release cycles
- Customer feedback cycles
- Financial review cycles
- Governance review cycles
- Agent monitoring cycles

EIOS connects work, decisions, meetings, strategy, and value signals across these rhythms.

## 30. Lifecycle Models

EIOS models information and operational objects through lifecycle states. A lifecycle helps distinguish current, proposed, approved, deprecated, completed, and archived information.

| Object | Lifecycle |
| --- | --- |
| Decision | proposed → discussed → drafted → reviewed → approved / rejected / deferred → implemented → revisited → superseded → archived |
| Project | idea → proposed → approved → active → blocked → completed / cancelled → archived |
| Policy | draft → reviewed → approved → active → deprecated → replaced → archived |
| Product | idea → discovery → validation → development → launch → growth → maintenance → retirement → archived |
| Customer | lead → prospect → opportunity → customer → expansion → support → renewal → dormant → former customer |
| Agent | proposed → configured → tested → active → restricted → suspended → retired → archived |
| Agreement | template → draft → under review → negotiation → approved for signature → signed → active → renewal pending → amended → terminated / expired → archived / disputed |
| Entity view | living → snapshot created → human review requested → approved → published → superseded → retired → archived |
| Glossary term | candidate → active → merged → deprecated |

## 31. Retrieval and Use

### 31.1 Retrieval

EIOS supports retrieval across originals, events, knowledge, derived views, and system rules. Retrieval may use:

- Keyword search
- Metadata filtering
- Structured queries
- Semantic retrieval
- Graph traversal
- Time-based retrieval
- Actor-based retrieval
- Source-based retrieval
- Project-based retrieval
- Stakeholder-based retrieval
- Approval-status retrieval
- Sensitivity-aware retrieval

> **Retrieve summary-first.** Good retrieval does not start by reading everything. Agents should choose the right navigation layer first — index, summary, History period, entity view, stakeholder page, project page, agreement register, event record, or original source — depending on the question. Vector and graph indexes are projections, not truth.

### 31.2 Agent use

- Retrieve context
- Summarize meetings
- Draft documents
- Prepare decisions
- Track approvals
- Monitor market signals
- Update knowledge objects
- Propose next actions
- Detect contradictions
- Create stakeholder summaries
- Generalize sensitive details
- Route governance requests
- Maintain glossaries
- Compare work to strategy
- Support continuity
- Improve loops

### 31.3 Human use

- Understand what happened
- Find current truth
- Review decisions
- Prepare meetings
- Onboard into roles
- Understand customers
- Track strategy
- Review project history
- Audit approvals
- Learn from past work
- Coordinate with agents
- Preserve institutional memory

## 32. Security, Sensitivity, and Guarded Handling

### 32.1 Sensitivity levels

| Level | Meaning | Examples |
| --- | --- | --- |
| **Normal** | Processed according to ordinary access and sharing rules. | Public product descriptions, internal process notes, non-sensitive project updates, approved public summaries. |
| **Sensitive** | Requires careful handling. | Customer-specific context, commercial negotiations, employee matters, financial information, legal context, strategy, partner discussions, internal conflicts, non-public roadmap details. |
| **Guarded** | Requires strong restrictions, approval, redaction, or isolation. | Credentials, tokens, private keys, M&A discussions, legal disputes, HR-sensitive matters, board-only materials, unpublished financials, high-impact external commitments, destructive actions, public statements requiring approval, contract approvals, financial commitments, untrusted inbound content. |

### 32.2 Guarded action contexts

Guarded handling applies not only to information but also to actions. Actions may be guarded when they:

- Spend money
- Publish externally
- Modify production systems
- Delete records
- Commit the entity legally
- Affect employees
- Affect customers
- Reveal sensitive information
- Change access rights
- Trigger external communication
- Create compliance risk

## 33. Cross-Entity Collaboration

### 33.1 Entity-to-entity relationships

Entities often collaborate with other entities: company and customer, company and supplier, company and partner, company and investor, company and regulator, company and public funder, company and ecosystem initiative, parent and subsidiary, joint venture partners.

### 33.2 Relationship record

```yaml
entity_relationship:
  id: relationship_001
  subject_entity: own_entity
  related_entity: partner_entity
  relationship_type: strategic_partner
  circle_scope: extended_circle
  active_projects:
    - project_001
  sharing_rules:
    - share_project_status
    - do_not_share_customer_names_without_approval
  decision_rights:
    - joint_steering_group_required_for_scope_change
```

### 33.3 Shared projections

Cross-entity collaboration relies on shared projections rather than uncontrolled merging of source truth. An entity may share approved summaries, project views, shared decisions, meeting minutes, status updates, deliverables, redacted records, partner dashboards, and public reports.

> **Each entity preserves its own source truth and governance context.** When both entities in a relationship run their own Entity Keel, collaboration happens through governed projections between Keels, never through merged storage.

Where an entity's people also maintain personal information systems (such as PIOS-based ones), the same rule applies: the entity's Keel and a person's own system exchange governed projections. The entity does not absorb personal source truth, and the person does not absorb entity source truth.

## 34. Implementation Considerations

### 34.1 Conceptual model versus storage

EIOS is a conceptual and operational information architecture. It can be implemented using different technologies: object storage, document storage, relational databases, graph databases, vector indexes, search engines, event logs, message queues, workflow engines, APIs, agent tools, file systems, knowledge repositories, data warehouses, and identity systems.

> **The conceptual model should not be reduced to one storage technology.** EIOS defines what a compliant entity information core should do; Keel chooses the stack.

### 34.2 Keel implementation profiles

| Profile | Description | Fit |
| --- | --- | --- |
| **Keel Managed** | Hosted entity information core: infrastructure, backups, updates, connectors, security, and operations managed as a service. The entity remains the primary authority and conceptual owner of its information; the service operates as a fiduciary steward with mandatory export, deletion, and takeover rights. | Entities that want the foundation without operating infrastructure. |
| **Keel Self-Hosted** | A portable VM/server distribution runnable on any cloud provider, a company server, or on-premise hardware. Same information model, same agent-facing service contract: switch base URL and credentials, not the architecture. | Entities with sovereignty, regulatory, or infrastructure requirements. |

The Keel service interface should be provider-neutral before it is implementation-specific. The agent-facing contract remains the same across profiles where possible.

### 34.3 Originals and projections

Originals remain preserved. Structured knowledge, summaries, dashboards, indexes, and documentation views are treated as projections where possible.

### 34.4 Existing systems and legacy schemas

Existing systems may remain operational systems of record for their own current workflows, while the Entity Keel becomes the aggregated entity information foundation. Existing schemas, taxonomies, and data models can be useful as mappings, references, or migration aids — but they should not automatically define the entity's primary organizing logic. EIOS treats external schemas as mappings, not masters.

### 34.5 Introduce specialized systems only when needed

Databases, queues, graph stores, vector stores, search engines, and orchestration platforms are added only when actual data volume or retrieval needs justify them. A small entity's first Keel can run on object storage, Markdown knowledge objects, JSON event logs, and a handful of agents.

## 35. Portability and Continuity

### 35.1 Portability requirement

A complete Entity Keel must be exportable, recoverable, and runnable outside the infrastructure provider currently hosting it. The export is not a folder of files — it is a reconstructable entity information core.

An Entity Keel export should include:

- Originals
- Canonical events
- Knowledge objects
- Entity glossary
- System definitions and governance rules
- Agent definitions and permissions
- Connector configuration (excluding secrets where necessary)
- Derived data where useful
- Rebuild instructions
- Deployment configuration

### 35.2 Keel Bundle model

| Artifact | Role |
| --- | --- |
| **Keel Template** | The parameterized infrastructure shape of an empty Entity Keel: storage zones, keys, policies, roles, indexes, audit logging, guardrails. Structure is golden and repeatable; entity-specific values stay parameterized. |
| **Keel Export Bundle** | The entity's exportable data payload, scoped or full. A full Keel Export Bundle carries everything needed for migration, rebuild, or takeover. Scoped bundles serve sharing, audits, due diligence, or partner projections. |
| **Provisioning Manifest** | Binds a specific template version, entity, account, region, security posture, and optional bundle hydration into one rebuildable Keel instance. |

### 35.3 Why portability is an entity survival property

For an entity, portability is not only a data right — it is a continuity mechanism for the events entities actually face:

- **Ownership change:** in an acquisition or succession, the Keel Export Bundle is the institutional memory being transferred.
- **Provider change:** the entity can move between Keel Managed and Keel Self-Hosted without losing its operating memory.
- **Wind-down:** obligations, records, and IP remain governed and retrievable through and after dissolution.
- **Audit and due diligence:** scoped bundles provide governed, evidence-linked views without exposing the full Entity Core.

### 35.4 Backup, versioning, and recovery

Originals and events require versioned, tested backup. Knowledge objects require version history. Derived data may be excluded from backup where rebuild instructions exist. Recovery must be rehearsed: a backup that has never been restored is a hypothesis, not a continuity plan.

## 36. Minimum Viable EIOS

A minimum viable EIOS for a small organization includes:

#### Entity foundation

Purpose, mission, vision, values, strategy, stakeholder map, customer segments, value propositions, basic governance roles.

#### Information core

Originals preservation, event log, knowledge objects, derived summaries, system rules.

#### Communication capture

Meeting summaries, decision records, email or channel ingestion, action item extraction, approval tracking.

#### Actor model

People, teams, AI agents, roles, responsibilities, decision rights, access rules.

#### Value and market context

Customers, jobs to be done, market signals, customer feedback, value propositions, product/service knowledge.

#### Financial context

Basic revenue model, cost structure, budget, forecast, actuals, cash position, runway, reserves, financial risks.

#### Agreements and obligations

Agreement register, obligation tracking, renewal dates, legal review flags, contract-sensitive handling.

#### Governance basics

Approval records, sensitive and guarded handling, hard boundaries, soft boundary rules, need-to-know sharing.

#### Self-improving loops

Customer signal loop, meeting-to-decision loop, support-to-product loop, financial review loop, agent improvement loop.

#### Continuity views

Entity history, decision log, project status, customer insight view, strategy alignment view, knowledge gaps, risk register, financial viability view.

## 37. Naming and Terminology Mapping

EIOS and Weave terms should remain stable across implementations even when underlying tools, services, and storage differ. This section also records terminology inherited from the PIOS origin, so divergence stays documented rather than accidental. Inherited terms carry no compatibility obligation in either direction.

| EIOS / Weave term | Meaning in EIOS | Inherited from (PIOS origin) | Divergence |
| --- | --- | --- | --- |
| EIOS | The open entity information framework. | PIOS | Entity-centered rather than person-centered. |
| Keel | The packaged implementation running the entity information core. | Core | Renamed; structural-nautical metaphor for entity continuity. |
| Weave | The entity context blueprint: organizing canon for meaning, naming, classification. | Cotton | Renamed; extends the fiber metaphor — personal fiber woven into entity fabric. |
| Entity Keel | An entity's own running instance and private source of truth. | Core Self | Renamed; owner is the entity/governance, not a person. |
| Keel Managed / Keel Self-Hosted | Deployment profiles. | Core Managed / Core Self-Hosted | Pattern inherited directly. |
| Entity Core | The innermost circle layer: the entity's private trust boundary. | Core Self (as circle center) | In EIOS, "Entity Core" names only the circle layer; the instance is "Entity Keel". |
| Entity circles | Entity Core → Internal → Extended → Served World → Outer. | Circle (Core Self → Inner → Extended → Outer) | Adds Served World as a distinct circle; renames Inner to Internal. |
| Five information zones | Originals, Events, Knowledge, Derived, System. | Five Core data zones | Inherited unchanged. |
| Sensitivity levels | normal / sensitive / guarded, extended to guarded actions. | Sensitivity axes | Inherited; action-guarding emphasized. |
| Source promotion lifecycle | parked → analyzed → mapped → enriched → history_included. | Source promotion lifecycle | Inherited unchanged. |
| core_disposition | Transition-time disposition of sources toward the Keel. | core_disposition | Inherited unchanged. |
| Correction/reversion events | state_reverted pattern for append-only rollback. | Correction and Reversion Events | Inherited; framed additionally as a compliance property. |
| Entity Glossary | Shared entity vocabulary with term lifecycle. | Personal Glossary | Subject shifts from personal nuance to institutional vocabulary and continuity. |
| Proposals, rules, earned autonomy | Agent autonomy earned through confirmed standing rules, bounded by decision rights. | Proposals, Rules, and Earned Autonomy | Composed with entity decision rights: a rule cannot exceed the confirming role's authority. |
| Keel Export Bundle / Keel Template / Provisioning Manifest | Portability artifacts. | Core Export Bundle / Core Template / Provisioning Manifest | Pattern inherited; reframed as entity survival property (M&A, succession, wind-down). |
| Entity History | Curated human-readable projection of the event log. | Update-first owner History | Inherited principle; curation authority follows governance roles. |
| Recognized entity views | Living / ratified / candidate business artifacts as projections. | Living views are projections | EIOS-native extension: formal ratification and approval workflow added. |
| Entity DNA | Purpose, mission, vision, values, strategy as a decision lens. | — | EIOS-native concept. |
| Entity viability | Value creation, capture, cost, reserves, legitimacy balance. | — | EIOS-native concept. |
| Served world | The stakeholders for whom the entity creates value. | — | EIOS-native concept. |
| Governance agent | Agent that detects decisions, routes approvals, maintains audit trails. | — | EIOS-native concept. |
| Self-improving entity loops | Governed observe→interpret→decide→act→measure→improve cycles. | — | EIOS-native concept. |

## 38. Conclusion

EIOS is an Entity Information Operating System: a framework for making an entity's existence, value creation, governance, knowledge, operations, and continuity information-native.

An entity is not merely a collection of documents, systems, people, meetings, agreements, and processes. It is a value-generating structure that must continuously justify and sustain its existence through stakeholder value.

EIOS gives the entity a durable information core — its Keel — that preserves originals, records events, maintains living knowledge, creates rebuildable views, and governs the system rules that allow humans and AI agents to act responsibly. Weave gives that core its organizing logic: how entity information is named, classified, related, and made understandable.

It supports the entity's ability to:

- Know why it exists
- Understand whom it serves
- Create and capture value
- Govern decisions
- Preserve institutional memory
- Coordinate people and agents
- Handle sensitive information
- Learn from customers and markets
- Maintain financial viability
- Track agreements and obligations
- Improve through governed loops
- Maintain continuity through change
- Operate beyond dependence on any single individual or tool
- Improve and renew itself over time

The ultimate purpose of EIOS is to help an entity remain intelligible, governable, useful, self-improving, and viable as it operates in a changing environment.

## 39. License and Attribution

### 39.1 Attribution

> **EIOS originated as a sibling framework to PIOS** (Personal Information Operating System, github.com/peecos), created by Valto Loikkanen. EIOS inherits architectural principles and terminology from PIOS 2.0 with permission and attribution. The frameworks evolve independently; no compatibility between them is implied or maintained.

### 39.2 License

- **Specification and documentation** (this document and the EIOS/Weave framework texts): [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may share and adapt for any purpose, including commercially, provided you give appropriate credit.
- **Reference code, schemas, and tooling** (Keel implementations and related software): [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### 39.3 Document status

EIOS 1.0, Keel, and Weave — Master Documentation. Working master v1.0, generated 2026-07-08 from the EIOS Framework working draft, restructured into the master documentation format with inherited sections (inbound flow, correction and reversion events, entity glossary, earned autonomy, portability) incorporated at fork. Names ratified 2026-07-08: EIOS / Keel / Weave / Entity Keel / Keel Managed / Keel Self-Hosted.