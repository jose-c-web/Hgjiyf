# Phase 44/45 artifact recovery

The exact Phase44 inputs have been recovered and verified in the working environment.

## Verified artifacts

| Artifact | Size | SHA-256 | Role |
|---|---:|---|---|
| sinnoh_step44_events_converted.gba | 33,554,432 | 9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0 | Phase45 ROM input |
| sinnoh-reconstruction-phase44.zip | 14,532,507 | 78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c | Recovery package |
| scr_seq_release.narc | 219,608 | c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7 | Gen4 script source |
| zone_event_release.narc | 140,020 | 3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4 | Gen4 event source |
| PK P3ar1 (PT-BR).nds | 61,105,608 | 03455137ff59c27e192355153e66007f60a2566bbb6e3ce59b6d2a0101c8880c | Source container |

## Phase44 package contents

The recovery ZIP contains the exact Phase44 ROM plus:

- `PHASE44_REPORT.md`
- `phase44_statistics.json`
- `phase44_warp_fallbacks.json`

The ROM reports 204 maps, 813 object events, 380 warp events and 31 coordinate/trigger events. Pearl script IDs were preserved as metadata; Gen4 bytecode was not executed directly on GBA.

## Phase45 rule

Use the exact SHA-256 inputs above. Do not substitute an earlier ROM, do not rebuild Phase44, and do not fabricate a script inventory.

## Distribution note

The repository stores continuity metadata and cryptographic fingerprints only. The ROM/NDS/NARC binaries are not published here because they contain copyrighted game assets. Keep the verified binaries in the private working environment and compare their hashes against this manifest before Phase45 conversion.
