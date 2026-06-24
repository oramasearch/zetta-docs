# Orama Zetta

> ## Intelligence Velocity for Big Thinkers.

**Orama Zetta** is a desktop GUI control plane for the **ZettaDB** engine that turns a plain-language problem — or an artifact you already have, like an n8n workflow — into a correct, professionally-architected data + AI **execution graph**, then deploys ZettaDB nodes and the workflows onto infrastructure you control and runs them. *The data engineer, the AI engineer, and the platform engineer — in a bottle.*

This site is the **design blueprint** for Orama Zetta. It is generated from the worktree-manager blueprint (`ORAMA-ZETTA`) and kept in sync with the GitHub issues on [`oramasearch/zetta`](https://github.com/oramasearch/zetta) — see [README](https://github.com/oramasearch/zetta-docs) for how.

## Read it in this order

| Section | What's there |
|---|---|
| [Strategy](strategy.md) | Vision, goals, KPIs, assumptions, scope |
| [Personas & Stakeholders](personas.md) | Charles, Dana, Sam, the Agent; the buyers |
| [Requirements](requirements.md) | Business / stakeholder / functional / non-functional / integration / data / transition |
| [Architecture](architecture.md) | The ADRs (the decisions), architecture elements, quality scenarios |
| [Domain Model](domain-model.md) | Six bounded contexts → entities, commands, events |
| [Data & Storage](data.md) | Control-plane store, tables, tiered storage, retention |
| [APIs](apis.md) | Native cluster API, DDF, Runner, Cloud Interface, MCP, CLI |
| [Security](security.md) | Threat model, trust boundaries, controls, permission rules |
| [UX](ux.md) | Screens, journeys, components |
| [Delivery](delivery.md) | Releases R1→R8, environments, runbooks |
| [Backlog](backlog.md) | Features, user stories, use cases, business rules |
| [Testing](testing.md) | Test plan + test cases |
| [Risks](risks.md) | Gating risks + mitigations |
| [Glossary](glossary.md) | Load-bearing terms |
| [Diagrams](diagrams.md) | Architecture + traceability (Graphviz) |

## The thesis in four lines

- **It learns from your data** — trains a model on *your* data (native, cluster-parallel), not inference over a rented one.
- **Correct by construction** — every generated graph is validated before it can deploy.
- **ZettaDB underneath** — data lives where it sits; compute runs next to it; storage tiers hot→cold→re-warm.
- **Governed self-service** — in your firewall, identity-scoped, audited.

---

!!! note "Generated content"
    Every page below this landing is generated from the wtm blueprint by the `zetta-sync` skill. Don't hand-edit — re-run the sync.
