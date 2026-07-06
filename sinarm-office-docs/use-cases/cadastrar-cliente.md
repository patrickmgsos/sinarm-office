# Caso De Uso: Cadastrar Cliente

## Objetivo

Registrar um cliente com dados suficientes para iniciar processos SINARM.

## Atores

- Usuario interno autorizado.

## Pre-condicoes

- Usuario autenticado.
- Empresa ativa.

## Fluxo Principal

1. Usuario informa dados cadastrais.
2. Sistema valida documento principal.
3. Sistema verifica possivel duplicidade.
4. Sistema registra cliente.
5. Sistema cria evento de auditoria.

## Regras

- Cliente duplicado deve ser sinalizado antes da gravacao.
- Campos sensiveis devem ser auditaveis.
