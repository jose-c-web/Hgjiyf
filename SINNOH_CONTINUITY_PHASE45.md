# Sinnoh GBA — Continuity Phase 45

## Estado atual

Phase 1–44 permanece concluída. **Nenhuma fase anterior deve ser refeita.**

A documentação e os SHA-256 exatos da Phase44/Pearl foram preservados no GitHub, porém os **bytes dos binários não estão atualmente acessíveis nesta execução** e não estão publicados no repositório.

Portanto o estado correto é:

**Phase45 = BLOCKED_PENDING_BINARY_RECOVERY**

Isso é um bloqueio de acesso aos artefatos, não um problema de engenharia das fases anteriores.

## Inputs exatos

- `sinnoh_step44_events_converted.gba`
  - 33,554,432 bytes
  - SHA-256: `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0`
- `sinnoh-reconstruction-phase44.zip`
  - 14,532,507 bytes
  - SHA-256: `78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c`
- `fielddata/script/scr_seq_release.narc`
  - 219,608 bytes
  - SHA-256: `c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7`
- `fielddata/eventdata/zone_event_release.narc`
  - 140,020 bytes
  - SHA-256: `3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4`
- `PK P3ar1 (PT-BR).nds`
  - 61,105,608 bytes
  - SHA-256: `03455137ff59c27e192355153e66007f60a2566bbb6e3ce59b6d2a0101c8880c`

## Phase44 facts

- maps: 204
- ObjectEventTemplate: 813
- WarpEvent: 380
- Coord/trigger events: 31
- scripts preserved as metadata: 813
- script execution: safely disabled with GBA end stub
- warp fix preserved
- script arena: `0x1FE3000..0x1FE96CC`

## What was checked now

GitHub was searched for the exact names of the Phase44 ROM, Phase44 ZIP and both required NARCs. No binary matches were found.

The hashes remain useful and authoritative for verification **after recovery**, but cannot reconstruct missing bytes.

## Phase45 objective

Once the exact bytes are recovered:

1. Verify the Phase44 ROM/package SHA-256.
2. Verify the exact Pearl script/event NARCs.
3. Audit `scr_seq_release.narc`.
4. Build the complete D/P command inventory and decoder.
5. Map commands to the actual Quetzal/Emerald ABI in the verified Phase44 ROM.
6. Convert scripts into executable GBA bytecode.
7. Patch script pointers safely.
8. Statically validate every converted script.
9. Preserve Phase44 events, warps and the warp-engine fix.
10. Runtime-test only after static validation.

## Non-negotiable rules

- Do not redo phases 1–44.
- Do not substitute Phase43 or Step21.
- Do not invent a script inventory.
- Do not use an unverified Phase45 ROM as the base.
- Do not claim runtime success without emulator testing.
- Do not claim binary recovery until the actual bytes pass the recorded SHA-256 checks.

See `PHASE45/PHASE45_INPUT_MANIFEST.json` and `PHASE45/README.md`.
