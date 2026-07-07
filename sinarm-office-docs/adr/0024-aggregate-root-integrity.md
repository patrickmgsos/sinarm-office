# ADR 0024: Aggregate Root Integrity

## Status

Aceita

## Contexto

Ate a Backend Review 3.0, o projeto consolidou fundacao tecnica, servicos de
plataforma e dados de referencia. A partir do Backend 4, o sistema comeca a
implementar dominios de negocio reais, iniciando por Customer Domain.

Customer sera um Aggregate Root. Enderecos, contatos, documentos, tags e eventos
de timeline deverao evoluir como partes do agregado, e nao como entidades soltas
manipuladas diretamente por qualquer camada.

Sem uma regra explicita, alteracoes em objetos internos do agregado podem
contornar invariantes, auditoria, politicas e validacoes do dominio.

## Decisao

Toda alteracao em um agregado deve passar pelo Aggregate Root ou por um service
de dominio/aplicacao responsavel pelo agregado.

Codigo de aplicacao nao deve criar ou alterar entidades internas diretamente.

Exemplo rejeitado:

```python
CustomerAddress.objects.create(...)
```

Exemplos aceitos:

```python
customer.add_address(...)
```

```python
CustomerService.add_address(...)
```

Enquanto o agregado ainda nao possuir determinada entidade interna, nenhum atalho
de persistencia deve ser criado.

## Motivo

Aggregate Roots protegem invariantes. Quando cada parte do agregado pode ser
alterada isoladamente, a regra de negocio fica espalhada, as transacoes perdem
coerencia e o codigo volta a parecer CRUD.

## Vantagens

- Protege invariantes do dominio.
- Reduz duplicacao de validacoes.
- Facilita auditoria de mudancas importantes.
- Mantem linguagem de negocio nos casos de uso.
- Evita escrita direta em entidades internas do agregado.

## Desvantagens

- Pode exigir services mais explicitos.
- Algumas operacoes simples terao mais cerimonia.
- Testes precisam cobrir o comportamento do agregado, nao apenas inserts.

## Impactos Futuros

- Customer Address, Contact, Document, Tag e Timeline deverao ser adicionados por
  casos de uso do Customer Aggregate.
- Firearm e futuros agregados deverao seguir o mesmo principio.
- Reviews de backend devem procurar escritas diretas em entidades internas.

## Alternativas Rejeitadas

Permitir que qualquer service crie entidades internas diretamente foi rejeitado
por enfraquecer o agregado.

Usar `GenericForeignKey` para associar eventos ou anexos genericos tambem foi
rejeitado para preservar integridade, indices, consultas e tipagem.
