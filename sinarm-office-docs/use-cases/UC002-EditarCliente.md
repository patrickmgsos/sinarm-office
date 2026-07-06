# UC002 - Editar Cliente

## Objetivo

Atualizar dados cadastrais de cliente mantendo rastreabilidade.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Cliente existente.
- Usuario possui permissao para editar clientes.

## Fluxo Principal

1. Usuario acessa cadastro do cliente.
2. Usuario altera dados permitidos.
3. Sistema valida alteracoes.
4. Sistema registra valores alterados.
5. Sistema salva nova versao logica do cadastro quando aplicavel.
6. Sistema registra auditoria.

## Regras De Negocio

- Alteracoes sensiveis devem ser auditadas.
- CPF ou CNPJ nao deve gerar duplicidade.
- Cliente arquivado pode exigir permissao especial para edicao.

## Eventos

- ClienteAtualizado.
- ContatoClienteAtualizado.
