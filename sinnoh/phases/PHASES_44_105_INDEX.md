# Sinnoh — índice das fases 44–105

Este índice registra a continuidade das fases anteriores que foram executadas no ambiente de reconstrução.

## 44
- 204 mapas Sinnoh reconstruídos; layouts 993–1196.
- 406 warps, 813 ObjectEvents, 31 CoordEvents.
- Scripts preservados como metadados; execução ainda não ligada.
- Artefato: `sinnoh-reconstruction-phase44.zip`.
- ROM: `sinnoh_step44_events_converted.gba`.

## 45A–45E
- Mapeamento de comandos Pearl→GBA.
- Pool de mensagens e compilação inicial de scripts.
- Correção de ABI de controle de fluxo na 45D.
- Checkpoint correto: `sinnoh_step45d_fixed.gba`.
- SHA-256: `66bc1619a72da36b24f09f7eacc72a87e4d662ee24195319e8cfe01c3467be23`.
- Warp-fix preservado em `0x0DFF3A–0x0DFF3F`: `04 1C 00 28 46 D0`.
- 45E: tabela estrutural de eventos em `0x1FE0EC4`; nenhuma identidade de piloto foi considerada comprovada.

## 46–55
- Auditorias de reconstrução/segurança e preservação do checkpoint.
- Artefato: `sinnoh-reconstruction-phase46-55-audit.zip`.

## 56–65
- Lote de validação máxima segura.
- Artefato: `sinnoh-reconstruction-phase56-65-max-safe.zip`.

## 66–80
- Auditorias e validações sem alteração destrutiva.
- Artefato: `sinnoh-reconstruction-phase66-80-max-safe.zip`.

## 81–83
- Catálogo de 559 headers Pearl, 512 bancos de eventos e 204 mapas GBA.
- Decodificação do destino GBA como par group/map.
- Artefato: `phase81_83/phase81_83_mapping_catalog.json`.

## 84–87
- Teste seguro com links de script para NPCs.
- 193 mapas com NPCs receberam link de teste; 380 warps preservados.
- Artefato: `sinnoh-reconstruction-phase84-87-safe-test.zip`.
- Não foi tratado como prova de identidade dos NPCs.

## 88–90
- Catálogo global: 559 headers, 512/512 bancos de eventos, 3160 ObjectEvents, 1118 warps, 114 triggers, 1051 bancos de script, 10309 funções e 624 bancos de mensagens.
- Artefato: `phase88_90/global_event_script_catalog.json`.

## 91–95
- Auditoria de resolução dos 204 mapas.
- Todos os 813 ObjectEvents ainda eram stubs END.
- Pilotos permaneciam sem identidade comprovada.
- Artefato: `phase91_95/phase91_95_map_resolution_audit.json`.

## 96–100
- Propagação de grafo em 8 iterações.
- Resultados ainda ambíguos para Twinleaf/Sandgem e dependentes de hipótese para os demais.
- Artefato: `phase96_100/phase96_100_global_graph_candidates.json`.

## 101–105
- Atribuição global 1:1 como diagnóstico.
- Cinco pilotos permaneceram sem resolução confiável.
- Artefato: `phase101_105/PHASE101_105_GLOBAL_ASSIGNMENT.json`.

## Gate de continuidade
Até a fase 105, nenhuma identidade de mapa-piloto foi considerada segura o bastante para patch de ObjectEvents/scripts. Isso evita criar uma ROM aparentemente funcional, mas com NPCs/warps ligados aos mapas errados.
