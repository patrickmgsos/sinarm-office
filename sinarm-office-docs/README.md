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
  database/
  diagrams/
  decisions/
  domain/
  erd/
  flows/
  glossary/
  governance/
  milestones/
  modules/
  security/
  use-cases/
  workflow/
  user-manual/
  developer-manual/
  roadmap/
  changelog/
```

## Fase Atual

Fase 1 documental: modelagem de dominio.

Nenhum Model Django de negocio deve ser criado antes da aprovacao da modelagem
DDD, dos casos de uso, dos fluxos, dos diagramas e do modelo de banco.

## Sprint 1

- Dominio DDD.
- Casos de uso UC001-UC010.
- ERD conceitual, logico e fisico.
- Workflows por tipo de processo.
- Glossario.
- Decisoes arquiteturais de produto.

## Sprint 2

Modelagem do Domain Model, ainda sem Django Models:

- Modelo conceitual.
- Modelo logico.
- Modelo fisico.
- Mapeamento DDD.
- Organizacao multiempresa.
- ACL.
- Soft delete.
- Eventos de auditoria.

## Sprint 2.5

Modelo conceitual antes de Django Models:

- ERD.
- Mapa de agregados.
- Bounded Contexts.
- Eventos de dominio.
- Servicos de dominio.
- Matriz ACL/RBAC.

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
