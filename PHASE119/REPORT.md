# Phase 119 — Auditoria de conversão para Quetzal

## Artefatos inspecionados
- Scarlet/Violet GBA SHA-256: ecf6738f537e3842b9f187880fc2617b9aebe4f6a178be13ed25d3f85edefb6e; 425 headers em 43 grupos; 309 layouts únicos.
- Quetzal PT-BR SHA-256: 9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f; 33.554.432 bytes; game code BPEE.
- Fire Ash 3.7.1: catálogo de MapInfos com 996 mapas, conforme fase anterior.

## Auditoria de layout
- 305 layouts sem erro registrado; 4 layouts sinalizados para revisão.
- O pacote Phase 119 contém um CSV por mapa com grupo, número, section ID, layout, dimensões, tilesets, warps e conexão, além de resumo por grupo e uma folha de contato de 24 candidatos.
- IDs são técnicos, não nomes canônicos de Paldea.

## Compatibilidade e bloqueios reais
1. **Não copiar diretamente os grids.** Os metatile IDs da ROM fonte referenciam metatiles e atributos dos tilesets da própria ROM. A Quetzal tem SHA-256 9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f e não corresponde à ROM-base validada pelo pipeline antigo (SHA-256 cd7a419797e9a45c3060771769b8f028592416e9381fc8e88b5da4c2c640dfa2). Endereços conhecidos de outro build não podem ser reutilizados como se fossem válidos.
2. **Remapeamento visual necessário.** Precisamos gerar correspondências entre tiles/metatiles da fonte e os tilesets existentes na Quetzal, com confiança e revisão visual; equivalência numérica de ID não prova equivalência visual.
3. **Eventos precisam ser convertidos separadamente.** Warps, scripts, objetos, flags e conexões dependem de IDs e rotinas da engine. Só a grade não garante navegação jogável.
4. **Quatro casos seguem sem decodificação segura.** Estão listados em LAYOUT_ERRORS.csv; não foram preenchidos artificialmente.

## Resultado desta fase
Criados CSVs de auditoria e resumo por grupo, além da folha visual. Nenhuma ROM foi alterada e nenhum patch é declarado como testado. Próximo alvo seguro: escolher um mapa exterior com tileset e warp compreendidos, criar um protótipo de conversão isolado e só integrar após conferir metatiles, colisão, warp de ida/volta e boot em emulador.
