# SINNOH GBA — CONTINUIDADE DO PROJETO

Atualizado em 2026-10-08. Este arquivo existe para impedir que o projeto seja reiniciado ou tratado como uma ROM genérica.

## OBJETIVO
Modificar uma ROM GBA baseada em Pokemon Quetzal/Emerald para adicionar Sinnoh completo, mantendo as regioes existentes.

## REGRA CRITICA
Nao substituir a ROM GBA pelo Pokemon Pearl NDS. Pearl e apenas referencia de dados Sinnoh.
Fluxo:
Pearl NDS -> extracao/reconstrucao -> GBA Quetzal/Emerald -> integracao final.

## ROM BASE ESTAVEL
Arquivo: sinnoh_step21_warpchain.gba
SHA-256: cd7a419797e9a45c3060771769b8f028592416e9381fc8e88b5da4c2c640dfa2
Tamanho: 33,554,432 bytes.
Correcao obrigatoria em offsets 0x0DFF3A-0x0DFF3F:
04 1C 00 28 46 D0
NAO remover.

## FONTE PEARL
Repositorio: jose-c-web/Hgjiyf
Arquivo-fonte: PK P3ar1 (PT-BR).nds / ZIP correspondente.
NARCs importantes:
fielddata/areadata/area_data.narc
fielddata/areadata/area_build_model/area_build.narc
fielddata/areadata/area_build_model/areabm_texset.narc
fielddata/areadata/map_tex_set.narc
fielddata/areadata/area_move_model/move_model_list.narc
fielddata/encountdata/d_enc_data.narc
fielddata/encountdata/p_enc_data.narc
fielddata/eventdata/zone_event_release.narc
fielddata/land_data/land_data_release.narc
fielddata/mapmatrix/map_matrix.narc
fielddata/maptable/mapname.bin
fielddata/script/scr_seq_release.narc

## DADOS RECONSTRUIDOS
578 land_data
245 mapmatrix
512 eventos
1051 scripts
183 encounters
559 map headers
559 nomes
850 trainers
850 trainer Pokemon
442 itens
624 message files
16 scenario message banks
501 Pokemon
471 moves

## MAPA GBA SINNOH
Map Group original de trabalho: 40.
Mapas reconstruidos: 204 unicos.
IDs de layout privados: 993..1196.
Tabela de layouts privada: file 0x1FDB6A8 / GBA 0x09FDB6A8, 204*24.
Blockdata: 534528 bytes.
Border: file 0x90B914, bytes 08 00 08 00 08 00 08 00.
gMapLayouts original: 0x1348500.
A Phase41 conectou IDs 993..1196 a gMapLayouts[layoutId-1].

## PHASES COMPLETAS
1-4 catalogo/eventos/scripts/encounters/matrix/adjacencias.
5 blueprints.
6 terrain.
7 collision.
8 objects.
9 semantic mapping.
10-18 reconstrucoes progressivas.
19 tilesets reais da GBA.
20 semantic metatiles reais.
21 atribuicao de tilesets.
22 candidatos visuais.
23 primeira materializacao.
24 permissões land_data.
25 composição contextual.
26 anchors estruturais.
27 reconstrução de paredes/doors/stairs/cave.
28 variantes geométricas.
29 object anchors.
30 auditoria.
31 anchors adicionais.
32 separacao dos FFFF restantes.
33 dry-run MapLayout.
34 layouts reais.
35 packing dentro dos 32 MiB.
36 ABI de MapHeader/MapGroup.
39 auditoria de storage.
40 headers preparados.
41 tabela gMapLayouts conectada.
42 core maps.
43 integracao de grupo + eventos sintéticos.
44 conversao estrutural de eventos Pearl.

## STORAGE SEGURO
Blockdata Phase35: file 0x19AC164, 534528 bytes, GBA 0x099AC164.
Private layouts: file 0x1FDB6A8, 4896 bytes, GBA 0x09FDB6A8.
Phase40 header table: file 0x1FDD800, 204*28.
Shared empty events: 0x1FDEE50.
Shared empty connections: 0x1FDEE60.
Group table Phase40: 0x1FDEE68.
Free upper region identificado em 0x1FDD800..0x2000000, mas respeitar tudo ja ocupado.
NAO usar 0x1A2E964 como codigo.
NAO sobrescrever 0x1FDB800.
NAO sobrescrever a gMapLayouts original sem validar.

## PHASE43 / 44
Phase43 foi reportada como:
ROM: sinnoh_step43_sinnoh_group43_full.gba
SHA-256: 1bde8c2356fc7deafed7741394e72882718d53b2f68cffcf77afb805d5eb36f3
204 mapas, 406 warps, 0 FFFF, grupo 43 expandido preservando 33 mapas antigos.
Phase44:
ROM reportada: sinnoh_step44_events_converted.gba
SHA-256: 9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0
Conversao estrutural reportada:
204/204 mapas
813 ObjectEventTemplate
380 WarpEvent
31 CoordEvent
174 furniture analisados
0 ponteiros invalidos
0 objetos fora dos limites
0 erros estruturais
IMPORTANTE: scripts Pearl NAO foram ainda convertidos para bytecode Emerald. Interações foram deixadas seguras/terminais. A etapa de scripts ainda está PENDENTE.

