# Munich AI Nexus — Module 5 Retro

## Collaboration: Human Oversight by Design

**Host:** fortiss
**Module:** Collaboration — Human Oversight by Design
**Format:** Keynote, demo, World Café challenge, networking
**Resources:**

* Host slides: `slides/`
* Dr. Yuanting Liu keynote slides: `slides/`
* World Café board photos: `challenge/`

---

## 1. Session Focus

Module 5 focused on one of the hardest questions in production AI:

> How do we keep humans meaningfully in control as AI systems become more autonomous, adaptive, and action-oriented?

After previous modules on Context, Behavior, Execution, and State, this session moved to the collaboration layer: where humans intervene, approve, correct, override, and take responsibility.

The central framing of the evening was:

> Human oversight is not a button.
> It is architecture.

The session combined:

1. A keynote by **Dr. Yuanting Liu** on human oversight as an engineering capability
2. A fortiss demo by **Michael Neumeier** on human-guided continual learning and federated edge deployment
3. A World Café challenge around oversight mechanisms for adaptive AI systems
4. Group synthesis and networking

---

## 2. Registration Signal

The registration responses showed strong alignment with the topic.

Attendees were not asking whether humans should be involved. The stronger question was:

> When should humans be involved, what context do they need, and who remains accountable?

Recurring registration themes included:

* approving high-risk AI actions
* correcting wrong outputs
* handling uncertainty and low confidence
* escalation of edge cases
* feedback loops that actually improve the system
* unclear responsibility boundaries
* auditability and traceability gaps
* human review becoming a bottleneck

The strongest tension going into the event:

> Human oversight is needed, but manual review everywhere does not scale.

This set up the evening’s core design challenge:

> How do we achieve high automation without losing human control?

---

## 3. Keynote: Oversight Is Not a Button

**Speaker:** Dr. Yuanting Liu
**Topic:** Human oversight as architecture

Dr. Liu’s keynote gave the strongest conceptual framing of the evening.

The central argument:

> Human oversight is not a final approval step.
> It must be embedded across the system.

As AI systems move from generating suggestions to taking actions, every part of the pipeline can fail:

* data intake
* AI / ML components
* policy gates
* tool execution
* human handoff
* monitoring
* recovery
* system updates

This means oversight cannot be added only at the end of the process. Engineers need to reason about failure modes across the whole system.

Key engineering questions:

* What could fail?
* How likely is the failure?
* What is the exposure?
* What is the impact?
* Can the system validate automatically?
* Can it retry safely?
* Should it log and continue?
* Should it escalate?
* Should it stop?

A useful risk framing from the keynote:

```text
Operational risk = probability of error × exposure × impact
```

This shifts the conversation away from generic human-in-the-loop patterns and toward risk-based control design.

---

## 4. Oversight Needs Automation

A key insight from the keynote was that human oversight itself requires automation.

Manual oversight everywhere creates new failure modes:

* alert fatigue
* information overload
* slow feedback loops
* rubber-stamping
* unclear accountability
* reviewers without enough context

Meaningful oversight needs supporting system capabilities:

* validation
* logging
* monitoring
* retry logic
* anomaly detection
* risk scoring
* escalation rules
* contextual handoff
* traceability
* recovery mechanisms

The goal is not low automation with high human burden.

The goal is:

> High automation with high control.

This is difficult because control cannot depend only on humans manually checking everything. The system must automate low-risk checks, surface patterns, and escalate only when the situation matters.

---

## 5. Three Control Points for Human Oversight

Dr. Liu introduced a practical model with three control points.

### 5.1 May it act?

This is **decision oversight**.

Before the system takes an action, should it be allowed to proceed?

Relevant for:

* customer-facing outputs
* external communication
* high-risk recommendations
* irreversible actions
* regulated decisions
* tool calls with business impact

Example framing:

> Should the AI system be allowed to make or communicate this decision?

### 5.2 May it continue?

