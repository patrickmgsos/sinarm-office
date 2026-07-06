# ADR 0014: Modulos Dependem De Interfaces

## Status

Aceita

## Decisao

Nenhum modulo podera depender diretamente de outro modulo quando houver regra de
negocio ou fronteira de contexto.

Comunicacao entre modulos deve ocorrer por interfaces, services, eventos ou
contratos bem definidos.

## Motivo

Dependencias diretas entre modulos aumentam acoplamento, dificultam testes e
criam risco de mudancas em cascata.

## Consequencias

- Bounded contexts devem ter fronteiras explicitas.
- Repositories e services devem expor contratos claros.
- Eventos de dominio podem comunicar fatos entre contextos.
- Imports cruzados devem ser avaliados com cuidado.
