# Histórico completo disponível — Fases 81–115

## Fases 81–83 — catálogo estrutural
- 559 headers de mapas Pearl analisados.
- 512/512 bancos de eventos analisados.
- 204 mapas Sinnoh GBA catalogados.
- 380 warps GBA e estruturas de eventos catalogados.
- Nenhum patch de NPC/script/warp aplicado.
- Gate: AUDIT_ONLY / matching estrutural.

Artefatos locais:
- `phase81_83/phase81_83_mapping_catalog.json`
- `phase81_83/PHASE81_83_REPORT.md`
- `build_phase81.py`
- ZIP SHA-256: `2171921677ce0fb7f2df8c0830de4b93d12d823a1d1851cbd7225441438b893e`

## Fases 84–87 — teste técnico seguro
- ROM de teste: 32 MiB.
- 204 mapas processados; primeiro ObjectEvent de cada mapa recebeu ligação para função de diálogo genérica já validada.
- 204 objetos ligados.
- Layouts, warps e MapHeaders não foram regravados.
- Identidade Pearl→GBA dos NPCs não foi considerada provada.
- Warp-fix preservado: `04 1C 00 28 46 D0`.

Artefatos:
- `sinnoh_phase84_87_safe_test.gba`
- `phase84_87_safe_report.json`
- `PHASE84_87_SAFE_REPORT.md`
- `build_phase84_87_safe.py`
- ZIP SHA-256: `f2b90761aadfa01cb944c597ebb2e1347069a410ceb52e4d35c23e3c0f93c87d`
- ROM SHA-256: `907cac2d6f53ff49627dc1342567344f2ff2b8407060ddd78447b5d21223798f`

## Fases 88–90 — catálogo global
- 559 headers.
- 512/512 event banks.
- 3160 ObjectEvents.
- 1118 warps.
- 114 triggers.
- 1051 script banks.
- 10309 funções de script.
- 624 message banks.
- 589 IDs de script distintos usados por NPCs.
- Nenhum patch de ROM.

Artefatos:
- `phase88_90/global_event_script_catalog.json`
- `phase88_90/PHASE88_90_REPORT.md`
- `build_phase88_90.py`
- ZIP SHA-256: `bf6a2b10254d87b16818f56705fc2257665c8b1d643dd2c063f70d6532722374`

## Fases 91–95 — resolução de mapas
- 204 mapas / 813 objetos / 380 warps.
- Todos os 813 scripts ainda eram END stubs.
- Twinleaf, Route 201 e Sandgem permaneceram sem resolução.
- Jubilife e Oreburgh tinham apenas candidatos estruturais, não prova.
- Nenhum patch.

Artefatos:
- `phase91_95/phase91_95_map_resolution_audit.json`
- `phase91_95/PHASE91_95_REPORT.md`
- ZIP SHA-256: `ad0bd1222ba0fc6dd854d7cc4988ebb1a595bfc0b50825e3747674114ce58f4f`

## Fases 96–100 — grafo
- 8 iterações de propagação de grafo.
- Twinleaf: GBA41 / GBA107 próximos, ambíguo.
- Route201: GBA53 candidato.
- Sandgem: GBA100 / GBA125 próximos, ambíguo.
- Jubilife: GBA112 candidato forte no modelo.
- Oreburgh: GBA3 candidato forte no modelo.
- Caveat: ciclos podem gerar falsos positivos.
- Nenhum patch.

Artefatos:
- `phase96_100/phase96_100_global_graph_candidates.json`
- `phase96_100/PHASE96_100_GRAPH_REPORT.json`
- `phase96_100/PHASE96_100_REPORT.md`
- `build_phase96_100.py`
- ZIP SHA-256: `8dfbf5a5a8dba825d0e968c378277bdacd4792734ff6c30b3a4065302396b44f`

## Fases 101–105 — atribuição global
- Matching one-to-one usado como diagnóstico.
- Todos os cinco pilotos permaneceram sem identidade comprovada.
- Não houve patch de ObjectEvent/script/warp.

