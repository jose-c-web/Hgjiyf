# Phase 57 — ObjectEvent Interaction Adapter

Phase 57 identifies the interaction chain used by the Emerald engine:
ProcessPlayerFieldInput -> TryStartInteractionScript -> GetInteractionScript -> GetInteractedObjectEventScript -> GetObjectEventScriptPointerByObjectEventId -> ScriptContext_SetupScript.

A standalone Thumb adapter was inserted into the free Sinnoh arena.

Input:
- r0 = localId

Output:
- localId 1..5 -> pointer to the corresponding Phase 54 Twinleaf script
- any other value -> r0 = 0

Adapter:
- file offset 0x1FF9C00
- GBA address 0x09FF9C00
- Thumb entry 0x09FF9C01
- 44 bytes
- script table starts at adapter+0x1C

No existing executable call site was patched. No map header, warp table, or object event container was modified.

Static validation: PASS.
Runtime validation: PENDING.
