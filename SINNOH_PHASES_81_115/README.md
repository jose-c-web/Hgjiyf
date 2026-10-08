# Sinnoh — Histórico completo disponível das fases 81–115

Este diretório organiza a continuidade técnica das fases 81–115. As fases foram executadas como auditorias progressivas e, quando indicado, não aplicaram patch de NPC/script/map identity.

## 81–83 — catálogo de mapeamento
- 559 headers Pearl, 512 bancos de eventos, 204 mapas GBA.
- Pilotos analisados: Twinleaf, Route 201, Sandgem, Jubilife, Oreburgh.
- Gate: nenhum ObjectEvent/script alterado.
- ZIP local: `sinnoh-reconstruction-phase81-83-mapping.zip`
- Script: `build_phase81.py`

## 84–87 — teste seguro
- ROM de teste: `sinnoh_phase84_87_safe_test.gba`
- SHA-256: `907cac2d6f53ff49627dc1342567344f2ff2b8407060ddd78447b5d21223798f`
- 193 mapas com NPCs receberam um link de script de teste.
- 380 warps foram preservados/revalidados.
- Resultado NÃO prova identidade correta dos NPCs.
- ZIP local: `sinnoh-reconstruction-phase84-87-safe-test.zip`

## 88–90 — catálogo global
- 559 headers, 512/512 bancos de eventos, 3160 ObjectEvents, 1118 warps, 114 triggers.
- 1051 bancos de script, 10309 funções de script, 624 bancos de mensagens.
- 589 IDs distintos de script usados por NPCs.
- ZIP local: `sinnoh-reconstruction-phase88-90-global-catalog.zip`

## 91–95 — resolução de mapas
- 204 mapas, 813 objetos, 380 warps.
- Todos os 813 scripts continuavam como END stubs.
- Twinleaf/Route201/Sandgem permaneceram sem resolução.
- Jubilife e Oreburgh apenas candidatos estruturais, não provados.
- ZIP local: `sinnoh-reconstruction-phase91-95-map-resolution-audit.zip`

## 96–100 — grafo global
- 8 iterações de propagação no grafo de warps.
- Twinleaf: GBA41 score 92, margem 5.
- Route201: GBA53 score -8, margem 13.
- Sandgem: GBA100 score 206, margem 4.
- Jubilife: GBA112 score 503, margem 146.
- Oreburgh: GBA3 score 568, margem 88.
- Caveat: ciclos podem gerar falsos positivos.
- ZIP local: `sinnoh-reconstruction-phase96-100-graph-audit.zip`

## 101–105 — atribuição global
- Diagnóstico one-to-one global, sem patch.
- Todos os cinco pilotos permaneceram não resolvidos.
- Melhores candidatos:
  - Twinleaf: 91/102/123/111/50...
  - Route201: 53/12/112/101...
  - Sandgem: 105/3/112/114...
  - Jubilife: 121/117/110/124...
  - Oreburgh: 121/100/86/129...
- ZIP local: `sinnoh-reconstruction-phase101-105-global-match.zip`

## 106–110 — auditoria bidirecional
- 501 fontes elegíveis, 204 mapas GBA.
- K=80 candidatos, 4 iterações de consistência de arco.
- 38160 candidatos removidos.
- 24 atribuições globais únicas.
- Twinleaf/Sandgem/Jubilife/Oreburgh: NO_CANDIDATE.
- Route201: GBA53, margem 6, confiança LOW.
- Gate: AUDIT_ONLY_GRAPH_BIDIRECTIONAL.
- ZIP local: `sinnoh-reconstruction-phase106-110-bidirectional-audit.zip`

## 111–115 — subgrafo local
- Assinatura local de subgrafos, grau in/out, 8 iterações de propagação suave, geometria e contagens.
- Twinleaf: GBA177, margem 5, LOW.
- Route201: GBA12, margem 3, LOW.
- Sandgem: GBA114, margem 1, LOW.
- Jubilife: GBA117, margem 7, LOW.
- Oreburgh: GBA129, margem 1, LOW.
- Nenhum NPC/script/warp alterado.
- Gate: AUDIT_ONLY_SOFT_BIDIRECTIONAL.
- ZIP local: `sinnoh-reconstruction-phase111-115-subgraph-audit.zip`

## Checkpoint de continuidade
Base validada: `sinnoh_step45d_fixed.gba`
SHA-256: `66bc1619a72da36b24f09f7eacc72a87e4d662ee24195319e8cfe01c3467be23`
Warp-engine fix obrigatório em 0x0DFF3A–0x0DFF3F:
`04 1C 00 28 46 D0`

## Observação sobre binários
Os artefatos ZIP/ROM foram gerados nesta sessão. Os arquivos de histórico textual e scripts estão sendo versionados neste diretório. Os binários grandes devem ser tratados como artefatos de build/LFS, não como blobs Git comuns.
