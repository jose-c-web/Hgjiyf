# Sinnoh — fases 106–115

Branch de continuidade: `sinnoh-phases-106-115`

Esta branch preserva a auditoria das fases mais recentes sem modificar a `main`.

## Checkpoint
- ROM-base de identidade/scripts: `sinnoh_step45d_fixed.gba`
- SHA-256: `66bc1619a72da36b24f09f7eacc72a87e4d662ee24195319e8cfe01c3467be23`
- Warp-fix obrigatório: offset `0x0DFF3A–0x0DFF3F` = `04 1C 00 28 46 D0`
- Fases 106–110: auditoria bidirecional, sem patch.
- Fases 111–115: assinatura de subgrafo local, sem patch.
- Próximo passo correto: obter identidade direta GBA↔Pearl por metadados de mapas/geometria, antes de ligar NPCs/scripts.

## Artefatos locais correspondentes
- `build_phase106_110.py`
- `build_phase111_115.py`
- `phase106_110/PHASE106_110_REPORT.json`
- `phase106_110/PHASE106_110_BIDIRECTIONAL_MATCH.json`
- `phase111_115/PHASE111_115_REPORT.json`
- `phase111_115/PHASE111_115_LOCAL_GRAPH_MATCH.json`

## Zips
- `sinnoh-reconstruction-phase106-110-bidirectional-audit.zip`
- `sinnoh-reconstruction-phase111-115-subgraph-audit.zip`

Os relatórios desta branch são auditoria: não declarar Sinnoh jogável/zerável a partir dessas fases, porque os cinco mapas-piloto ainda não têm identidade confiável.
