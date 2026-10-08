CONTINUE O PROJETO SINNOH GBA EXATAMENTE DO ESTADO SALVO EM:
https://github.com/jose-c-web/Hgjiyf/blob/main/SINNOH_CONTINUITY_PHASE44.md

NAO COMECE DO ZERO. LEIA O ARQUIVO DE CONTINUIDADE INTEIRO ANTES DE ALTERAR QUALQUER COISA.

OBJETIVO:
Continuar a conversao de scripts de Pokemon Diamond/Pearl para a ROM GBA baseada em Quetzal/Emerald, usando os 204 mapas Sinnoh ja reconstruidos e os eventos ja convertidos.

BASE:
ROM GBA estavel original:
sinnoh_step21_warpchain.gba
SHA-256 cd7a419797e9a45c3060771769b8f028592416e9381fc8e88b5da4c2c640dfa2
32 MiB.
Warp-fix obrigatorio em 0x0DFF3A-0x0DFF3F:
04 1C 00 28 46 D0

ESTADO:
Phases 1-44 ja feitas. Nao repetir.
Phase44 reportada:
204 mapas
813 ObjectEventTemplate
380 WarpEvent
31 CoordEvent
scripts Pearl AINDA NAO CONVERTIDOS.
A ROM Phase44 reportada:
sinnoh_step44_events_converted.gba
SHA-256 9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0

IMPORTANTE:
O bytecode dos scripts de Diamond/Pearl nao e compativel com o interpretador Emerald. Nao copiar os bytes diretamente.
Use a estrutura de comandos D/P do repositorio:
https://github.com/DS-Pokemon-Rom-Editor/scrcmd-database
arquivo diamond_pearl_v2.json
Ele contem IDs, nomes, parametros e descricoes dos comandos.

FONTE PEARL:
Repositorio:
https://github.com/jose-c-web/Hgjiyf
NARCs:
fielddata/script/scr_seq_release.narc
fielddata/eventdata/zone_event_release.narc
fielddata/msgdata/...
fielddata/encountdata/d_enc_data.narc
fielddata/encountdata/p_enc_data.narc
fielddata/trainerdata/...
Tambem existem os land_data, matrix, map headers, nomes, itens, trainers e Pokemon ja extraidos.

ESTRATEGIA:
1. Recuperar a ROM/artefatos reais, nao inventar arquivos.
2. Catalogar todos os scripts D/P referenciados pelos 204 mapas.
3. Decodificar os comandos usando a base D/P.
4. Mapear cada comando D/P para equivalente Emerald/Quetzal.
5. Para comandos sem equivalente direto, criar adaptadores seguros em free space e documentar.
6. Converter primeiro:
   - End/Return
   - Set/Clear/CheckFlag
   - Set/Compare/Increment/Decrement vars
   - Message/OpenMessage/CloseMessage
   - Wait
   - GiveItem
   - HiddenItem
   - TrainerBattle
   - movement
   - warp/teleport
7. Depois converter cutscenes e comandos especiais.
8. Converter mensagens D/P para texto GBA com encoding correto; nao usar texto bruto NDS como se fosse texto GBA.
9. Reapontar mapScripts, CoordEvents e ObjectEvents para os scripts GBA convertidos.
10. Usar trainers ja extraidos para reconstruir trainer battles.
11. Validar todos os ponteiros, offsets, alinhamento, terminadores e tamanhos.
12. Testar primeiro Twinleaf, Route201, Sandgem, Jubilife e Oreburgh.
13. Depois expandir para todos os 204 mapas.
14. Manter ROM <=32 MiB.
15. Usar somente regioes comprovadamente livres em 0xFF.
16. Nunca sobrescrever:
   - 0x1348500 gMapLayouts sem validacao
   - blockdata privado
   - layouts 993-1196
   - warp-fix
   - grupos existentes de Hoenn/Quetzal.

DADOS DE MAPA:
204 layouts privados: IDs 993-1196.
Tabela privada: file 0x1FDB6A8, 4896 bytes.
Blockdata: file 0x19AC164, 534528 bytes.
Group43 foi usado para os mapas integrados.
Phase43 tinha 406 warps.
Phase44 adicionou eventos estruturais.

ABI:
MapHeader:
mapLayout*, events*, mapScripts*, connections*, music, mapLayoutId, regionMapSectionId, cave, weather, mapType, bikingAllowed, flags, floorNum, battleType.
MapEvents:
objectEventCount, warpCount, coordEventCount, bgEventCount, objectEvents*, warps*, coordEvents*, bgEvents*.

VALIDACAO OBRIGATORIA:
Nao afirmar que scripts foram convertidos sem realmente gerar bytecode funcional.
Gerar:
- script conversion report
- command mapping report
- unresolved command list
- pointer audit
- ROM SHA
- artifact ZIP
- ROM final
- README/manifest da nova fase.

QUANDO ENCONTRAR UM COMANDO D/P SEM EQUIVALENTE:
Nao substitua silenciosamente por END. Preserve o comportamento de forma segura se possivel, ou marque como adaptador pendente. Priorize funcionamento real dos NPCs e progressao.

PRIMEIRO PASSO:
Ler SINNOH_CONTINUITY_PHASE44.md e recuperar os artefatos. Depois auditar os scripts de Pearl e descobrir o formato exato dos comandos usados pelos 204 mapas. So depois iniciar a Phase45.

ENTREGA:
Ao terminar cada fase, salvar artefatos e estado no GitHub e informar:
- o que foi realmente convertido
- quantos comandos foram convertidos
- quantos ficaram pendentes
- SHA da ROM
- caminho/URL do arquivo de continuidade
- proxima fase objetiva.

NAO FAZER UMA VERSAO GENERICA. ESTE E UM PROJETO CONTINUADO.