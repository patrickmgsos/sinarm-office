# ADR 0025: Thin Models, Rich Domain Services

## Status

Aceita

## Contexto

O projeto usa Django ORM para persistencia, mas a arquitetura definida nas ADRs
anteriores evita colocar regra de negocio em views, templates ou detalhes de
framework. Com a entrada dos dominios de negocio, e necessario explicitar onde as
regras vivem.

Models Django sao importantes para estrutura, constraints, relacionamentos e
persistencia. Entretanto, models carregados com regras complexas tendem a ficar
dificeis de testar, reutilizar e evoluir.

## Decisao

Models devem permanecer finos.

Models podem conter:

- campos;
- constraints;
- indices;
- relacionamentos;
- metodos simples de apresentacao;
- pequenas garantias locais quando forem inerentes ao proprio dado.

Regras de negocio complexas devem ficar em:

- services;
- policies;
- specifications.

Casos de uso devem ser expressos por services com nomes de negocio, por exemplo
`register_new_customer`, e nao como CRUD generico.

## Motivo

Separar persistencia de comportamento de dominio reduz acoplamento com Django,
melhora testabilidade e preserva a linguagem do escritorio nos casos de uso.

## Vantagens

- Services ficam alinhados a capacidades de negocio.
- Models permanecem previsiveis e simples.
- Policies e specifications podem crescer sem inflar o ORM.
- Facilita evoluir para APIs, tarefas assincronas e eventos.
- Mantem coerencia com ADR-0011 e ADR-0012.

## Desvantagens

- Pode haver mais arquivos por dominio.
- Regras pequenas exigem julgamento para nao fragmentar demais.
- A equipe deve evitar voltar a escrever CRUD generico em services.

## Impactos Futuros

- Customer Domain deve iniciar com `Register New Customer`.
- Firearm Domain deve iniciar com casos de uso como `Register Firearm From CRAF`,
  quando chegar sua fase.
- Reviews devem avaliar se services expressam capacidades de negocio.

## Alternativas Rejeitadas

Fat Models foram rejeitados por acoplar regras de negocio ao ORM.

CRUD Services genericos foram rejeitados por nao expressarem a linguagem do
escritorio nem protegerem invariantes de agregados.
