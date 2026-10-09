# Phase 116 — Auditoria das quatro frentes (Quetzal / Sinnoh)

Data: 2026-10-09. Escopo: os três arquivos anexados, artefatos reais das Actions do repositório e relatórios existentes. **Esta é uma auditoria, não uma ROM nova. Nenhuma ROM foi alterada nesta fase.**

## 1. ROM-base Quetzal
- Arquivo: `PokemonQuetzalPtBrAlpha9v0.gba`
- Tamanho: 33.554.432 bytes (32 MiB); game code `BPEE`.
- SHA-256: `9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f`.
- Esta ROM NÃO tem o mesmo SHA da base usada pelos artefatos Phase 21–23. Não é seguro reaplicar offsets/tabelas do pipeline anterior nela sem redescobrir e validar os endereços.

## 2. ROM de referência Scarlet/Violet GBA
- Arquivo: `scarlet_violet_reference.gba`
- Tamanho: 16 MiB; game code `BPRE` (família FireRed).
- SHA-256: `ecf6738f537e3842b9f187880fc2617b9aebe4f6a178be13ed25d3f85edefb6e`.
- Foi feita apenas a inspeção do cabeçalho e fingerprint. Não foi copiado código ou dado para Quetzal: os formatos/endereços precisam ser validados primeiro.

## 3. Fire Ash como referência de Sinnoh
- ZIP: `Pokemon Fire Ash 3.7.1 (Audioless).zip`; 16.701 membros e 996 arquivos de mapa `Map###.rxdata`.
- A árvore de MapInfos sob as raízes de Sinnoh (IDs 501 e 503) contém 138 entradas de mapa/submapa: Twinleaf, Routes 201–222, cidades, ginásios, casas, lagos, cavernas, Mt. Coronet, Spear Pillar e Liga, entre outros.
- O changelog documenta gates úteis: entrada em Hearthome após vencer Gardenia em Eterna; teleporte de Celestic após derrotar Paul na Route 210 (3.7.1); atalho de Valor Lakefront após encontrar Wallace no Lake Valor; e alteração da transição Valor Lakefront/Route 213.
- Uso: referência de progressão e locais. Os arquivos RPG Maker não são diretamente importáveis para Emerald GBA.

## 4. Estado real do pipeline e integração
- Artefatos reais das Actions Phase 21–23 foram baixados e inspecionados. As validações estáticas passaram, mas cada relatório define explicitamente `rom_integration_allowed: false`.
- Phase 21: 204 mapas únicos, 287 referências de mapa e 58 tilesets catalogados; os mapas ainda preservam IDs semânticos.
- Phase 22: 58 tilesets, 15 papéis semânticos e nenhum erro de parsing; gera candidatos de metatile, não patches.
- Phase 23: 245.190 células resolvidas de 267.264; 22.074 ainda não resolvidas (8,26%). As semânticas disponíveis são grama, terra, água e desconhecido; faltam estradas, paredes, árvores, cercas, margens e outras categorias. Portanto, não é ainda uma reconstrução visual completa.
- Os relatórios das fases 81–115 registram 559 headers Pearl, 512 bancos de eventos e 204 mapas GBA, mas os cinco mapas-piloto continuam sem identidade segura ou com confiança baixa. A fase 91–95 registra 813 scripts como stubs END; as fases 106–115 não aplicaram patch de NPC/script/warp.
- O repositório marca Phase 45 como `BLOCKED_PENDING_BINARY_RECOVERY`: faltam a base Phase 44 com SHA `9e12e7c2de0f0671d339c6683e6295944d5a281f3d0e4d436fd617c2120512d0` e os NARCs Pearl de scripts/eventos com hashes exatos. A Quetzal anexada não substitui esses arquivos.

## Bloqueios confirmados
1. A ROM Quetzal anexada não corresponde à base binária do pipeline anterior.
2. 22.074 células de mapa seguem sem resolução; categorias visuais importantes ainda não foram mapeadas.
3. A correspondência dos mapas-piloto/NPCs permanece insegura e os scripts de evento ainda não constituem a campanha executável.
4. A conversão real de scripts Pearl está bloqueada até recuperar e validar a ROM Phase 44 e os dois NARCs.

## Próxima execução segura
1. Recuperar a base Phase 44 e NARCs e conferir SHA-256 antes de tocar em bytes.
2. Resolver Twinleaf, Route 201, Sandgem, Jubilife e Oreburgh com evidência visual/estrutural e warps bidirecionais; não usar score baixo como autorização de patch.
3. Expandir semânticas visuais para estradas, árvores, paredes, cercas, margens e interiores, validando cada mapa.
4. Converter scripts Pearl em bytecode Emerald após recuperar NARCs e validar cada opcode; nunca transformar comandos desconhecidos em END.
5. Integrar somente com ABI/map IDs verificados, validar ponteiros, colisões e warps e depois testar a ROM no emulador.

**Resultado desta fase:** quatro frentes auditadas e documentadas; nenhum patch arriscado foi aplicado à ROM-base. Sinnoh ainda não está provado como jogável/zerável.
