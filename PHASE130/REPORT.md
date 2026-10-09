# Phase 130 — bulk source-map conversion preparation

## Verified output
- Processed 138 source Sinnoh maps.
- Exported 893,610 layer cells as little-endian uint16 data with per-map metadata.
- Generated source tile usage/behavior table with 3,468 rows, crossing usage with source passages, priorities, and terrain tags.
- Exported 28,324 event command rows for explicit destination translation.
- Created a provisional registry for 138 maps, explicitly marked as not yet safe/final for ROM registration.
- Packaged the map layers, CSVs, JSON metadata and 20 source tileset sheets in the downloadable artifact.

## Important status
This is a source-data export and conversion inventory, not a playable ROM patch. No Quetzal ROM bytes were modified. Source RPG Maker tile IDs are not Emerald metatile IDs. Destination metatile/palette generation and actual map/event registration remain pending; no fake target IDs were assigned.

## Next integration work
1. Derive source graphic tile atlas and autotile composition.
2. Build a viable GBA 4bpp palette/tileset allocation and source-to-metatile translation.
3. Translate passage/priority/terrain behavior to GBA metatile collision/elevation attributes.
4. Translate events, warps, conditions, switches and scripts to Quetzal-compatible map event structures.
5. Validate free map group/layout slots and ROM insertion points before patching.
6. Build/test the ROM in an emulator before calling it playable.

The Emerald map pipeline represents layouts, map headers, connections and map events separately. Reference: https://github.com/pret/pokeemerald/blob/master/tools/mapjson/mapjson.cpp and https://github.com/pret/pokeemerald/blob/master/map_data_rules.mk
