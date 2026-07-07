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
  -> API
    -> Service
      -> Repository
        -> Model
```

## Padrao De Dominio

Novos dominios devem organizar responsabilidades por arquivo:

- `models.py`: estrutura, constraints, indices, relacionamentos e persistencia.
- `services.py`: casos de uso, transacoes e regras de negocio.
- `repositories.py`: leitura/escrita persistente usada por services.
- `selectors.py`: queries de leitura para apresentacao, relatorios e telas.
- `policies.py`: decisoes de permissao ou regra contextual, quando necessario.
- `specifications.py`: regras booleanas reutilizaveis, quando necessario.

Services devem falar a linguagem do negocio. Evitar CRUD generico como padrao de
caso de uso.

Exemplos preferidos:

- `register_new_customer`.
- `change_customer_address`.
- `register_firearm_from_craf`.

Exemplos rejeitados como linguagem principal:

- `create_customer`.
- `update_address`.
- `create_firearm`.

## Agregados

Alteracoes em entidades internas de um agregado devem passar pelo Aggregate Root
ou por um service responsavel pelo agregado.

Nao usar `GenericForeignKey` para modelar relacoes de dominio. Preferir
relacionamentos explicitos, com integridade, indices e tipagem claros.
