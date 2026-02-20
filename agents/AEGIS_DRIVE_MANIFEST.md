# Aegis Google Drive — Repo Snapshot Manifest

**Prepared by:** Anvil (BS Buddy)
**Date:** 2026-02-20 09:30 CST
**Purpose:** Define what gets pushed to Aegis's Google Drive and what gets excluded. Goal: give Aegis full codebase access without burying him in 72GB of venvs and model weights.

---

## Total Repo: 72GB

### EXCLUDE (71.5GB+ of noise)

| Directory | Size | Reason |
|-----------|------|--------|
| `.venvs/` | 12 GB | Python virtual environments (fish_speech, etc.) |
| `.git/` | 14 GB | Git history and objects |
| `.cache/` | 16 GB | Build/runtime cache |
| `models/` | 31 GB | ML model weights (fish_speech, etc.) |
| `client/node_modules/` | ~70 MB | NPM dependencies |
| `client/dist/` | varies | Build output |
| `**/__pycache__/` | varies | Python bytecode cache |
| `*.bak*`, `*.backup` | varies | Backup files |
| `output/` | 33 MB | Runtime output (logs, generated audio) |
| `image_cache/` | 2 MB | Cached generated images |
| `runtime_logs/` | 45 KB | Runtime log files |
| `credentials.json` | — | **SENSITIVE** — never push credentials |
| `nul` | — | Artifact (empty Windows NUL file) |
| `srd_fixture_temp.json` | — | Temp fixture |
| `playtest_log.jsonl` | — | Runtime playtest data |
| `trust_findings_raw.txt` | — | Temporary analysis output |
| `f:DnD-3.5docsresearch/` | 0 | Empty artifact directory |

### INCLUDE — Tier 1: Architecture (what Aegis needs most)

**Source code — `aidm/` (8.5 MB, 242 files, ~85K lines)**

| Subdirectory | Files | Purpose |
|-------------|-------|---------|
| `aidm/core/` | ~70 files | **BOX** — deterministic engine, geometry, combat, state, RNG, events |
| `aidm/lens/` | ~12 files | **LENS** — narrative briefs, context assembly, discovery log, scene management |
| `aidm/oracle/` | ~9 files | **ORACLE** — canonical state, facts ledger, compaction, story state |
| `aidm/spark/` | ~5 files | **SPARK** — LLM adapter, grammar shield, model registry |
| `aidm/narration/` | ~7 files | Narration service, play loop adapter, LLM query interface |
| `aidm/immersion/` | ~19 files | TTS, STT, image gen, emotion routing, voice intent |
| `aidm/interaction/` | ~2 files | Intent bridge |
| `aidm/runtime/` | ~8 files | Bootstrap, session, play controller, IPC |
| `aidm/server/` | ~3 files | WebSocket bridge, app entry |
| `aidm/services/` | ~5 files | Asset pools, discovery log, job queue |
| `aidm/schemas/` | ~60+ files | All Pydantic schemas — the project's type system |
| `aidm/data/` | ~8 files | Content packs (creatures, spells, feats, equipment), policy defaults |
| `aidm/rules/` | ~2 files | Legality checker |
| `aidm/evaluation/` | ~2 files | Evaluation harness |
| `aidm/testing/` | ~4 files | Performance profiler, property testing, replay regression |
| `aidm/ui/` | ~6 files | Camera, character sheet, table objects, zones |
| `aidm/examples/` | varies | Example scripts |

**Tests — `tests/` (20 MB, 232 files, ~113K lines)**
- 3302+ tests, all green at last count
- Full coverage of Box, Lens, Oracle, Spark, Immersion, Runtime
- Include entire directory

### INCLUDE — Tier 2: Governance & Doctrine

| File/Directory | Size | Purpose |
|---------------|------|---------|
| `docs/doctrine/` | ~3 files | SPARK_LENS_BOX_DOCTRINE, DEFINITIONS, SWAPPABLE_INVARIANT |
| `docs/contracts/` | ~6 files | CLI_GRAMMAR, INTENT_BRIDGE, WORLD_COMPILER, UNKNOWN_HANDLING, schemas |
| `docs/planning/` | ~15 files | Execution plans, master requirements, research questions |
| `docs/work_orders/` | ~4 files | WO-057 through WO-060 (active) |
| `docs/governance/` | varies | Governance layer docs |
| `docs/milestones/` | varies | Milestone definitions |
| `docs/specs/` | varies | Technical specifications |
| `docs/schemas/` | varies | Schema documentation |
| `pm_inbox/` | 11 MB | PM briefing, rehydration kernel, burst queue, doctrine, memos |
| `config/` | ~468 KB | models.yaml, user_profile.yaml, REUSE_DECISION.json |
| `pyproject.toml` | — | Project configuration |
| `requirements.txt` | — | Python dependencies list |

