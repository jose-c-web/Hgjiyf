# Phase 127 — Preparação integral de Sinnoh

## Resultado desta fase

- Mapas/entradas listados no catálogo Sinnoh: **138**.
- Arquivos Map*.rxdata efetivamente extraídos: **138**.
- Arquivos de mapa ausentes: **0**.
- Arquivos de suporte copiados: **29**.
- ROM Quetzal alterada: **não** (integridade preservada).

## Cobertura do inventário

- Cidades/locais: 30
- Ginásios: 8
- Interiores/instalações: 39
- Lagos: 9
- Liga Pokémon: 6
- Raízes/índices: 2
- Rotas: 32
- Áreas especiais/cavernas: 12

## Próxima implementação na ROM GBA

1. Resolver mapa por mapa a correspondência entre IDs semânticos Sinnoh e layouts/tilesets disponíveis na Quetzal.
2. Converter primeiro a cadeia de abertura Twinleaf → Route 201 → Lake Verity → Sandgem → Route 202, incluindo warps e scripts.
3. Expandir a conversão visual e eventos para as 8 insígnias, Mt. Coronet/Spear Pillar, lagos e Liga.
4. Manter o inventário como fila de execução; nenhuma caixa `*_converted` deve ser marcada até existir conversão e validação reais.

## Limitação técnica crítica

Os `.rxdata` são objetos serializados do RPG Maker e não são mapas GBA. Esta entrega prepara os 138 itens e os dados auxiliares como fonte de conversão; ela **não** afirma que a ROM contenha Sinnoh inteiro, nem que NPCs/scripts estejam executáveis no motor Quetzal. Copiar esses arquivos ou seus ponteiros para a ROM seria inválido.

## Ordem inicial priorizada

1. Twinleaf Town
2. Twinleaf House
3. Route 201
4. Lake Verity
5. Lake Verity Cave
6. Sandgem Town
7. Sandgem House
8. Professor Rowan's Lab
9. Route 202
10. Jubilife City
11. Route 203
12. Oreburgh Gate
13. Oreburgh City
14. Oreburgh Mine
15. Route 204
16. Ravaged Path
17. Floaroma Town
18. Floaroma Meadow
19. Route 205
20. Eterna Forest
21. Eterna City
22. Route 206
23. Route 207
24. Mt. Coronet
25. Hearthome City
26. Route 209
27. Solaceon Town
28. Solaceon Ruins
29. Route 210
30. Route 215
31. Veilstone City
32. Route 214
33. Valor Lakefront
34. Lake Valor
35. Route 213
36. Pastoria City
37. Route 212
38. Celestic Town
39. Route 218
40. Canalave City
41. Iron Island
42. Route 211
43. Route 216
44. Route 217
45. Lake Acuity
46. Snowpoint City
47. Route 222
48. Sunnyshore City
49. Spear Pillar
50. Sinnoh Pokemon League
