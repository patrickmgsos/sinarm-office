# ADR 0023: Domain Package Independence

## Status

Aceita

## Contexto

Com a Core Platform aprovada pela Architecture Review Backend 1.0, o SINARM
Office entra na etapa de implementacao dos dominios tecnicos e, posteriormente,
dos dominios juridicos.

Para preservar modularidade, cada dominio deve ser tratado como pacote
independente, e nao apenas como uma pasta Django compartilhando detalhes internos
com outras apps.

## Decisao

Cada dominio deve ser desenvolvivel, testavel e evoluivel de forma isolada.

Um pacote de dominio deve concentrar suas proprias responsabilidades:

- Models.
- Services.
- Selectors.
- Repositories.
- Permissions.
- Serializers e APIs.
- Tests.
- Documentacao tecnica local quando necessaria.

Dominios nao devem acessar detalhes internos de outros dominios diretamente.
Quando houver colaboracao entre dominios, ela deve ocorrer por servicos de
aplicacao, eventos, interfaces ou contratos explicitos.

## Motivo

Pacotes independentes reduzem acoplamento, facilitam testes, tornam revisoes mais
objetivas e preservam a capacidade do produto evoluir por muitos anos sem
reescrita estrutural.

## Vantagens

- Cada dominio pode ter testes, APIs e permissoes proprias.
- Mudancas ficam mais localizadas.
- Reduz risco de dependencias circulares.
- Facilita ownership tecnico por modulo.
- Reforca DDD e bounded contexts.

## Desvantagens

- Pode gerar mais arquivos por dominio.
- Exige disciplina para evitar imports diretos entre pacotes.
- Alguns fluxos exigirao contratos explicitos antes da implementacao.

## Impactos Futuros

- Pull requests de dominio devem declarar quais boundaries foram tocados.
- Backend Review 2.0 deve verificar dependencias, imports e independencia dos
  pacotes.
- Testes de arquitetura poderao ser criados para impedir dependencias proibidas.

## Alternativas Rejeitadas

Usar apps Django como simples agrupamentos tecnicos foi rejeitado por incentivar
compartilhamento informal de models, services e regras internas entre dominios.

Centralizar regras de varios dominios em uma app unica tambem foi rejeitado por
aumentar acoplamento e dificultar manutencao.
