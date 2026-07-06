# Architecture Principles

## Principios

- Clean Architecture pragmatica.
- DDD orientando modelagem.
- Baixo acoplamento entre modulos.
- Isolamento entre dominios de negocio.
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
