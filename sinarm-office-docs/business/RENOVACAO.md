# Renovacao

## Descricao

Processo administrativo para renovacao de registro, autorizacao ou documento
relacionado a arma ja vinculada ao cliente.

## Regra Estrutural

Renovacao utiliza arma existente do cliente.

## Entradas De Negocio

- Cliente.
- Arma vinculada ao cliente.
- Documento anterior.
- Validade atual.
- Certidoes e comprovantes aplicaveis.

## Fluxo De Alto Nivel

1. Cliente selecionado.
2. Armas selecionadas.
3. Validades verificadas.
4. Documentacao conferida.
5. Minutas geradas.
6. Revisao humana.
7. Assinatura.
8. Protocolo.
9. Acompanhamento.
10. Deferimento ou exigencia.

## Pontos De Atencao

- Validade vencida deve gerar alerta.
- CRAF e documentos correlatos devem ser preservados.
- Renovacoes sucessivas devem manter historico da mesma arma.
