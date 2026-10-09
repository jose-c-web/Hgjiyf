# Phase 122 — pacote de importação de mapa e tilesets

## Objetivo
Preparar `g03_m010` para futura inserção na build Quetzal BPEE sem tocar nos mapas já existentes de Kanto, Johto e Hoenn.

## Resultado
- Grade de 66×55 = 3.630 células, preservando palavras little-endian de 16 bits.
- IDs de metatile (10 bits), colisão (2 bits) e elevação (4 bits) separados.
- Dois tilesets de origem incluídos com tiles 4bpp, paletas, metatiles e atributos.
- Manifesto com 15 warps e CSV por célula.
- SHA-256 dos recursos copiados para auditoria.

## Estratégia
Em vez de adivinhar equivalências visuais com tilesets de Kanto/Johto/Hoenn, o pacote preserva os dois tilesets referenciados pelo mapa de origem. IDs 0–511 são tratados como primários e 512–1023 como secundários. Isso evita substituir gráficos por aproximações.

## Validação estática
- 3.630 palavras de 16 bits, 7.260 bytes.
- Todos os IDs normalizados no intervalo 0–1023.
- 319 IDs distintos; máximo 839.
- 2.225 células usam IDs primários; 1.405 secundários.
- 15 warps mantidos no manifesto.

## Limite atual
O ZIP é um pacote de assets pronto para integração, não uma ROM modificada. Ainda é necessário registrar uma entrada de mapa na tabela de mapas Quetzal, adaptar/validar cabeçalhos e eventos/scripts, ligar destinos dos warps a mapas reais e confirmar em emulador que o loader BPEE interpreta os tilesets do mesmo modo. A build tem 160.628 bytes de `0xFF` contínuos no fim da ROM, mas isso não prova que a região seja segura nem que os dados possam ser referenciados pelo código.

Nenhum byte da ROM Quetzal foi alterado. Kanto, Johto e Hoenn permanecem intocados. Não foi realizado teste de jogo em emulador.