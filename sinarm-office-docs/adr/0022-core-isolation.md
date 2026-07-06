# ADR 0022: Core Isolation

## Status

Aceita

## Contexto

O SINARM Office passou da fase de arquitetura documental para a fase de
engenharia do backend. Antes de criar dominios juridicos como Customer,
Firearms, Cases e Documents, a plataforma precisa de uma base tecnica comum e
reutilizavel.

## Decisao

Nenhum dominio de negocio podera depender diretamente de outro dominio de
negocio.

Exemplos:

- Customer nao depende diretamente de Firearms.
- Firearms nao depende diretamente de Cases.
- Cases nao depende diretamente de Documents.
- Documents nao depende diretamente de Legal Automation.

Dominios de negocio devem se comunicar por servicos de aplicacao, eventos de
dominio, interfaces ou contratos explicitamente definidos.

Apps tecnicos como `core`, `common`, `health`, `identity`, `organization`,
`audit`, `configuration` e `notification` podem fornecer capacidades
transversais, desde que nao contenham regras juridicas do SINARM.

## Motivo

Separar dominios reduz acoplamento, facilita testes, simplifica manutencao e
permite que cada contexto evolua de forma independente.

Essa decisao tambem reforca que o Django sera a base de infraestrutura do
backend, sem ditar a modelagem do dominio juridico.

## Vantagens

- Reduz dependencia circular entre apps.
- Melhora testabilidade.
- Facilita evolucao modular.
- Preserva boundaries de DDD.
- Prepara integracoes futuras por eventos e interfaces.

## Desvantagens

- Exige mais disciplina na criacao de servicos e contratos.
- Pode parecer mais verboso no inicio.
- Requer revisoes arquiteturais para evitar atalhos entre apps.

## Impactos Futuros

- Pull requests de dominios juridicos deverao ser revisados contra esta ADR.
- Imports diretos entre dominios de negocio devem ser tratados como alerta
  arquitetural.
- Eventos e interfaces deverao ser preferidos quando houver colaboracao entre
  dominios.

## Alternativas Rejeitadas

Permitir imports diretos entre apps de negocio foi rejeitado por aumentar o risco
de acoplamento, dependencias circulares e dificuldade de manutencao conforme o
ERP crescer.
