# Arquitetura

## Decisao Inicial

O SINARM Office sera organizado como um produto profissional composto por tres
repositorios logicos:

```text
sinarm-office-backend/
sinarm-office-frontend/
sinarm-office-docs/
```

## Por Que Esta Arquitetura Foi Escolhida

O ERP possui varios dominios de negocio, integra dados sensiveis, exige trilha
de auditoria, controle de permissoes, documentacao juridica e uso assistido de
IA. Separar backend, frontend e documentacao reduz acoplamento e permite que
cada parte evolua com ciclo proprio.

## Vantagens

- Clareza de responsabilidade entre API, interface e conhecimento do produto.
- Documentacao versionada independentemente do codigo.
- Melhor governanca para ADRs, fluxos, regras de negocio e manuais.
- Facilidade para evoluir o frontend sem comprometer regras de dominio.
- Preparacao para CI/CD separado por componente.
- Melhor onboarding de novos desenvolvedores.

## Desvantagens

- Maior custo inicial de organizacao.
- Necessidade de coordenar versoes entre API e frontend.
- Mais configuracoes de CI/CD, releases e ambientes.
- Exige disciplina para manter contratos e documentacao atualizados.

## Impacto Futuro

Esta decisao favorece manutencao em horizonte de varios anos, facilita auditoria
e permite transformar o sistema em produto para outros escritorios. Tambem reduz
o risco de regras juridicas ficarem misturadas com templates, views ou detalhes
de infraestrutura.

## Alternativas Consideradas

### Monorepo

Um unico repositorio para backend, frontend e documentacao.

Vantagem: menor complexidade inicial.

Desvantagem: maior risco de acoplamento e crescimento desorganizado.

### Django Full Stack Unico

Backend Django servindo paginas, APIs, templates e documentacao no mesmo
repositorio.

Vantagem: desenvolvimento inicial mais rapido.

Desvantagem: menos flexivel para crescimento, times independentes, versionamento
de contratos e evolucao futura da interface.

## Estilo Arquitetural Do Backend

O backend deve usar Django 5 com uma organizacao inspirada em Clean Architecture
e DDD pragmatico:

```text
apps/
  <bounded_context>/
    domain/
    application/
    infrastructure/
    interfaces/
    tests/
core/
config/
```

Cada modulo deve evitar logica de negocio em views, serializers ou templates.
Regras relevantes devem ficar em services de aplicacao e objetos de dominio.
