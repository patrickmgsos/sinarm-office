# Caso De Uso: Cadastrar Arma

## Objetivo

Registrar uma arma vinculada a um cliente para uso em processos administrativos
SINARM.

## Atores

- Usuario interno autorizado.

## Fluxo Principal

1. Usuario seleciona cliente.
2. Usuario informa dados tecnicos da arma.
3. Sistema valida numero de serie e dados obrigatorios.
4. Sistema verifica possivel duplicidade.
5. Sistema registra arma.
6. Sistema cria evento de auditoria.

## Regras

- Numero de serie deve ser rastreavel.
- Arma pode existir sem processo aberto.
- Dados de validade devem alimentar alertas quando aplicavel.