This is **execution oversight**.

Even if the system was allowed to start, should it continue after new signals, failures, or anomalies appear?

Relevant for:

* long-running workflows
* deployment rollouts
* multi-step agents
* automated operations
* systems with external side effects
* progressive releases

Example framing:

> Should the system continue executing after early warning signs?

### 5.3 May it change?

This is **update oversight**.

Should the system be allowed to adapt, learn, update memory, adjust behavior, or change future decisions?

Relevant for:

* personalization
* continual learning
* adaptive agents
* memory updates
* policy changes
* self-improving systems
* reinforcement from feedback

Example framing:

> Should this feedback become a system update?

---

## 6. Examples: Different Failures Need Different Control Points

Two examples helped make the control-point model concrete.

### Air Canada chatbot case

The Air Canada chatbot case illustrates a failure where the system created a customer-facing commitment.

The relevant control question:

> May it act?

The oversight problem is not only whether a human reviewed the output later. The issue is whether the system should have had authority to produce that kind of binding answer in the first place.

### CrowdStrike outage

The CrowdStrike outage illustrates a different kind of failure.

The relevant control question is less about the first action and more about continuation after early rollout signals.

The stronger control question:

> May it continue?

This points to execution oversight: canarying, monitoring, rollout gates, anomaly detection, and stop conditions.

### Key distinction

Not all failures are caught by the same oversight mechanism.

* Some failures require control before action.
* Some require control during execution.
* Some require control before adaptation or update.

This distinction was one of the most useful architectural takeaways from the session.

---

## 7. Demo: Human-Guided Continual Learning

**Speaker:** Michael Neumeier
**Topic:** Federated edge deployment and human-guided continual learning

Michael presented a fortiss demo around adaptive industrial robotics.

The demo involved:

* federated learning
* edge deployment
* spiking CNNs
* neuromorphic gesture interaction
* industrial welding context
* human-guided continual learning

The demo showed a system where learning happens close to the operator, while the operator remains involved in when and how the system adapts.

The broader architectural question was:

> How can adaptive systems learn from users without compromising safety, accountability, or human control?

This connected the robotics demo back to the broader agentic AI discussion.

The technical stack was robotics-specific, but the system design question maps directly to AI agents:

| Robotics demo                            | Agentic AI equivalent                               |
| ---------------------------------------- | --------------------------------------------------- |
| Robot adapts from operator gestures      | Agent adapts from user feedback                     |
| Federated learning on edge devices       | Local / distributed learning from sensitive context |
| Operator controls adaptation             | Human approval before memory / policy update        |
| Safety constraints around robot behavior | Guardrails around tool use and business actions     |
| Continual learning                       | Memory, personalization, skills, feedback loops     |
| Traceable adaptation                     | Auditable agent behavior changes                    |

The room engaged strongly with this demo because it made the abstract oversight discussion tangible.

---

## 8. World Café Challenge

The World Café became the core of the evening.

The challenge question:

> How can adaptive AI systems learn from humans without compromising safety, accountability, or human control?

Participants rotated across four tables. Each table focused on one design tension.

Table captains:

* Johannes
* Thomas
* Matthias
* Michael

The four tables were:

1. **Control & Consent**
   When is learning allowed?

2. **Safety Boundaries**
   What must never adapt automatically?

3. **Feedback & Correction**
   How does feedback become system improvement?

4. **Accountability & Traceability**
   Who can explain what changed and why?

Board photos are available under:

```text
challenge/
```

---

## 9. World Café Output

### 9.1 Feedback & Correction

**Table question:**
How does feedback become system improvement?

Captured themes:

* credibility of feedback
* systematic stakeholder engagement
* governance structure
* feedback classification and prioritization
* system prompts
* error / bug tracing
* validation rules and tests during development
* monitoring and follow-ups
* update deployment
* latency of feedback
* surprising feedback
* bias prevention
* notifications
* backpropagation / propagation of corrections

