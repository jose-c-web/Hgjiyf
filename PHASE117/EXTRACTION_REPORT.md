# Phase 117 — Extração de mapas de Scarlet/Violet e catálogo Fire Ash

Data: 2026-10-09. Entrada: os ZIPs de referência já anexados à conversa. Quetzal foi preservada; nenhuma ROM foi modificada.

## Scarlet+Violet GBA — extração binária concluída

ROM dentro de `Pokemon ScarletViolet (1).zip`:
- Tamanho: 16.777.216 bytes (16 MiB)
- SHA-256: `ecf6738f537e3842b9f187880fc2617b9aebe4f6a178be13ed25d3f85edefb6e`
- Tabela de grupos de mapas encontrada através do ponteiro no offset `0x5524C`, resolvendo para `0x083526A8`.

Resultados:
- 43 grupos de mapas
- 425 headers válidos, nenhum header inválido
- 309 layouts únicos
- 61 tilesets únicos
- 1.294 registros de warp extraídos
- 61 mapas com conexões de mapas
- 421 previews PNG renderizados
- 4 layouts cujos dados não puderam ser decodificados com segurança (falha de back-reference LZ77 ou comprimento incompatível); isso não prova, por si só, que a ROM esteja corrompida. Foram sinalizados, não corrigidos por suposição

O pacote exporta os grids de metatiles descomprimidos, bordas, tiles 4bpp, paletas, metatiles, atributos, manifest JSON, índice CSV de mapas, índice CSV de warps, PNGs individuais e folhas de contato por grupo.

**Limitação de nomenclatura:** os mapas foram identificados de forma segura por grupo/número e `region_section_id`. A tabela específica de nomes dessa ROM ainda precisa ser recuperada para dar nomes canônicos a cada mapa e separar com certeza os mapas específicos de Paldea dos mapas herdados/auxiliares. O pacote não inventa nomes.

## Fire Ash — catálogo de referência Kanto–Galar

Extraídos os 996 arquivos `Data/Map###.rxdata` correspondentes às 996 entradas de `MapInfos.rxdata`, com hierarquia de nomes e índice CSV/JSON. Classificação por árvore de pais do MapInfos:

| Região | Entradas/mapas |
|---|---:|
| Kanto | 185 |
| Johto | 101 |
| Hoenn | 114 |
| Sinnoh | 138 |
| Unova | 129 |
| Kalos | 90 |
| Alola | 76 |
| Galar | 44 |
| Outras regiões/áreas laterais | 119 |
| **Total** | **996** |

As 119 entradas restantes incluem áreas laterais/crossover e raízes como Orange Archipelago e Tiall. Os dados Fire Ash usam estruturas RPG Maker `.rxdata`; servem de referência para geografia e progressão, mas não são diretamente compatíveis com os bytes de mapas do Emerald GBA.

## Próxima etapa técnica

1. Identificar a tabela de nomes/nomes de seção da ROM Scarlet/Violet.
2. Conferir visualmente os 4 layouts problemáticos e os 421 previews para classificar quais grupos representam Paldea.
3. Comparar mapas selecionados com o catálogo Fire Ash e com os mapas/tilesets reais de Quetzal.
4. Só então preparar uma conversão de mapas, eventos, colisões e warps para Quetzal, com validação de IDs e teste em emulador.

Nenhuma ROM foi alterada e nenhuma integração foi declarada como concluída nesta fase.
