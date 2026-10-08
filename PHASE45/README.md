# Phase 44/45 artifact recovery

## Current verified state

The repository contains the exact cryptographic fingerprints from the prior verified Phase44 handoff, but the binary bytes are **not currently present in this execution environment** and are **not committed to this public repository**.

Therefore Phase45 is **BLOCKED_PENDING_BINARY_RECOVERY**. This is intentional: a SHA-256 recorded in a handoff is not sufficient to reconstruct a missing ROM or NARC.

## Exact inputs that must be recovered

| Artifact | Size | SHA-256 | Required |
|---|---:|---|---|
| sinnoh_step44_events_converted.gba | 33,554,432 | 9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0 | Yes |
| sinnoh-reconstruction-phase44.zip | 14,532,507 | 78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c | Preferred recovery package |
| fielddata/script/scr_seq_release.narc | 219,608 | c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7 | Yes |
| fielddata/eventdata/zone_event_release.narc | 140,020 | 3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4 | Yes |
| PK P3ar1 (PT-BR).nds | 61,105,608 | 03455137ff59c27e192355153e66007f60a2566bbb6e3ce59b6d2a0101c8880c | Optional if the two NARCs are recovered separately |

## What has been established

- Phase 1–44 must not be redone.
- Phase44 remains the only valid base for Phase45.
- The hashes above are preserved from the prior verified handoff.
- GitHub searches for the exact ROM, ZIP and NARC filenames returned no binary matches.
- No binary upload/release is being claimed here.
- Existing unverified Phase45 outputs must not be used as a substitute.

## Fastest recovery path

1. Recover/upload the original `sinnoh-reconstruction-phase44.zip` from the previous execution/environment.
2. Verify its SHA-256 against `78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c`.
3. Extract and verify `sinnoh_step44_events_converted.gba` against `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0`.
4. Recover the two Pearl NARCs, or the verified Pearl source, and verify their hashes.
5. Only then start the real Phase45 script audit/conversion.

## Phase45 engineering target

Convert Pearl/Gen4 scripts into executable Quetzal/Emerald-compatible GBA scripts while preserving all Phase44 map/event/warp structures and the corrected warp-engine behavior.

Do not fabricate an inventory and do not substitute an earlier ROM.
