# Sprint Backend 1: Core Platform

## Objetivo

Consolidar a plataforma tecnica compartilhada antes de iniciar qualquer dominio
juridico.

## Escopo

- Apps tecnicos:
  - `core`.
  - `common`.
  - `health`.
  - `identity`.
  - `organization`.
  - `audit`.
  - `configuration`.
  - `notification`.
- Mixins reutilizaveis.
- Excecoes padronizadas.
- Logging estruturado inicial.
- Health checks separados por capacidade.
- Estrutura pronta para auditoria, configuracao, organizacao, identidade e
  notificacao.

## Fora De Escopo

- Customer Domain.
- Firearms Domain.
- Case Management Domain.
- Document Domain.
- Legal Automation Engine funcional.
- Regras juridicas do SINARM.
- APIs publicas de negocio.

## Criterios De Saida

- `python manage.py check` passa.
- Pytest passa para apps tecnicos.
- Ruff, Black e Mypy passam.
- Nenhum model juridico foi criado.
- Architecture Review Backend 1.0 pode ser iniciada.
