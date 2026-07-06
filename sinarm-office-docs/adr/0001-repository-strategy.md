# ADR 0001: Estrategia De Repositorios

## Status

Aceita

## Contexto

O SINARM Office sera um ERP juridico completo para gestao de processos
administrativos perante a Policia Federal. O produto deve ser mantido por muitos
anos, conter dados sensiveis e possuir documentacao robusta.

## Decisao

Adotar tres repositorios logicos desde o inicio:

```text
sinarm-office-backend/
sinarm-office-frontend/
sinarm-office-docs/
```

## Consequencias Positivas

- Separacao clara de responsabilidades.
- Documentacao com historico proprio.
- Melhor governanca de arquitetura e regras de negocio.
- Preparacao para evolucao futura como produto profissional.

## Consequencias Negativas

- Mais repositorios para administrar.
- Necessidade de padronizar releases, contratos e ambientes.
- Maior custo inicial de setup.

## Alternativas

- Monorepo.
- Django full stack em repositorio unico.
- Backend e frontend separados, mas documentacao dentro do backend.
