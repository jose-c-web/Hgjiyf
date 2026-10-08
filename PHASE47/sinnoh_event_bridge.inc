@ Phase 47 — native Emerald event bridge
SinnohOreburghGymVictory::
    lockall
    message SinnohText_Gym1Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_01
    releaseall
    end
SinnohEternaGymVictory::
    lockall
    message SinnohText_Gym2Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_02
    releaseall
    end
SinnohVeilstoneGymVictory::
    lockall
    message SinnohText_Gym3Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_03
    releaseall
    end
SinnohPastoriaGymVictory::
    lockall
    message SinnohText_Gym4Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_04
    releaseall
    end
SinnohHearthomeGymVictory::
    lockall
    message SinnohText_Gym5Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_05
    releaseall
    end
SinnohCanalaveGymVictory::
    lockall
    message SinnohText_Gym6Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_06
    releaseall
    end
SinnohSnowpointGymVictory::
    lockall
    message SinnohText_Gym7Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_07
    releaseall
    end
SinnohSunyshoreGymVictory::
    lockall
    message SinnohText_Gym8Victory
    waitmessage
    closemessage
    setflag FLAG_SINNOH_BADGE_08
    releaseall
    end
SinnohLeagueGate::
    checkflag FLAG_SINNOH_BADGE_08
    goto_if FALSE, SinnohLeagueBlocked
    message SinnohText_LeagueOpen
    waitmessage
    closemessage
    end
SinnohLeagueBlocked::
    message SinnohText_LeagueBlocked
    waitmessage
    closemessage
    end
SinnohChampionVictory::
    lockall
    message SinnohText_ChampionDefeated
    waitmessage
    closemessage
    setflag FLAG_SINNOH_LEAGUE_CLEARED
    setflag FLAG_SINNOH_POSTGAME
    releaseall
    end
SinnohSpearPillarPostgame::
    checkflag FLAG_SINNOH_POSTGAME
    goto_if FALSE, SinnohPostgameLocked
    message SinnohText_GalacticReturns
    waitmessage
    closemessage
    end
SinnohPostgameLocked::
    message SinnohText_PostgameLocked
    waitmessage
    closemessage
    end
