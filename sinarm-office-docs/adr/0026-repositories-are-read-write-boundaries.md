# ADR 0026: Repositories Are Read/Write Boundaries

## Status

Aceita

## Contexto

As primeiras sprints consolidaram `services.py` e `selectors.py`. Essa divisao
foi suficiente para dominios tecnicos e dados de referencia. A partir dos
dominios de negocio, os services precisarao coordenar casos de uso e invariantes
de agregados sem espalhar detalhes de persistencia.

Se services chamarem `Model.objects.filter(...)` livremente, a camada de dominio
passa a conhecer detalhes de consulta e escrita do ORM, dificultando testes,
mudancas e revisoes arquiteturais.

## Decisao

Dominios de negocio devem possuir `repositories.py`.

Fluxo esperado:

```text
View
  -> API
    -> Service
      -> Repository
        -> Model
```

Services nao devem depender diretamente de `Model.objects.filter(...)` para
operacoes de persistencia do caso de uso. Essas operacoes devem passar por
repositories.

`selectors.py` continua existindo para queries de leitura e apresentacao,
especialmente quando a consulta nao representa uma escrita ou decisao de dominio.

## Responsabilidades Por Arquivo

- `models.py`: estrutura, constraints, indices, relacionamentos e persistencia.
- `services.py`: casos de uso, transacoes e regras de negocio.
- `repositories.py`: fronteira de leitura/escrita persistente usada por services.
- `selectors.py`: queries de leitura para apresentacao, relatorios e telas.
- `policies.py`: decisoes de permissao ou regra contextual.
- `specifications.py`: regras booleanas reutilizaveis e combinaveis.

## Motivo

Repositories tornam explicita a fronteira entre caso de uso e persistencia. Isso
facilita testes, reduz acoplamento ao ORM e permite revisar queries e escritas
como parte da arquitetura do dominio.

## Vantagens

- Services ficam mais focados em linguagem de negocio.
- Persistencia fica concentrada e testavel.
- Reduz duplicacao de queries.
- Melhora a capacidade de substituir ou otimizar consultas.
- Facilita auditar dependencias entre dominios.

## Desvantagens

- Mais um arquivo por dominio.
- Requer disciplina para nao transformar repository em camada anemica sem
  criterio.
- Pode ser excesso para apps puramente tecnicos simples; a obrigatoriedade vale
  principalmente para dominios de negocio.

## Impactos Futuros

- Customer Domain deve incluir `repositories.py` desde o primeiro caso de uso.
- Services de Customer devem chamar repositories para persistencia.
- Selectors devem ficar separados de repositories quando a intencao for leitura
  para apresentacao.

## Alternativas Rejeitadas

Permitir ORM livre dentro de services foi rejeitado por misturar caso de uso e
persistencia.

Usar apenas selectors para leitura e escrita foi rejeitado porque selectors
devem permanecer orientados a consulta/apresentacao.
