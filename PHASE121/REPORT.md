# Phase 121 — Normalização do primeiro mapa para conversão

## Resultado
A grade fonte usa palavras little-endian de 16 bits. O campo não é um ID puro: bits 0–9 = ID do metatile; bits 10–11 = flags de colisão; bits 12–15 = elevação. Interpretar a palavra inteira como ID produz valores inválidos e previews enganosas.

Para `g03_m010` (66×55):
- 3.630 células; 319 IDs distintos após máscara `0x03FF`.
- ID mínimo 1; máximo 839.
- Flags de colisão: 917 células valor 0 e 2.713 valor 1.
- Elevação: 2.711 células nível 0 e 919 células nível 3.
- 15 warps preservados.

O ZIP contém IDs normalizados, flags de colisão e elevação separados, CSV por célula, inventário de warps e estatísticas.

## Limite restante
A normalização dos campos de origem não cria automaticamente correspondência visual com Quetzal. Os IDs apontam para metatiles da ROM Scarlet/Violet e precisam de crosswalk validado contra os tilesets reais da ROM Quetzal. Nenhum dado foi escrito na ROM e o mapa ainda não é jogável.

ROM Quetzal preservada sem alterações. Próximo passo: identificar a tabela real de tilesets/metatiles da build Quetzal e produzir candidatos de correspondência visual com confiança explícita.