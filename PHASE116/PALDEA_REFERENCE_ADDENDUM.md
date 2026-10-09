# Phase 116 Addendum — Paldea map reference

Date: 2026-10-09.

Correction to the interpretation of input #2: `Pokemon ScarletViolet (1).zip` is intended by the project owner as a **Paldea map/content reference**, not merely a generic FireRed technical comparison ROM. This interpretation is now recorded for future phases.

## Verified file facts
- ZIP contains exactly one member: `Pokemon Scarlet+Violet.gba`.
- ROM size: 16,777,216 bytes (16 MiB).
- Header game code: `BPRE` (FireRed family).
- SHA-256: `ecf6738f537e3842b9f187880fc2617b9aebe4f6a178be13ed25d3f85edefb6e`.
- The ZIP does not contain separate map source files, map exports, a map list, or documentation: the map data is inside the GBA binary.

## Consequence
This is a Paldea reference ROM according to the project's intended use, but its actual Paldea map content has **not yet been extracted or verified**. The printable strings scan did not reveal a reliable list of Paldea map names, so it would be incorrect to claim that the region or its maps are already catalogued. The next technical step is to identify this hack's map-header/group tables and map data using its FireRed-family engine, extract map dimensions, layout pointers, events and connections, and visually inspect the resulting maps before deciding what can be ported into Quetzal.

## Preservation rule
Do not copy raw map pointers, map headers, event structures, or tilesets directly into Quetzal. Different ROM builds can use different offsets, IDs, assets and event scripts. Extract to an intermediate manifest, compare against the Quetzal target, then port/rebuild and validate each selected map.

No ROM bytes were changed by this addendum.