Core insight:

> Feedback does not improve the system just because it was collected.

For feedback to become system improvement, it needs:

* classification
* prioritization
* validation
* testing
* governance
* deployment process
* monitoring after deployment

A feedback loop is not complete until the system has a controlled way to decide whether feedback should change behavior.

### 9.2 Accountability & Traceability

**Table question:**
Who can explain what changed and why?

Captured themes:

* explainability
* provenance
* logs and interaction history
* agent IDs
* structured outputs
* input quality
* constraints and boundaries
* plans before execution
* metrics and system feedback
* monitoring
* notifications
* compliance as infrastructure
* human-in-the-loop for critical processes
* AI as a judge
* feedback loops as improvement
* versioning / true system state

Core insight:

> Traceability is not only about recording what happened.
> It is about being able to explain why something changed, who approved it, and whether it can be rolled back.

This table moved beyond logs toward the idea of provenance and structured execution records.

Important traceability questions:

* What input led to this output?
* Which agent or component acted?
* Which constraints were active?
* What plan was followed?
* What changed?
* Who approved it?
* What metrics were observed?
* Can the change be reversed?
* Can a human reconstruct the decision path?

### 9.3 Control & Consent

**Table question:**
When is learning allowed?

Captured themes:

* explicit consent
* only learn from information the user allows
* reinforcement learning from user feedback
* deterministic vs non-deterministic adjustment
* cost of deterministic control
* acceptable error thresholds
* balancing probability vs impact in operational risk
* evaluation against status quo before implementation
* non-critical environments
* observe → suggest → confirm → learn
* environment-dependent rules
* most systems need a harness to work

Core insight:

> Learning should be staged and consent-based.

One strong pattern emerged:

```text
Observe → Suggest → Confirm → Learn
```

This sequence avoids uncontrolled adaptation.

The system first observes behavior, then proposes a change, then asks for confirmation, and only then updates its future behavior.

This is highly relevant for both robotics and agent systems.

### 9.4 Safety Boundaries

**Table question:**
What must never adapt automatically?

Captured themes:

* compliance policies
* specific authorization
* zero-trust assumptions
* system prompts and guardrails
* things out of scope
* safety-critical behavior
* feature biases
* unlearning the wrong task
* impact measurement
* risk assessment
* ethics
* confidential information
* data access
* segregation of duties
* RAG control

Core insight:

> Before a system is allowed to learn, it needs clear non-adaptive boundaries.

Some parts of the system should not adapt automatically, even if feedback suggests they should.

Examples:

* compliance policies
* authorization rules
* safety-critical behavior
* confidential data access
* ethical constraints
* system-level guardrails
* segregation of duties
* out-of-scope behavior

Adaptive systems need fixed boundaries around the parts that must remain stable, controlled, or separately approved.

---

## 10. Cross-Table Synthesis

Across all four tables, a clear pattern emerged:

> Adaptive systems should not learn freely.

They need:

* consent
* hard safety boundaries
* structured feedback loops
* governance over updates
* traceability
* rollback
* human context
* escalation rules
* monitoring

The room did not argue for manual control everywhere. Instead, the stronger conclusion was:

> Human oversight must prevent both blind automation and human overload.

This is the central tension of collaboration design.

Too little human control creates unsafe autonomy.

Too much manual oversight creates bottlenecks, alert fatigue, and rubber-stamping.

The architecture has to decide where automation is safe, where humans are needed, and what context they require.

---

## 11. Main Takeaways

### 11.1 Oversight is architecture

Human oversight cannot be reduced to a final approval button.

It must be embedded across:

* decisions
* execution
* updates
* monitoring
* recovery
* feedback loops

### 11.2 Control points matter

The three questions are a useful design model:

```text
May it act?
May it continue?
May it change?
```

These map to different risk points and require different mechanisms.

### 11.3 Oversight needs automation

Human oversight does not mean manual review everywhere.

