# Munich AI Nexus — Module 2 Retrospective

**Behavior: Explicit, Inspectable Planning**
📍 Munich · ~25 participants · Workshop format

## 1. Overview

Module 2 of the Production Readiness Blueprint focused on **agent behavior under real-world constraints**: rate limits, partial failures, multimodal input, and missing decision traces.

Compared to earlier sessions, this meetup intentionally traded scale for depth. The result was a highly engaged room, a workshop-like dynamic, and concrete insights from teams at very different maturity levels.

Key theme of the evening:

> Most agent failures are not caused by bad reasoning — they happen when reasoning meets reality.

---

## 2. Contributions

### 2.1 Andrei — Operating Agent Systems Under Real Constraints

An end-to-end walkthrough of a production AI application serving tens of thousands of users daily, with a focus on **behavioral decisions forced by infrastructure and usage reality**.

**Key patterns and lessons:**

* **Context shaping over raw persistence**
  User chat history is rewritten before storage to ensure stability and policy alignment. Prompts undergo similar normalization via intent detection before routing.

* **Intent-first routing**
  Requests are classified early and routed to distinct workflows (AI search, summarization, generation, etc.), rather than relying on a single “do everything” model.

* **Small models by default**
  Smaller, cheaper models handle most steps. Queries are enriched or normalized before escalation to frontier models when necessary.

* **Fallback as policy, not retry**
  The system spans multiple data centers and model families (including internal models). During a recent regional outage, users were unaffected due to explicit fallback rules.

* **Human choice as a control mechanism**
  Users can choose between models with clear indications of capability and *total cost* (infrastructure + operations), rather than opaque “auto-best” routing.

* **Adversarial behavior is assumed**
  Internal users frequently attempt jailbreaks. Guardrails are therefore designed with misuse in mind, not just happy paths.

* **Operational hardening over time**
  After a silent upstream model update changed behavior without notice, model versions were locked to preserve stability.

**Takeaway:**
Reliability emerged not from better models, but from **making behavior explicit**: what to do, when to escalate, when to fall back, and when to refuse.

---

### 2.2 Brinda & Tanja — Multimodal Intake as a Planning Problem (Workshop)

A hands-on, discussion-driven session centered on **email-based intake with attachments** (PDFs, scans, images) and the challenge of routing work to the right human expertise.

**Current approach:**

* ~80 skills/categories
* Model detects relevant skill(s) and routes the request
* Goal: reduce misrouting and dependency on human routers

**Observed patterns:**

* Earlier models performed better with hierarchical classification
* Newer models perform better when given the full category list plus context
* Long documents are used to extract specific fields (PII, contract IDs, dates, addresses)
* Long-term vision: move from routing → execution (e.g. auto-creating CRM entries)

**Confidence & fallback:**

* The system uses an LLM-generated confidence score (1–5 scale)
* In practice, mid-range values are rarely produced (scores cluster at extremes)
* Fallback is human correction: misrouted items are fixed manually, feeding back into the system
* Primary objective is to reduce external human routing, not eliminate humans entirely

**Discussion insight:**
Discrete confidence buckets tend to collapse with LLMs. Continuous confidence signals (e.g. 0–1) may better support thresholding and policy-based decisions.

---

## 3. Menti Results — Aggregated Signal

### Where behavior breaks first

* Opaque reasoning & decisions: **~54%**
* Not in production yet: ~31%
* Other factors (rate limits, multimodal chaos): minor

### Explicitness of planning today

* No explicit plan at all: **50%**
* Plan exists but not persisted/enforced: ~40%
* Fully explicit, enforced, traceable: **~7%**

### Execution constraints causing most trouble

* Rate limits / throttling: **~43%**
* Cost ceilings: ~21%
* Tool incompatibilities: ~21%

### When the preferred model isn’t available

* Silent downgrade (users unaware): **~33%**
* Fail loudly: ~27%
* “We haven’t designed this”: ~20%
* Policy-based routing: **0%**

### Multimodal pain points

* Long documents / scattered information: **~58%**
* Poor input quality: ~25%

### Handling long documents today

* Chunk + embed: ~40%
* Send everything to the model: ~20%
* Extract → assemble → reason: ~20%
* Still experimenting: ~20%

### Explainability when things go wrong

* Partial logs, unclear decisions: ~36%
* Execution trace but not reasoning: ~36%
* Fully traceable end-to-end: ~21%

---

## 4. Cross-Cutting Observations

* **Planning remains largely implicit** in most systems
* **Fallback behavior is ad hoc or silent**, not policy-driven
* **Observability stops at execution**, not reasoning
* Teams fear **silent failure** more than incorrect answers
* Confidence scoring, guardrails, and fallback are all *behavioral* problems, not model problems

A clear pattern emerged:

> At early stages, models decide.
> At scale, policies decide.

---

## 5. What Worked

* Smaller, repeat audience → higher depth
* Workshop format → active participation
* Real production failures → higher trust
* Explicit tradeoff discussions → better insights

## 6. What to Improve

* Stricter timeboxing on Q&A
* Even clearer boundaries between “talk” and “workshop”
* More explicit synthesis slides to close each segment

---

## 7. Looking Ahead

Module 2 confirmed that **behavior is the next bottleneck once context stabilizes**.

As systems make planning explicit, the next challenges become:

* enforcement
* state management
* observability
* auditability
