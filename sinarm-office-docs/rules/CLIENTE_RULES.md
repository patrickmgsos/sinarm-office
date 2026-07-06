# Cliente Rules

## Regras Funcionais

- Cliente deve possuir tipo de pessoa.
- Cliente pessoa fisica deve possuir CPF valido.
- Cliente pessoa juridica deve possuir CNPJ valido.
- CPF deve ser unico por organizacao quando informado.
- CNPJ deve ser unico por organizacao quando informado.
- Telefone principal e obrigatorio.
- Email e opcional, mas deve ser valido quando informado.
- Cliente com processos nao pode ser excluido fisicamente.
- Cliente arquivado deve ser somente leitura, salvo permissao especial.
- Alteracao de dados sensiveis deve gerar auditoria.
