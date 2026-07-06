# Coding Standards

## Objetivo

Definir padroes de codigo para quando a implementacao for liberada.

## Padroes

- Python tipado.
- PEP 8.
- Black.
- Ruff.
- Mypy.
- Pytest.
- Docstrings em componentes relevantes.
- Sem codigo morto.
- Sem variaveis magicas.
- Sem regra de negocio em templates.
- Sem regra de negocio em views.

## Organizacao Esperada

```text
View
  -> Application Service
    -> Domain Service
      -> Repository
        -> Model
```

## Regra

Codigo deve seguir os documentos de dominio e ADRs aprovados.
