# SINARM Office Docs

Repositorio de documentacao arquitetural, funcional e tecnica do SINARM Office.

Este repositorio deve ser tratado como parte principal do produto. Ele registra
decisoes, regras de negocio, desenho de banco de dados, fluxos operacionais,
politicas de seguranca, manuais, roadmap e changelog.

## Objetivo

Manter uma fonte confiavel de conhecimento para desenvolvimento, auditoria,
onboarding de novos desenvolvedores e evolucao de longo prazo do ERP juridico
SINARM Office.

## Estrutura Inicial

```text
sinarm-office-docs/
  architecture/
  adr/
  business/
  database/
  domain-storytelling/
  diagrams/
  decisions/
  domain/
  erd/
  flows/
  glossary/
  governance/
  milestones/
  modules/
  rules/
  security/
  use-cases/
  workflow/
  user-manual/
  developer-manual/
  roadmap/
  changelog/
```

## Produto

Nome curto: SINARM Office.

Nome interno arquitetural: SINARM Office Platform (SOP).

## Fase Atual

Fase de descoberta encerrada.

Fase atual: Domain Storytelling / Event Storming, ainda sem PostgreSQL, sem
Django Models e sem telas.

Nenhum Model Django de negocio deve ser criado antes da aprovacao da modelagem
DDD, dos casos de uso, dos fluxos, dos diagramas e do modelo de banco.

## Domain Storytelling

Os documentos em `domain-storytelling/` descrevem como aquisicao, renovacao,
transferencia e porte acontecem no mundo real. Eles revelam eventos, comandos,
agregados, filas, notificacoes e pontos de auditoria.

## Sprint 1

- Dominio DDD.
- Casos de uso UC001-UC010.
- ERD conceitual, logico e fisico.
- Workflows por tipo de processo.
- Glossario.
- Decisoes arquiteturais de produto.

## Sprint 2.5

Modelo conceitual antes de Django Models:

- ERD.
- Mapa de agregados.
- Bounded Contexts.
- Eventos de dominio.
- Servicos de dominio.
- Matriz ACL/RBAC.

## Sprint PostgreSQL Logical Model

Os documentos em `database/postgresql/` projetam o banco de dados antes de
qualquer `models.py`:

- Catalogo de tabelas por dominio.
- Estrategia de indices.
- Regras de integridade.
- Checklist da Architecture Review 2.0.

## Camada De Negocio

Os documentos em `business/` descrevem como o mundo juridico-operacional
funciona. Os documentos em `rules/` consolidam regras funcionais que serao
implementadas futuramente no dominio.

## Governanca

Os documentos em `governance/` funcionam como a constituicao tecnica do SINARM
Office: definem como o produto sera construido, evoluido, testado, protegido e
governado.

## Ordem de Desenvolvimento

Toda entrega deve seguir a ordem abaixo:

1. Arquitetura
2. Banco de Dados
3. Models
4. Services
5. Repositories
6. Views
7. APIs
8. Templates
9. Testes
10. Documentacao

## Principios

- Codigo tipado, documentado, testavel e reutilizavel.
- Separacao clara entre dominio, aplicacao, infraestrutura e interface.
- Nenhuma decisao juridica automatizada por IA.
- Toda sugestao gerada por IA deve exigir revisao humana.
- Seguranca, auditoria e LGPD como requisitos estruturais.
