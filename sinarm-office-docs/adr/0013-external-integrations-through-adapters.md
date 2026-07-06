# ADR 0013: Integracoes Externas Por Adaptadores

## Status

Aceita

## Decisao

Toda integracao externa sera feita por adaptadores.

Exemplos:

- OpenAI.
- Gemini.
- Ollama.
- WhatsApp.
- Email.
- Assinatura digital.

Nenhum servico externo deve ser chamado diretamente pelo dominio.

## Motivo

Adaptadores reduzem acoplamento, facilitam testes, permitem troca de provedores
e isolam falhas externas.

## Consequencias

- Dominio define interfaces.
- Infrastructure implementa adaptadores.
- Testes podem usar fakes ou mocks.
- Troca de fornecedor nao deve exigir mudanca nas regras de dominio.
