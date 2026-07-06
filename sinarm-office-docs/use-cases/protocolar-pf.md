# Caso De Uso: Protocolar PF

## Objetivo

Registrar o protocolo do processo junto a Policia Federal.

## Atores

- Usuario interno autorizado.

## Fluxo Principal

1. Usuario acessa processo em etapa de assinatura concluida.
2. Usuario informa dados de protocolo.
3. Sistema valida documentos obrigatorios.
4. Sistema registra data, numero e comprovante.
5. Sistema move processo para etapa de protocolo ou analise.
6. Sistema registra auditoria e cria alertas de acompanhamento.

## Regras

- Protocolo deve registrar data.
- Comprovante deve ser anexado quando existir.
- Transicao deve respeitar workflow aprovado.
