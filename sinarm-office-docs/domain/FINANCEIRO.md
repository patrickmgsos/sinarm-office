# Financeiro

## Proposito

Controlar cobrancas, pagamentos, parcelas e situacao financeira associada a
clientes e processos.

## Entidades Candidatas

- LancamentoFinanceiro
- Pagamento
- Parcela
- FormaPagamento

## Regras Iniciais

- Processo pode possuir lancamentos financeiros.
- Pagamento deve registrar data, valor e forma.
- Estorno ou cancelamento deve ser auditado.
- Pendencias financeiras podem gerar alertas, mas regras juridicas nao devem ser
  bloqueadas sem decisao do escritorio.

## Questoes Em Aberto

- Havera emissao de nota fiscal?
- Havera integracao bancaria ou Pix?
- Financeiro sera simples na primeira versao ou completo desde o inicio?
