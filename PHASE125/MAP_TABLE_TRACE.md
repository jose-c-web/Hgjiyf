# Phase 125 — Rastreamento da tabela de grupos de mapas

## Descoberta principal
A varredura da ROM BPEE encontrou um conjunto altamente estruturado de 57 ponteiros consecutivos em torno do offset de arquivo `0x91F240`. Os destinos cobrem estruturas relacionadas a mapas na região `0x91DE30–0x91F1F0`. O conjunto inclui listas de ponteiros para cabeçalhos que passam pela validação cruzada com estruturas de layout (largura/altura plausíveis e ponteiros para borda/dados), além de séries de cabeçalhos com stride de 28 bytes.

## Evidências de cabeçalhos
Foram detectadas nove sequências de cabeçalhos plausíveis com stride de 28 bytes. As maiores têm 307, 246, 233, 170 e 105 entradas. Cada cabeçalho candidato aponta para um layout estruturalmente plausível; isso é evidência forte de uma tabela real de mapas, embora a identificação sem símbolos/execução não prove por si só qual função de código consome o bloco.

A sequência de cabeçalhos no offset `0x915EC4` tem 33 entradas consecutivas e um vetor de ponteiros correspondente perto de `0x91E00C`. Outros vetores de cabeçalhos são referenciados perto de `0x91F240`.

## O que foi e não foi resolvido
- Resolvido: a ROM contém estruturas reais e repetidas de cabeçalhos/layouts; a busca não precisa continuar às cegas por todo o binário.
- Parcial: `0x91F240` é um candidato de alta confiança a uma tabela de ponteiros de grupos/coleções de mapas, mas a função consumidora e a semântica de todos os 57 itens não foram provadas apenas por análise estática.
- Não resolvido: não foi escolhido um novo slot nem alterada a tabela. Inserir um grupo exige confirmar o consumidor da tabela, limite de grupos/mapas, uso dos índices de saveblock e referências em código.

## Proteção
A ROM Quetzal de 32 MiB (SHA-256 `9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f`) permanece byte a byte inalterada. Nenhum patch é declarado jogável. Kanto, Johto e Hoenn não foram tocados.

## Próximo passo
Usar referências de código ARM/Thumb para `0x91F240` e seus destinos, validar a tabela pelo caminho de carregamento de mapas, e confirmar se a build permite ampliar grupos sem modificar código. Só depois disso criar patch em cópia e rodar em emulador.