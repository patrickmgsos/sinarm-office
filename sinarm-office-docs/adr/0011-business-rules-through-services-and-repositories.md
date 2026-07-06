# ADR 0011: Regras De Negocio Fora Dos Models Django

## Status

Aceita

## Decisao

Nenhum Model Django podera acessar outro Model diretamente quando existir uma
regra de negocio envolvida.

O fluxo padrao sera:

```text
View
  -> Application Service
    -> Domain Service
      -> Repository
        -> Model
```

## Motivo

Models Django representam persistencia e invariantes simples. Regras de negocio
devem ficar centralizadas, testaveis e desacopladas de views, templates,
serializers e detalhes de ORM.

## Consequencias

- Casos de uso relevantes devem ter services.
- Consultas complexas devem passar por repositories ou selectors.
- Models nao devem orquestrar workflows, documentos ou IA.
- Testes de dominio ficam mais simples e previsiveis.
