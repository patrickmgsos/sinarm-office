# Branching Strategy

## Branches Principais

### main

Contem apenas documentacao consolidada e codigo aprovado.

### architecture

Branch permanente de laboratorio arquitetural.

Nao deve ser mergeada diretamente na `main`. Serve para:

- Estudos.
- ADRs em avaliacao.
- Propostas.
- Prototipos.
- Decisoes arquiteturais.
- Pesquisas.

## Regra

Ideias em discussao devem nascer em `architecture` ou em branches derivadas dela.
Material aprovado deve ser consolidado em branch de entrega propria antes de
chegar a `main`.
