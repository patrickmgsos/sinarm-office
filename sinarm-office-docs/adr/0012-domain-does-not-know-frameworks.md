# ADR 0012: Dominio Nao Conhece Frameworks

## Status

Aceita

## Decisao

O dominio nao dependera de frameworks.

```text
Domain
  -> Application
    -> Infrastructure
      -> Django
```

Django, DRF, Celery, Redis e bibliotecas externas pertencem a camadas externas.

## Motivo

O dominio deve representar regras juridicas e operacionais duradouras. Frameworks
podem mudar; o dominio deve permanecer estavel.

## Consequencias

- Entidades e regras de dominio nao importam Django.
- Application services coordenam casos de uso.
- Infrastructure implementa repositories, adapters e persistencia.
- Django Models ficam como detalhe de persistencia.
