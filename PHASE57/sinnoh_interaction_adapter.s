@ Phase 57 standalone Thumb adapter
@ r0 = localId 1..5
@ r0 = native Emerald event-script pointer, or 0
.syntax unified
.thumb
Sinnoh_GetTwinleafScript:
    cmp r0, #1
    blt invalid
    cmp r0, #5
    bgt invalid
    subs r0, r0, #1
    lsls r0, r0, #2
    adr r1, script_table
    ldr r0, [r1, r0]
    bx lr
invalid:
    movs r0, #0
    bx lr
.align 2
script_table:
    .word 0x09ff9600
    .word 0x09ff9608
    .word 0x09ff9610
    .word 0x09ff9618
    .word 0x09ff9620
