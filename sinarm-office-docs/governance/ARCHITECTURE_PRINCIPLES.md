# Architecture Principles

## Principios

- Clean Architecture pragmatica.
- DDD orientando modelagem.
- Baixo acoplamento entre modulos.
- Dependencias apontam para dentro do dominio.
- Frameworks ficam nas camadas externas.
- Integracoes externas usam adaptadores.
- Regras de negocio ficam em services e dominio.
- Persistencia nao define o dominio.
- Documentacao precede implementacao em decisoes estruturais.

## Camadas

```text
Domain
  <- Application
    <- Infrastructure
      <- Frameworks
```

## Regra

O dominio nao deve depender de Django, Celery, Redis, DRF ou bibliotecas externas.
