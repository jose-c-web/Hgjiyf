# Sinnoh GBA — Continuity Phase 45

## Estado

Phase 1–44 permanece concluída conforme os handoffs anteriores. Nenhuma fase anterior deve ser refeita.

A Phase44 foi **recuperada e verificada** no ambiente de trabalho. O bloqueio de disponibilidade dos binários foi resolvido.

### Inputs exatos da Phase45

- ROM: `sinnoh_step44_events_converted.gba`
  - size: 33,554,432 bytes
  - SHA-256: `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0`
- Package: `sinnoh-reconstruction-phase44.zip`
  - size: 14,532,507 bytes
  - SHA-256: `78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c`
- Pearl script NARC:
  - `fielddata/script/scr_seq_release.narc`
  - size: 219,608 bytes
  - SHA-256: `c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7`
- Pearl event NARC:
  - `fielddata/eventdata/zone_event_release.narc`
  - size: 140,020 bytes
  - SHA-256: `3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4`

The source Pearl NDS from which those NARCs were extracted is also verified:
- `PK P3ar1 (PT-BR).nds`
- 61,105,608 bytes
- SHA-256: `03455137ff59c27e192355153e66007f60a2566bbb6e3ce59b6d2a0101c8880c`

## Phase44 facts

- maps: 204
- ObjectEventTemplate: 813
- WarpEvent: 380
- Coord/trigger events: 31
- scripts preserved as metadata: 813
- script execution: disabled safely with GBA end stub
- warp fix preserved
- script arena: `0x1FE3000..0x1FE96CC`

## Phase45 objective

Convert Pearl/Gen4 script bytecode into executable Quetzal/Emerald-compatible GBA scripts while preserving the Phase44 map/event structures.

Required approach:

1. Audit the exact `scr_seq_release.narc`.
2. Build a complete D/P script command inventory and command decoder.
3. Map commands to the actual Quetzal/Emerald script ABI in the Phase44 ROM.
4. Resolve message/text IDs, movement commands, conditionals, variables/flags, trainer battles, item/give commands, warps and calls.
5. Generate converted script bytecode in unused ROM space.
6. Patch script pointers/MapScripts/ObjectEvent script references safely.
7. Validate every converted script statically before ROM execution.
8. Preserve all Phase44 event/warp data and the warp-engine fix.
9. Do not use Phase43, Step21 or a generic replacement ROM as the Phase45 base.

## Distribution policy

The repository contains manifests, reports and hashes. The ROM/NDS/NARC binaries are intentionally not committed publicly because they contain copyrighted game assets. The exact binaries must be supplied from the private working environment and verified against `PHASE45_INPUT_MANIFEST.json` before conversion.

See:
- `PHASE45/PHASE45_INPUT_MANIFEST.json`
- `PHASE45/PHASE44_SHA256.txt`
- `PHASE45/README.md`
