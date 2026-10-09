# Phase 120 — primeiro protótipo de mapa (isolado)

## Mapa escolhido
- ID técnico: `g03_m010`
- Grupo/mapa: `3/10`
- Dimensões: 66 × 55 metatiles
- Tilesets fonte: primário `0x82d4a94`, secundário `0x82d4b9c`
- Warps: 15
- Objetos/eventos: 15 objetos, 9 eventos de fundo
- Grade fonte extraída sem reinterpretar os IDs.

## Integridade e compatibilidade
- Scarlet/Violet SHA-256: `ecf6738f537e3842b9f187880fc2617b9aebe4f6a178be13ed25d3f85edefb6e`
- Quetzal SHA-256: `9883aebc24ac670d2be50a1cc5ce9a652752782a55fed22c4f74ed523197ee3f`
- Quetzal: 33.554.432 bytes; código `BPEE`.
- IDs de metatile referenciam os tilesets da ROM fonte e não podem ser copiados numericamente como IDs Quetzal.

## Resultado
O pacote isolado contém a grade binária original, borda, preview, inventário de warps/eventos, índice de mapas e referência aos quatro layouts com falhas. **Este ainda não é um mapa convertido para Quetzal**: falta estabelecer a correspondência visual de metatiles, colisões e IDs de destino antes de escrever dados na ROM. Nenhuma ROM foi modificada.

## Próximo passo
Construir o crosswalk entre metatiles usados neste mapa e os tilesets reais da Quetzal; validar comportamentos de colisão; depois criar um patch separado e testar integridade e inicialização em emulador.
