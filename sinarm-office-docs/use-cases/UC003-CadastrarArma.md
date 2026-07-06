# UC003 - Cadastrar Arma

## Objetivo

Cadastrar arma vinculada ao cliente.

## Ator Principal

Usuario interno autorizado.

## Pre-condicoes

- Cliente cadastrado.
- Usuario possui permissao para cadastrar armas.

## Fluxo Principal

1. Usuario seleciona cliente.
2. Usuario informa dados tecnicos da arma.
3. Sistema valida numero de serie.
4. Sistema verifica duplicidade.
5. Sistema cadastra arma vinculada ao cliente.
6. Sistema registra auditoria.

## Regras De Negocio

- Arma pertence ao cliente, nao ao processo.
- Processo apenas utiliza armas do cliente.
- Validade de CRAF deve alimentar agenda quando informada.

## Eventos

- ArmaCadastrada.
- ArmaVinculadaAoCliente.
