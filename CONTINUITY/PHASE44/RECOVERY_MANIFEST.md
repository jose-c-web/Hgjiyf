# Phase 44 recovery manifest

## Exact artifacts verified in the execution environment

| Artifact | Size | SHA-256 |
|---|---:|---|
| sinnoh_step44_events_converted.gba | 33,554,432 | 9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0 |
| sinnoh-reconstruction-phase44.zip | 14,532,507 | 78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c |

The ZIP contains exactly:
- sinnoh_step44_events_converted.gba
- phase44_statistics.json
- phase44_warp_fallbacks.json
- PHASE44_REPORT.md

## Important distinction

These binaries existed and were validated in the execution environment that produced the handoff. They were not originally persisted to GitHub. This manifest records their exact identity and prevents a later chat from silently substituting an earlier phase.

## Integrity rule

Any recovered Phase 44 ROM must be SHA-256 checked against the value above before use.
