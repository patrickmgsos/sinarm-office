# Architecture Principles

## Principios

- Clean Architecture pragmatica.
- DDD orientando modelagem.
- Baixo acoplamento entre modulos.
- Dependencias apontam para dentro do dominio.
- Frameworks ficam nas camadas externas.
- Integracoes externas usam adaptadores.
- Persistencia nao define o dominio.

## Camadas

```text
Domain
  <- Application
    <- Infrastructure
      <- Frameworks
```