Artefatos:
- `phase101_105/PHASE101_105_GLOBAL_ASSIGNMENT.json`
- `phase101_105/PHASE101_105_REPORT.json`
- `phase101_105/PHASE101_105_REPORT.md`
- `build_phase101_105.py`
- ZIP SHA-256: `b159133084dff0c18155fa2b132866167f8dbe4f21db7193d00b7232067b887a`

## Fases 106–110 — consistência bidirecional
- 501 fontes elegíveis.
- K=80 candidatos.
- 4 iterações de arc-consistency.
- 38160 candidatos removidos.
- 24 atribuições globais únicas.
- Twinleaf, Sandgem, Jubilife e Oreburgh ficaram sem candidato após o filtro.
- Route201: GBA53, margem 6, baixa confiança.
- Nenhum patch.
- Gate: AUDIT_ONLY_GRAPH_BIDIRECTIONAL.

Artefatos:
- `phase106_110/PHASE106_110_BIDIRECTIONAL_MATCH.json`
- `phase106_110/PHASE106_110_REPORT.json`
- `phase106_110/PHASE106_110_REPORT.md`
- `build_phase106_110.py`
- ZIP SHA-256: `c09f0cdcfa3377b67f39a3e97de6f6c2486b155c72280e597875bf01b299d79a`

## Fases 111–115 — assinatura de subgrafo local
- 559 headers / 501 fontes elegíveis / 204 mapas GBA.
- K=30.
- 8 iterações de propagação suave.
- Evidência combinada: grau de entrada/saída, vizinhança, geometria, contagens.
- Twinleaf: melhor GBA177, confiança LOW.
- Route201: melhor GBA12, confiança LOW.
- Sandgem: melhor GBA114, confiança LOW.
- Jubilife: melhor GBA117, confiança LOW.
- Oreburgh: melhor GBA129, confiança LOW.
- 0 NPCs/scripts/warps alterados.
- Gate: AUDIT_ONLY_SOFT_BIDIRECTIONAL.

Artefatos:
- `phase111_115/PHASE111_115_LOCAL_GRAPH_MATCH.json`
- `phase111_115/PHASE111_115_REPORT.json`
- `phase111_115/PHASE111_115_REPORT.md`
- `build_phase111_115.py`
- ZIP SHA-256: `8658c2210277cccc4b3e5cc46c497436b74073d35a8f7abd894e0161f04ac1e7`

## Checkpoint crítico preservado
Warp-engine fix obrigatório:
- Offset `0x0DFF3A–0x0DFF3F`
- Bytes `04 1C 00 28 46 D0`

## Estado ao final da fase 115
As fases 81–115 fecharam o diagnóstico estrutural, mas **não fecharam a identidade dos cinco mapas piloto nem produziram uma Sinnoh zerável**. Portanto nenhum artefato desta faixa deve ser apresentado como ROM final.

## Inventário binário local
| Arquivo | Tamanho |
|---|---:|
| sinnoh-reconstruction-phase81-83-mapping.zip | 3,039 B |
| sinnoh-reconstruction-phase84-87-safe-test.zip | 14,539,002 B |
| sinnoh-reconstruction-phase88-90-global-catalog.zip | 99,130 B |
| sinnoh-reconstruction-phase91-95-map-resolution-audit.zip | 1,263 B |
| sinnoh-reconstruction-phase96-100-graph-audit.zip | 14,952 B |
| sinnoh-reconstruction-phase101-105-global-match.zip | 6,158 B |
| sinnoh-reconstruction-phase106-110-bidirectional-audit.zip | 9,630 B |
| sinnoh-reconstruction-phase111-115-subgraph-audit.zip | 48,454 B |
| sinnoh_phase84_87_safe_test.gba | 33,554,432 B |

O repositório deve usar esta documentação como índice de continuidade.