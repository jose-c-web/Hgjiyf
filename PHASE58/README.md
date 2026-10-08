# Phase 58 — ObjectEvent Resolver ABI

Phase 57 used a localId-only adapter. Phase 58 upgrades it to the actual Emerald ObjectEvent ABI.

Resolver entry: 0x09FF9C61
Input:
- r0 = ObjectEvent ID
- r1 = base address of gObjectEvents array

ObjectEvent offsets confirmed from pret/pokeemerald:
- localId 0x08
- mapNum 0x09
- mapGroup 0x0A

The resolver accepts Sinnoh Twinleaf objects only when mapGroup=43, mapNum=0, localId=1..5, and returns the corresponding native script pointer. Other inputs return NULL.

No existing call site is patched. This keeps all existing regions untouched while preparing the exact ABI needed for the final resolver hook.

Static validation: PASS.
Runtime validation: PENDING.
ROM SHA-256: 6d040117b41d63ec9ce191fb29388455cb30f1a43dd821ea01dac8cd0ffe7fde
