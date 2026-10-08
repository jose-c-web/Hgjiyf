# Sinnoh GBA — Phase45 Start Here

This file is the canonical handoff for continuing the project after Phase44.

## Current state

Phase44 converted Pearl event structures into GBA MapEvents for 204 reconstructed Sinnoh maps, but **did not convert Pearl script bytecode to Emerald/Quetzal bytecode**.

Phase45 must perform the real script conversion.

## Critical distinction

- Pearl NDS is the Sinnoh source/reference.
- The target is the GBA Quetzal/Emerald ROM.
- Never use Pearl bytecode directly in the GBA.

## Verified Phase44 ROM

Filename: `sinnoh_step44_events_converted.gba`
Size: 33,554,432 bytes
SHA-256: `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0`

Phase44 source/base SHA recorded in its statistics:
`1bde8c2356fc7deafed7741394e72882718d53b2f68cffcf77afb805d5eb36f3`

## Pearl script source

Required NARC:
`fielddata/script/scr_seq_release.narc`
SHA-256:
`c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7`

Required event NARC:
`fielddata/eventdata/zone_event_release.narc`
SHA-256:
`3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4`

The D/P command database is maintained upstream at:
https://github.com/DS-Pokemon-Rom-Editor/scrcmd-database
and the v2 database is:
https://github.com/DS-Pokemon-Rom-Editor/scrcmd-database/blob/main/diamond_pearl_v2.json

## Phase44 package

`sinnoh-reconstruction-phase44.zip`
Size: 14,532,507 bytes
SHA-256:
`78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c`

The package contains:
- sinnoh_step44_events_converted.gba
- phase44_statistics.json
- phase44_warp_fallbacks.json
- PHASE44_REPORT.md

## Important artifact-access note

The large Phase44 ROM/ZIP and Pearl NARCs were available in the working environment used to create this handoff, but the GitHub connector available to the assistant does not provide a direct binary/release upload operation. The persistent Library also rejected new uploads because its storage quota is full.

Therefore this repository deliberately records the **verified hashes and exact artifact requirements**, but does not falsely claim that the large binaries are stored in GitHub.

A new chat must not substitute an earlier ROM merely because these binaries are absent from the repository. If the binaries are not accessible through the conversation/Library, stop before Phase45 ROM modification.

## Phase45 first actions

1. Read `SINNOH_CONTINUITY_PHASE44.md`.
2. Read `PROMPT_PROXIMO_CHAT_SINNOH_SCRIPTS.md`.
3. Validate the Phase44 ROM against the SHA above.
4. Obtain the exact Pearl script/event NARCs.
5. Obtain `diamond_pearl_v2.json`.
6. Inventory the commands actually used by the 204 maps.
7. Discover the real Quetzal/Emerald script ABI.
8. Build D/P → GBA command mappings.
9. Pilot Twinleaf, Route201, Sandgem, Jubilife, Oreburgh.
10. Only after validation, expand to all 204 maps.

Do not call Phase45 complete unless a real ROM has been generated and validated.
