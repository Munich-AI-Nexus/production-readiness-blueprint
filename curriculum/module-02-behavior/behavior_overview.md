# Module 2: Behavior – Explicit, Inspectable Planning

## Overview
Modern agent failures are rarely about model quality.
They are about opaque reasoning, uncontrolled execution, and missing decision traces.

This module examines planning as a first-class system concern:
plans as artifacts, policies as code, and execution as a controlled process.

## Goals
- Understand planner–actor separation and why it matters in production
- Learn techniques for auditable, debuggable decision-making
- Design deterministic or policy-bounded behavior for complex workflows
- Reduce drift, hallucination, and unsafe tool execution

## Key Questions
- Why does black-box reasoning break under scale and concurrency?
- How can planning be explicit, testable, and replayable?
- What patterns make agent decision-making predictable instead of magical?
- Where should autonomy be constrained to increase reliability?

## Topics
- Planner–actor separation (reasoning vs execution)
- Explicit plans, specs, and decision artifacts
- Decision trees, policy engines, and rule-augmented planners
- Dynamic planning with bounded autonomy (replanning without chaos)
- Testing and debugging planners (traceability, invariants, validators)

## Related Layers
- CAA Layer: Behavior
- Cross-Cutting: Observability, Traceability, Governance

## Resources (Starter)
These are not “nice to read.” They are signals from teams shipping real systems.

- Microsoft – AI Agent Design Patterns
Manager / Magentic patterns, planner–executor separation, and orchestration tradeoffs
https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns

- Dropbox – Context Engineering for Smarter AI
Empirical evidence that unbounded context and tools degrade reasoning; supports explicit planning and scoped context
https://dropbox.tech/machine-learning/how-dash-uses-context-engineering-for-smarter-ai

- Architect–Builder Pattern (Waleed Kadous)
Spec-driven, parallel execution with a single planner/integrator — a production-safe Magentic variant
https://waleedk.medium.com/the-architect-builder-pattern-scaling-ai-development-with-spec-driven-teams-d3f094b8bdd0

- Cognitive Agentic Architecture (CAA)
Design principles for explicit behavior, state, execution control, and observability
https://github.com/artiquare/cognitive-agentic-architecture
