# Phase 50 — Twinleaf NPC executable pilot

Base: Phase 48 ROM.

The first ObjectEvent on Sinnoh map 0 now has a real native Emerald script pointer. The script is SETFLAG 0x0700 followed by END, stored at ROM offset 0x1FF91E0. Static validation passed; emulator verification remains required.

Output SHA-256: 68bd95f09e39cc8934df19b63f1927ba3687662e6a2ea38d05aaa783463d2395
