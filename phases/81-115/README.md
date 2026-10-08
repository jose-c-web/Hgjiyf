# Pokémon Quetzal / Sinnoh — Histórico das Fases 81–115

Arquivo de continuidade do projeto de reconstrução de Sinnoh sobre a ROM GBA baseada em Pokémon Quetzal/Emerald.

## Escopo
- Fases 81–83: catálogo de mapeamento estrutural.
- Fases 84–87: teste seguro de ligação de scripts a NPCs.
- Fases 88–90: catálogo global de eventos e scripts.
- Fases 91–95: auditoria de resolução de mapas.
- Fases 96–100: auditoria de grafo e propagação.
- Fases 101–105: atribuição global one-to-one (diagnóstica).
- Fases 106–110: auditoria bidirecional com consistência de arco.
- Fases 111–115: assinatura de subgrafo/local graph match.

## Regra importante
As fases 81–115 foram majoritariamente **auditorias e diagnóstico**, não devem ser tratadas como prova de identidade dos NPCs. O patch de warp-engine que precisa ser preservado é:

`0x0DFF3A–0x0DFF3F = 04 1C 00 28 46 D0`

## ROMs/checkpoints
- `sinnoh_phase84_87_safe_test.gba`: checkpoint de teste seguro, 32 MiB.
- A ROM final zerável ainda não deve ser declarada concluída apenas com estas fases.

## Organização
`phases/81-83`, `84-87`, `88-90`, `91-95`, `96-100`, `101-105`, `106-110`, `111-115`.

Os ZIPs e arquivos maiores ficam registrados por nome, tamanho e SHA quando a transferência direta pelo conector não é adequada.
