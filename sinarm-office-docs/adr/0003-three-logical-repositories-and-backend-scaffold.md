# ADR 0003: Tres Repositorios Logicos E Scaffold Do Backend

## Status

Aceita

## Contexto

O SINARM Office sera um ERP juridico de longo prazo, com dominios sensiveis,
documentacao robusta, trilha de auditoria, integracao futura com IA assistiva e
evolucao independente entre backend, frontend e documentacao.

Uma estrutura unica poderia acelerar os primeiros dias do projeto, mas tambem
aumentaria o risco de acoplamento entre regras de negocio, interface, contratos
de API, documentacao e infraestrutura.

## Decisao

Manter tres repositorios logicos:

```text
sinarm-office-backend/
sinarm-office-frontend/
sinarm-office-docs/
```

O projeto Django completo sera criado dentro de:

```text
sinarm-office-backend/
```

Esse diretorio concentrara o backend executavel, incluindo `manage.py`,
`config/`, `apps/`, configuracoes por ambiente, testes, scripts, Docker,
ferramentas de qualidade e documentacao tecnica especifica do backend.

## Por Que Escolhemos Tres Repositorios Logicos

Backend, frontend e documentacao possuem ciclos de vida diferentes. O backend
concentra regras de dominio, persistencia, permissoes, auditoria, APIs e tarefas
assincronas. O frontend concentra experiencia operacional. A documentacao
concentra decisoes, regras, fluxos, manuais e historico arquitetural.

Separar esses componentes facilita governanca, revisao, versionamento,
responsabilidade tecnica e evolucao futura do produto.

## Por Que O Django Ficara Dentro De `sinarm-office-backend/`

Django e a aplicacao de backend. Portanto, suas configuracoes, apps, testes,
dependencias, scripts e infraestrutura devem viver no repositorio logico de
backend. Isso evita que o backend dependa de arquivos espalhados pela raiz do
produto ou pela documentacao.

Essa decisao tambem permite que `sinarm-office-backend/` seja tratado como um
repositorio autonomo no futuro, com CI/CD, Docker, releases e verificacoes
proprias.

## Vantagens

- Separacao clara entre backend, frontend e documentacao.
- Backend preparado para CI/CD independente.
- Documentacao estrategica versionada sem depender do codigo executavel.
- Menor acoplamento entre interface e dominio.
- Melhor organizacao para novos desenvolvedores.
- Possibilidade de evoluir o frontend sem alterar a estrutura do backend.
- Facilidade para transformar o produto em solucao reutilizavel por outros
  escritorios.

## Desvantagens

- Mais disciplina de versionamento entre repositorios logicos.
- Necessidade de documentar contratos entre backend e frontend.
- Mais configuracoes de automacao e CI/CD.
- Maior custo inicial de organizacao.
- Possibilidade de duplicacao de metadados se nao houver padronizacao.

## Impactos Futuros

O backend podera evoluir com APIs versionadas, Celery, Redis, PostgreSQL,
auditoria, workflow e IA assistiva sem exigir reorganizacao estrutural. O
frontend podera ser substituido ou expandido no futuro sem quebrar regras de
dominio. A documentacao podera continuar registrando ADRs, fluxos e regras de
negocio com historico proprio.

Essa estrutura tambem ajuda em auditorias, LGPD, onboarding e manutencao em
horizonte de varios anos.

## Alternativa Rejeitada: Monorepo Unico `sinarm-office/`

Foi considerada a alternativa de manter tudo em um unico repositorio:

```text
sinarm-office/
```

Essa abordagem tem a vantagem de simplicidade inicial, com menos configuracoes e
menos coordenacao entre partes. Porem, foi rejeitada porque tende a misturar
documentacao estrategica, backend, frontend, infraestrutura e regras de negocio
em uma mesma arvore de responsabilidade.

Para um ERP juridico sensivel e duradouro, o custo inicial menor do monorepo nao
compensa o risco futuro de acoplamento, crescimento desorganizado e dificuldade
de manutencao.