## FFFF
Fase30 tinha 15679 FFFF.
Fase43 reportou 0 FFFF por preenchimento semântico/geométrico. Validar novamente antes de usar como base final.

## SCRIPTS — ESTADO ATUAL
O pedido atual era converter os scripts de Pearl.
A conversa terminou antes da implementação final.
Foi encontrada uma base pública de comandos Diamond/Pearl:
DS-Pokemon-Rom-Editor/scrcmd-database, arquivo diamond_pearl_v2.json.
Ele fornece IDs, nomes, parâmetros e semântica de comandos D/P.
Isso deve ser usado para montar um tradutor D/P -> scripts Emerald/Quetzal.

NÃO copiar bytecode Pearl diretamente para o interpretador Emerald.

Prioridade de conversao:
1. mensagens/NPC simples
2. giveitem
3. hidden item
4. trainerbattle
5. flags/variáveis
6. movement/waits
7. warps/teleport
8. cutscenes
9. Team Galactic
10. gyms/elite four/Cynthia
11. lendários/Palkia
12. Victory Road/Liga
13. postgame.

## ABI / ROTEAMENTO
Fluxo padrão conhecido:
Overworld_GetMapHeaderByGroupAndId(group,num)
-> MapHeader
-> LoadCurrentMapData
-> mapLayoutId
-> GetMapLayout / gMapLayouts[mapLayoutId-1]
A ROM Quetzal customizada não deve ser tratada como pokeemerald vanilla sem validação local.
MapHeader GBA:
mapLayout*, events*, mapScripts*, connections*, music, mapLayoutId, regionMapSectionId, cave, weather, mapType, bikingAllowed, flags, floorNum, battleType.
MapEvents:
objectEventCount, warpCount, coordEventCount, bgEventCount, objectEvents*, warps*, coordEvents*, bgEvents*.

## O QUE O PRÓXIMO CHAT DEVE FAZER
Nao recomeçar fases 1-44.
Primeiro recuperar/verificar a ROM mais recente e os arquivos de eventos/scripts.
Depois implementar Phase45+:
- construir tradutor real de scripts D/P;
- converter comandos simples primeiro;
- gerar pools de scripts GBA;
- converter mensagens D/P para texto GBA, respeitando encoding e limites;
- substituir mapScripts/CoordEvents/Object scripts pelos ponteiros reais;
- converter trainer battles usando a tabela de trainers já extraída;
- validar todos os ponteiros e tamanhos;
- testar staticamente Twinleaf, Route201, Sandgem, Jubilife, Oreburgh;
- só então ampliar para os 204 mapas;
- manter ROM <=32MiB e usar apenas free space comprovadamente 0xFF;
- nunca sobrescrever a base estável, gMapLayouts global, blockdata ou warp-fix.

## FONTES / REFERENCIAS
pokeemerald: https://github.com/pret/pokeemerald
PokePlat: https://github.com/JimB16/PokePlat
scrcmd database: https://github.com/DS-Pokemon-Rom-Editor/scrcmd-database
Projeto Pearl: https://github.com/jose-c-web/Hgjiyf


## RECUPERAÇÃO DE ARTEFATOS — 2026-10-08
A auditoria verificou que os artefatos binários da Phase44 existem no ambiente de trabalho, mas não estavam materializados no GitHub principal. O GitHub contém apenas ponteiros LFS de 133 bytes para algumas ROMs, portanto esses ponteiros não devem ser tratados como ROMs recuperáveis.

Artefatos verificados localmente:
- sinnoh_step44_events_converted.gba — 33554432 bytes — SHA-256 9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0
- sinnoh-reconstruction-phase44.zip — SHA-256 78882441482c26f70dcbd12ee5834b731757ef5109698e72b2b2eb1e1993df4c
- fielddata_script_scr_seq_release.narc — SHA-256 c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7
- fielddata_eventdata_zone_event_release.narc — SHA-256 3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4

O relatório e as estatísticas da Phase44 agora também estão versionados em:
- sinnoh_work/phase44/PHASE44_REPORT.md
- sinnoh_work/phase44/phase44_statistics.json

IMPORTANTE: os binários acima ainda precisam ser materializados no GitHub/LFS ou anexados ao próximo chat para que outro ambiente possa recuperá-los. Não substituir a Phase44 por uma ROM anterior.


## PHASE45 ARTIFACT HANDOFF — 2026-10-08

Canonical next-chat handoff: `CONTINUITY/PHASE45_START_HERE.md`.

Verified Phase44 ROM: `sinnoh_step44_events_converted.gba` — SHA-256 `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0`, 33,554,432 bytes.

Verified Pearl script NARC: `fielddata_script_scr_seq_release.narc` — SHA-256 `c62e6f7f537fbff6604ba0e7985270ace40562d5a6912f2661b892545f039af7`, 219,608 bytes.

Verified Pearl event NARC: `fielddata_eventdata_zone_event_release.narc` — SHA-256 `3b61439a26b1c4bc6de9b1301a5a3073f6edf2b392082a4427e8ef3228bb23a4`, 140,020 bytes.

Phase45 must not substitute an earlier ROM when the exact Phase44 binary is unavailable. Large binary artifacts are documented by verified hashes in `CONTINUITY/PHASE45_INPUT_MANIFEST.json`; the current GitHub connector has no direct binary/release upload capability, and Library upload was blocked by the account storage quota. This is an access limitation, not permission to restart or fake Phase45.
