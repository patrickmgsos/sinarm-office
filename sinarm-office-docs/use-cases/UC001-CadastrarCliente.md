# UC001 - Cadastrar Cliente

## Objetivo

Cadastrar pessoa fisica ou juridica atendida pelo escritorio.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Usuario autenticado.
- Empresa ativa.
- Usuario possui permissao para cadastrar clientes.

## Fluxo Principal

1. Usuario informa tipo de pessoa.
2. Usuario informa dados cadastrais.
3. Sistema valida CPF ou CNPJ.
4. Sistema valida telefone principal.
5. Sistema verifica duplicidade.
6. Sistema cadastra cliente.
7. Sistema registra auditoria.

## Regras De Negocio

- CPF ou CNPJ deve ser unico por empresa.
- Telefone principal e obrigatorio.
- Email e opcional, mas deve ser valido quando informado.
- Cliente duplicado deve ser sinalizado antes da gravacao.

## Eventos

- ClienteCadastrado.
- DuplicidadeClienteDetectada.
