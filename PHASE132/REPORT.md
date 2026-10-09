# Phase 132 — 4bpp graphics conversion candidates and event translation classification

## Actual generated artifacts
- Converted 20 static source tileset atlases into candidate GBA 4bpp packed graphics.
- Generated one 16-color BGR555 palette per atlas with transparent index 0.
- Deduplicated 8x8 graphics tiles and wrote atlas coordinate -> unique tile ID CSVs.
- Generated source 32x32 cell manifests with 4x4 arrays of 8x8 tile IDs.
- Classified all 28,324 source event commands into destination command families, preserving original JSON parameters, map/event/page/index and indentation. Includes explicit classes for transfer-player/warps (201), conditional branches (111), switches (121), variables (122), battle processing (301), shops (302), messages/choices and custom command 509.

## Artifact
Download: https://github.com/jose-c-web/Hgjiyf/blob/main/PHASE132/REPORT.md
Local artifact generated in conversation: sinnoh_phase132_4bpp_palette_metatile_candidates.zip

## Limits — do not misrepresent as playable
This is the first actual indexed/4bpp graphics encoding pass, but the result is candidate assets only. Each source atlas currently has one 16-color palette, which is deliberately conservative and may lose detail. The source atlas cell size is 32x32; Emerald metatiles are 16x16, so the data still needs correct repacking and source tile ID semantics. RPG Maker autotiles need reconstruction from their component graphics. The event CSV is a translation classification/backlog, not compiled Emerald scripts. Collision/elevation attributes, Quetzal map group/layout/header registration, full event scripts and ROM/emulator validation are not complete. No ROM bytes were modified.

## Next work
1. Reconstruct RPG Maker autotiles and source ID semantics.
2. Repack 8x8 graphics into 16x16 metatiles and encode collision/elevation.
3. Fit palettes and graphics into actual Quetzal resource limits.
4. Generate Quetzal-compatible map layouts, headers, connections, warps, object events and scripts.
5. Implement trainer teams, gym progression, story flags, items and battles.
6. Build a patch against the verified base ROM and test in emulator before claiming playability.

Reference for Emerald's separate generated layout/map/event registration pipeline: https://github.com/pret/pokeemerald/blob/master/map_data_rules.mk
