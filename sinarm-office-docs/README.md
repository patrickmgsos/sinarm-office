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
  domain/
  flows/
  modules/
  security/
  use-cases/
  user-manual/
  developer-manual/
  roadmap/
  changelog/
```

## Fase Atual

Fase 1 documental: modelagem de dominio.

Nenhum Model Django de negocio deve ser criado antes da aprovacao da modelagem
DDD, dos casos de uso, dos fluxos, dos diagramas e do modelo de banco.

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
