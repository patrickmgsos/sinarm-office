# Coding Standards

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

## Fluxo Esperado

```text
View
  -> Application Service
    -> Domain Service
      -> Repository
        -> Model
```
