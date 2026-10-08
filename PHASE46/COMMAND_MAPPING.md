# Phase 46 command mapping policy

The D/P database supplies command IDs and parameters. These are semantic candidates, not proof of Emerald ABI compatibility.

- End -> END
- Return -> RETURN
- SetFlag -> SETFLAG
- ClearFlag -> CLEARFLAG
- CheckFlag -> CHECKFLAG
- Message -> MESSAGE
- CloseMessage -> CLOSE_MESSAGE
- WaitButton -> WAIT_BUTTON
- GiveItem -> GIVE_ITEM
- TrainerBattle -> TRAINER_BATTLE
- Warp -> WARP

All other commands remain ADAPTER_PENDING until real Pearl script streams are available.
