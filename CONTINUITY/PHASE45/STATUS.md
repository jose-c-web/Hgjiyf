# Phase 45 — Script conversion handoff

Status: READY_FOR_SCRIPT_CONVERSION

The exact Phase 44 ROM is `sinnoh_step44_events_converted.gba`.
SHA-256: `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0`

Phase 44:
- 204 maps
- 813 object events
- 380 warp events
- 31 coord/trigger events
- 813 Pearl script IDs preserved as metadata
- execution safely disabled with an Emerald `end` stub
- warp fix preserved

Next task: recover/verify the exact Pearl `scr_seq_release.narc` and `zone_event_release.narc`, retrieve the D/P command database, audit the 813 script references, build a real D/P → Emerald/Quetzal script compiler, and only then produce a verified Phase 45 ROM.

Critical rule: never substitute Phase 43, Step 21, or another ROM for Phase 44 and never invent missing script data.