### INCLUDE — Tier 3: Context & Reference

| File/Directory | Size | Purpose |
|---------------|------|---------|
| Top-level `.md` files | varies | MANIFESTO, PROJECT_COMPASS, PROJECT_STATE_DIGEST, BUILDER_FIELD_MANUAL, etc. |
| `docs/THESIS_BUBBLE_REALM_AND_THE_TABLE.md` | — | The thesis — Aegis was there when it was written |
| `docs/CP*.md` (decision docs) | varies | All CP decision records (CP001–CP21) |
| `methodology/` | 84 KB | Case studies, patterns, templates |
| `artifacts/` | 51 KB | Demo campaign, vertical slice transcript |
| `scripts/` | 742 KB | Utility scripts (listen.py, grammar checks, etc.) |
| `tools/` | 581 KB | Data extraction tools |
| `examples/` | 8 KB | Example usage |
| `play.py` | — | Main entry point |
| `demo_*.py` | — | Demo scripts |

### INCLUDE — Tier 4: Reference Data (optional, large)

| File/Directory | Size | Decision |
|---------------|------|----------|
| `sources/text/` | 7.2 MB | SRD text extractions — useful for Aegis to cross-reference rules |
| `sources/meta/` | 967 KB | Source metadata JSONs |
| `Vault/` (excl. 00-System) | ~1 MB | Obsidian vault markdown — D&D rules, conditions, MOCs |
| `Vault/00-System/` | 56 MB | Databases (.db), compiler JSON, indexes — **EXCLUDE databases, INCLUDE markdown only** |
| `inbox/` | 204 KB | Original design documents (.docx) — reference only |
| `client/src/` | varies | Frontend TypeScript source — include if Aegis will review UI |
| `client/index.html` | — | Frontend entry |
| `client/package.json` | — | Frontend dependencies |

### INCLUDE — Tier 5: Aegis-Specific Context

| File | Purpose |
|------|---------|
| `docs/aegis_shield_emblem.png` | His emblem — he made it |
| `pm_inbox/REHYDRATION_KERNEL_LATEST.md` | Slate's kernel — project continuity |
| `pm_inbox/PM_BRIEFING_CURRENT.md` | Current PM briefing |
| `pm_inbox/doctrine/` | PM-layer doctrine files |

---

## Estimated Drive Footprint

| Tier | Size |
|------|------|
| Tier 1 (source + tests) | ~29 MB |
| Tier 2 (governance) | ~12 MB |
| Tier 3 (context) | ~2 MB |
| Tier 4 (reference, selective) | ~9 MB |
| Tier 5 (Aegis-specific) | ~1 MB |
| **Total** | **~53 MB** |

Without Tier 4: ~43 MB. With everything including Vault markdown: ~53 MB. Either way, under 100 MB — trivial for Google Drive.

---

## Sync Strategy

**Initial push:** Full snapshot of Tiers 1-3 + Tier 5. Tier 4 at Thunder's discretion.

**Ongoing sync:** After each significant commit or WO completion, push updated files. The key directories to keep fresh:
- `aidm/` — source changes
- `tests/` — test changes
- `pm_inbox/` — PM briefing and kernel updates
- `docs/` — doctrine and contract changes
- `config/` — model and policy changes

**What NOT to sync:** Never push `.venvs`, `.git`, `.cache`, `models/`, `__pycache__`, `credentials.json`, `node_modules/`.

---

## Rsync Command (when ready)

```bash
rsync -av --progress \
  --exclude='.venvs' \
  --exclude='.git' \
  --exclude='.cache' \
  --exclude='models' \
  --exclude='__pycache__' \
  --exclude='node_modules' \
  --exclude='dist' \
  --exclude='*.bak*' \
  --exclude='*.backup' \
  --exclude='output' \
  --exclude='image_cache' \
  --exclude='runtime_logs' \
  --exclude='credentials.json' \
  --exclude='nul' \
  --exclude='srd_fixture_temp.json' \
  --exclude='playtest_log.jsonl' \
  --exclude='trust_findings_raw.txt' \
  --exclude='*.db' \
  --exclude='Vault/00-System/Compiler' \
  --exclude='Vault/00-System/Indexes' \
  f:/DnD-3.5/ /path/to/google-drive-sync/DnD-3.5/
```

Alternative: a Python script that copies with the same exclusions, for Windows compatibility.

---

*09:30 CST, 2026-02-20. Manifest complete. Awaiting Thunder's return for Drive path and push authorization.*
