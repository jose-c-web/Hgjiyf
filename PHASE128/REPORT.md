# Phase 128 — Sinnoh map/event normalization for GBA conversion

## Scope
This phase converts the extracted RPG Maker Ruby Marshal objects into a normalized intermediate representation suitable for a future Quetzal/Emerald importer. It does not claim that these maps are already encoded into the GBA ROM.

## Completed
- Parsed **138/138** Sinnoh map source files without failures.
- Normalized **893,610** 16-bit map-layer cells while retaining source layer order and table dimensions.
- Extracted **2,048** event objects, **3,648** event pages, and **28,324** event commands, preserving event conditions and command parameters in JSON.
- Extracted **1,023** transfer-player commands (RPG Maker code 201) into a transfer graph.
- Produced per-map dimensions/tileset inventory and command-code counts.
- Kept the Quetzal ROM unchanged; SHA-256: `9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f`.

## Artifacts
- `MAP_CONVERSION_INVENTORY.csv`: dimensions and event density for every map.
- `TRANSFER_GRAPH.csv`: source map/event and transfer target details.
- `EVENT_COMMANDS_RELEVANT.csv`: commands requiring mapping to target scripts/events.
- `COMMAND_CODE_COUNTS.csv`: frequency of source command codes.
- `CONVERSION_READINESS.json`: scope counts and explicit conversion blockers.
- Downloadable package contains normalized JSON for all 138 maps and their tile-layer data.

## Remaining before playable ROM
1. Convert source tileset graphics, palettes, autotiles, terrain tags and tile IDs into Quetzal metatiles.
2. Map source map IDs to new Quetzal map group/map numbers without overwriting existing regions.
3. Translate RPG Maker event commands and conditions into Quetzal/Emerald script bytecode and object/warp/background events. Custom source commands (including codes 509 and 412) must be explicitly translated or redesigned, not silently dropped.
4. Register layouts, map headers, event tables and connections in ROM-safe space after references are verified.
5. Validate warps, collision, NPC behavior, item pickup, battles and story flags; run emulator smoke tests.

## Safety and compatibility
Source tileset IDs and tile IDs are not Quetzal metatile IDs. Some transfer targets are outside the 138-map Sinnoh subset and need resolution against the full source catalog. The normalized package is conversion input, not a drop-in GBA asset. No ROM patch was made because writing unverified pointers could corrupt the existing regions.