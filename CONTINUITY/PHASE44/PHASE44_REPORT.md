# Phase 44 — Pearl event conversion to GBA

204 reconstructed Sinnoh maps now use real GBA `MapEvents` structures populated from Pearl `zone_event_release.narc`.

- Object events: 813
- Warp events: 380
- Coord/trigger events: 31
- Pearl furniture records inspected: 174
- Exact warp targets mapped to reconstructed Sinnoh maps: 12
- Warp targets outside the 204 reconstructed maps: 368
- Universal safe GBA interaction script: `end`
- ROM size: 33554432
- Arena: `0x1FE3000..0x1FE96CC`
- Warp-engine fix preserved.

This phase converts the **event data structures**. It does not pretend that Gen4 dialogue/trainer/script bytecode can run unchanged on GBA; script translation is a separate compiler/conversion stage.
