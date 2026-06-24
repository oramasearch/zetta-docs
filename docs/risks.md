# Risks

Gating risks and the decisions/controls that mitigate them.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Risks

### RSK-1 — Orama Zetta maturity is the gating risk  {: #rsk-1 }

`draft`  ·  `risk`  ·  issue [#200](https://github.com/oramasearch/zetta/issues/200)

DDF API, embedded Lua, tiered storage, indexing, cloud deploy, auth are all unbuilt.

Verified against the code: Orama Zetta today is a CRDT-replicated JSON store + equal-peer cluster + Postgres-SQL subset. Most of the substrate this product promises does not exist yet. **Mitigation:** R1 runs on what exists; co-own the Orama Zetta roadmap; sequence the engine bets explicitly.

**Realizes / depends on / relates to:** affects → [`FEAT-7`](backlog.md#feat-7) · affects → [`FEAT-8`](backlog.md#feat-8)
**Referenced by:** [`ADR-8`](architecture.md#adr-8) mitigates · [`STK-3`](personas.md#stk-3) relates to

### RSK-2 — Generated-graph correctness  {: #rsk-2 }

`draft`  ·  `risk`  ·  issue [#201](https://github.com/oramasearch/zetta/issues/201)

Self-service that ships confidently-wrong pipelines is worse than the bottleneck.

Guaranteeing a generated graph is 'robust, correct, professionally architected' is hard. **Mitigation:** the correctness gate (schema/leakage/point-in-time + a correctness eval) must block deploy; set a correctness floor before shipping self-service to non-engineers.

**Realizes / depends on / relates to:** affects → [`FEAT-6`](backlog.md#feat-6)
**Referenced by:** [`ADR-3`](architecture.md#adr-3) mitigates

### RSK-3 — Control-plane on CRDT without transactions/leadership  {: #rsk-3 }

`draft`  ·  `risk`  ·  issue [#202](https://github.com/oramasearch/zetta/issues/202)

Orama Zetta lacks transactions + leader election; trusting it with registry/locks/cursors is unproven.

Storing control-plane state (registry, run cursors, locks) in Orama Zetta's CRDT store is unproven until leadership-by-lease lands. **Mitigation:** validate the CRDT store for control-plane use in R1 on low-contention state; gate locks/cursors on the planned leadership feature.

**Realizes / depends on / relates to:** relates to → [`ADR-1`](architecture.md#adr-1)

### RSK-4 — Cloud-provisioning surface area  {: #rsk-4 }

`draft`  ·  `risk`  ·  issue [#203](https://github.com/oramasearch/zetta/issues/203)

k8s × AWS × Azure × GCP × on-prem × governance is enormous.

Over-reaching on the deploy matrix sinks the timeline. **Mitigation:** R1 ships local; add one real target at a time (start k8s, then on-prem VM); resist the full matrix.

**Realizes / depends on / relates to:** affects → [`FEAT-4`](backlog.md#feat-4)
**Referenced by:** [`ADR-7`](architecture.md#adr-7) mitigates

### RSK-5 — Scope vs. orama-platform-1  {: #rsk-5 }

`draft`  ·  `risk`  ·  issue [#204](https://github.com/oramasearch/zetta/issues/204)

Duplicating or contradicting the earlier plan wastes effort.

The relationship to the existing orama-platform repo needs an explicit decision (merge vs. distinct). **Mitigation:** treat it as prior art, borrow ideas, and make the merge/distinct call early.

**Referenced by:** [`ADR-9`](architecture.md#adr-9) relates to

### RSK-6 — Unvalidated cost-savings claim  {: #rsk-6 }

`draft`  ·  `risk`  ·  issue [#205](https://github.com/oramasearch/zetta/issues/205)

The ~60% vs. incumbents figure is a hypothesis, not a measured result.

The cost-reduction figure from zetta-business is unvalidated. **Mitigation:** do not state as fact externally; instrument actual local-vs-source query cost once tiered storage lands and report measured deltas.

**Realizes / depends on / relates to:** relates to → [`FEAT-7`](backlog.md#feat-7)

### RSK-7 — Arbitrary extension/runner code executing near customer data  {: #rsk-7 }

`draft`  ·  `risk`  ·  issue [#206](https://github.com/oramasearch/zetta/issues/206)

Lua/Orly (and later Python) extensions run on nodes next to data; a sandbox escape or over-broad grant = data exfiltration or tampering.

The extensibility model runs arbitrary code on nodes holding customer data. **Threat:** sandbox escape, capability over-grant, or egress would breach the 'no data leaves' promise. **Mitigation:** ADR-12 — capability-scoped deny-by-default sandbox, no fs/network egress by default, full audit, and approval gates for shared/enterprise-published extensions. Feeds the security-domain threat model.

**Realizes / depends on / relates to:** affects → [`FEAT-8`](backlog.md#feat-8)
**Referenced by:** [`ADR-12`](architecture.md#adr-12) mitigates · [`THR-1`](security.md#thr-1) relates to

### RSK-8 — Native reimplementation correctness + maintenance burden  {: #rsk-8 }

`draft`  ·  `risk`  ·  issue [#207](https://github.com/oramasearch/zetta/issues/207)

Re-implementing ML/DDF algorithms in C++/CUDA risks numerical divergence from reference implementations and ongoing maintenance load.

Re-implementing training/inference/DDF algorithms natively can subtly diverge from reference implementations (numerical correctness, edge cases) and carries a maintenance burden as algorithms evolve. **Mitigation:** the correctness gate (ADR-3) and a verification suite (TP-1) comparing native outputs to reference results on known cases; scope native reimplementation to the algorithms that matter; treat Claude-Code-assisted ports as code that still must pass verification.

**Realizes / depends on / relates to:** affects → [`FEAT-6`](backlog.md#feat-6)
**Referenced by:** [`ADR-3`](architecture.md#adr-3) mitigates

### RSK-9 — Ephemeral burst at scale: bulk identity, Spot eviction, orphaned-node cost  {: #rsk-9 }

`draft`  ·  `risk`  ·  issue [#208](https://github.com/oramasearch/zetta/issues/208)

Provisioning 20+ ephemeral nodes at once strains identity issuance/revocation, exposes Spot-eviction failures mid-job, and risks orphaned nodes running up cost.

Bursting many nodes raises three concerns: (1) **bulk identity** — minting + revoking N distinct short-lived node identities/capability tokens efficiently and without sprawl (open question on ADR-20/ADR-18); (2) **Spot/low-priority eviction** mid-training — jobs must tolerate node loss (checkpoint/restart); (3) **orphaned nodes** — a crashed orchestrator could leave paid nodes running. **Mitigation:** batch enrollment with TTL'd identities revoked on teardown; eviction-tolerant cluster-parallel jobs; a reconcile/reaper that reclaims nodes with no live owner; cost caps per burst.

**Realizes / depends on / relates to:** affects → [`FEAT-6`](backlog.md#feat-6) · relates to → [`ADR-18`](architecture.md#adr-18) · relates to → [`ADR-20`](architecture.md#adr-20)
**Referenced by:** [`RULE-5`](backlog.md#rule-5) relates to
