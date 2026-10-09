# Phase 124 — três frentes de compatibilidade

## Etapa 1 — índices de tilesets corrigidos
A auditoria da Phase 123 comparou as referências do tileset secundário somente com os gráficos presentes no arquivo secundário e marcou incorretamente referências como inválidas. A verificação correta para este par considera o conjunto gráfico combinado: tileset primário tem 640 tiles 8×8 4bpp; secundário tem 262; pool combinado = 902. A maior referência encontrada é 901. Portanto, as referências ficam dentro do pool combinado (zero fora do intervalo). Isso remove o falso bloqueio de índices, mas ainda exige validar como a build de origem compartilha/offseta os gráficos.

## Etapa 2 — tabela de mapas da Quetzal
A varredura da ROM BPEE encontra milhares de estruturas que parecem cabeçalhos sob uma heurística de ponteiros. Nenhuma tabela de grupos foi aceita como definitiva porque a heurística produz falsos positivos e a build Quetzal pode alterar a organização. O intervalo final preenchido com FF mede 160.628 bytes, mas não autoriza sozinho a criação de um novo slot de mapa. Resultado: etapa investigada, ponto de inserção ainda NÃO VERIFICADO.

## Etapa 3 — eventos e warps
Foi criado um inventário CSV dos 15 warps com coordenadas, elevação, ID e destinos da ROM-fonte. Os destinos não foram marcados como compatíveis com a Quetzal: IDs de grupo/mapa da ROM Scarlet/Violet não podem ser copiados diretamente para BPEE. É necessário construir a tabela de correspondência de mapas-alvo e implementar os eventos usando o formato do loader real.

## Integridade
- ROM-alvo: BPEE, 32 MiB, SHA-256 `9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f`.
- Nenhum byte da ROM foi alterado.
- Kanto, Johto e Hoenn permanecem intocados.
- Nenhuma ROM jogável é declarada nesta fase; falta confirmar a tabela real e testar o carregamento em emulador.