Good oversight architecture includes:

* automated validation
* sanity checks
* policy gates
* retries
* logging
* monitoring
* escalation
* stop conditions
* contextual handoff

### 11.4 Feedback needs governance

Feedback is not automatically learning.

Before feedback updates the system, it needs:

* credibility assessment
* prioritization
* validation
* testing
* approval
* deployment
* monitoring

### 11.5 Adaptation needs boundaries

Systems that learn continuously need rules for what must never adapt automatically.

This includes:

* safety-critical behavior
* compliance policies
* data access
* confidential information
* authorization rules
* out-of-scope behavior

### 11.6 Traceability requires provenance

Logs alone are not enough.

Production systems need to reconstruct:

* what happened
* why it happened
* what changed
* who approved it
* which constraints were active
* whether the change can be rolled back

---

## 12. Practical Design Pattern

A practical oversight pattern emerged from the evening:

```text
Low impact / expected failure:
    validate automatically
    retry if safe
    log

Recurring or accumulating failure:
    monitor
    summarize
    alert if pattern crosses threshold

High impact or critical step:
    stop
    provide context
    escalate to human

Potential system change:
    observe
    suggest
    confirm
    evaluate
    deploy
    monitor
```

This pattern captures the key idea:

> Human intervention should be risk-based, contextual, and designed into the system.

---

## 13. CAA Mapping

This module maps strongly to the Collaboration layer of the Cognitive Agentic Architecture, but it also connects across the full stack.

| CAA Layer     | Connection                                                      |
| ------------- | --------------------------------------------------------------- |
| Context       | Humans need the right evidence, not more information            |
| Behavior      | Systems need rules for when to act, stop, continue, or escalate |
| Execution     | Oversight during long-running workflows and tool use            |
| State         | Traceability, provenance, memory updates, rollback              |
| Collaboration | Human control, consent, approval, escalation, accountability    |
| Observability | Monitoring, logging, metrics, feedback signals                  |
| Governance    | Compliance, safety boundaries, responsibility                   |
| Learning      | Controlled adaptation and feedback-to-update loops              |

Core synthesis:

> Collaboration is not just a UI layer.
> It is the control interface between autonomous behavior and human responsibility.

---

## 14. What Worked Well

* The keynote gave a strong conceptual and architectural frame.
* The demo made adaptive learning tangible.
* The World Café format worked very well.
* The room was highly engaged.
* The table questions produced concrete patterns rather than generic discussion.
* The topic connected robotics, human-AI interaction, AI agents, and production AI architecture.
* More discussion time improved the format compared to talk-heavy sessions.

The strongest format decision was making the challenge the center of the evening.

---

## 15. What Could Be Improved

* More time for final synthesis would have helped.
* Some table outputs were strong but hard to capture fully from sticky notes.
* Table hosts should receive a slightly stricter capture template next time.
* It may help to give each table one explicit output format:

  * one design rule
  * one failure mode
  * one tradeoff
  * one unresolved question

Suggested template for future World Café sessions:

```text
Table:
Core question:
Design rule:
Failure mode:
Tradeoff:
Unresolved question:
```

---

## 16. Closing Conclusion

The strongest conclusion from the evening:

> Human oversight is not friction at the end of the process.
> It is a control architecture across the system.

The goal is not manual control everywhere.

The goal is:

> High automation with high control.

For adaptive AI systems, that means deciding:

* when the system may act
* when it may continue
* when it may change
* when it should retry
* when it should log
* when it should escalate
* when it should stop
* when feedback becomes a system update

Putting a human in the loop is easy.

Designing a loop that actually works is the hard part.

---

## 17. Thanks

Thank you to:

* **fortiss** for hosting the session
* **Dr. Yuanting Liu** for the keynote
* **Michael Neumeier** for the demo
* **Johannes, Thomas, Matthias, and Michael** for hosting the World Café tables
* all attendees for the strong discussion and engagement
