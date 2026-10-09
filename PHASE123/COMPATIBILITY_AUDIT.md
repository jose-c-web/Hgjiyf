# Phase 123 — Auditoria de compatibilidade da conversão

## Resultado
A auditoria automatizada da ROM Quetzal (BPEE, 32 MiB) encontrou uma área final preenchida por `0xFF` de 160.628 bytes, do offset `0x1FD8C8C` até `0x2000000`. Isso é apenas um candidato a espaço livre, não uma garantia de que possa ser usado sem conflito.

O layout-fonte tem 66×55 células (3.630 células) e 15 warps. Os dois tilesets têm 512 definições de metatile e 512 entradas de atributos cada. Porém, a checagem dos índices de tiles gráficos não fecha para a conversão: as definições referenciam IDs maiores que a quantidade de tiles gráficos extraídos em pelo menos um dos tilesets. Isso pode ser semântica de índice compartilhado ou extração incompleta; precisa ser resolvido antes de gravar o mapa.

## Por que ainda não é seguro criar uma ROM jogável
1. Ainda não foi validada a tabela de grupos/mapas específica da build Quetzal para registrar o novo mapa.
2. A contagem de tiles gráficos e os índices referenciados precisam concordar com o modelo de tileset da ROM-fonte.
3. O mapa precisa ter cabeçalho/layout/eventos/warps registrados com ponteiros GBA válidos e compatíveis com o loader BPEE.
4. A existência de uma área `0xFF` não demonstra que todo o intervalo seja livre nem que o jogo suporte a adição sem modificar tabelas/código.

## Proteções aplicadas
- ROM original preservada e não modificada.
- Nenhum patch de aparência foi declarado como jogável.
- Não foram alteradas regiões existentes (incluindo Kanto, Johto e Hoenn).

## Próxima resolução técnica
Validar o formato dos metatiles e os índices de tile contra os bytes originais da ROM BPRE, reconstruir corretamente os gráficos/tilesets, identificar a tabela de mapas da build BPEE e só então montar um patch em cópia, com checksums e verificação de ponteiros. Teste em emulador continua obrigatório para afirmar jogabilidade.