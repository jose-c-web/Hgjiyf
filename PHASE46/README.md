# Phase 46 — Sinnoh D/P Script Engine

This phase establishes the safe Diamond/Pearl -> Emerald/Quetzal script-conversion layer. The current supplied artifacts do not contain Pearl `scr_seq_release.narc` or `zone_event_release.narc`, so no executable script conversion is claimed.

Pipeline: NARC intake -> D/P command decode -> IR -> verified GBA mapping -> bytecode emission -> event repoint -> pointer audit.

Unknown commands are never silently replaced with END.
