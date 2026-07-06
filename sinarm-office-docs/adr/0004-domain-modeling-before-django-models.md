# ADR 0004: Modelagem De Dominio Antes Dos Models Django

## Status

Aceita

## Contexto

O SINARM Office deixou de ser tratado como uma ferramenta interna simples e
passa a ser tratado como produto de software juridico. O risco principal do
projeto nao esta em criar telas, PDFs ou integracoes, mas em modelar mal o
dominio juridico e operacional.

Criar `Models` Django cedo demais poderia cristalizar uma modelagem incompleta,
misturar persistencia com regras de negocio e gerar retrabalho caro quando o
workflow, versionamento documental, auditoria e templates evoluirem.

## Decisao

Congelar temporariamente o desenvolvimento de codigo de aplicacao Django e
priorizar a modelagem completa do dominio usando:

- DDD.
- Casos de uso.
- Diagramas UML.
- Fluxos BPMN ou equivalentes.
- ERD conceitual e logico.
- ADRs.

Nenhum `Model` Django de negocio devera ser criado antes da aprovacao da
modelagem de dominio.

## Por Que Esta Decisao Foi Escolhida

O ERP precisa representar processos administrativos SINARM, documentos,
workflows, prazos, anexos, auditoria, IA assistiva, revisao humana e versoes de
documentos. Esses elementos possuem regras proprias e relacionamento forte entre
si.

Modelar primeiro reduz o risco de o sistema virar apenas um cadastro com status
simples. O objetivo e construir um ERP juridico orientado a processos.

## Vantagens

- Reduz retrabalho futuro.
- Melhora a qualidade dos agregados e invariantes.
- Evita `Models` Django anemicos ou acoplados a telas.
- Ajuda a identificar regras juridicas antes da implementacao.
- Facilita auditoria, LGPD e manutencao.
- Permite desenhar o Workflow Engine e o Time Machine antes da persistencia.

## Desvantagens

- Atrasa a implementacao de funcionalidades visiveis.
- Exige mais disciplina documental.
- Pode gerar discussoes de dominio antes de haver prototipos.
- Requer revisao frequente para manter documentos e codigo alinhados depois.

## Impactos Futuros

O backend devera ser implementado a partir de casos de uso e agregados
aprovados. As tabelas, models, services, repositories, APIs e templates deverao
derivar da modelagem, e nao o contrario.

O Workflow Engine, o Motor de Templates e o Time Machine passam a ser conceitos
centrais do produto.

## Alternativa Rejeitada

Criar imediatamente os `Models` Django e ajustar a modelagem durante a
implementacao.

Essa alternativa foi rejeitada porque aumenta o risco de acoplamento precoce,
status simplificados, documentacao atrasada e perda de qualidade estrutural.
