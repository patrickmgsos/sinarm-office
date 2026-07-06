# Transferencia

## Descricao

Processo administrativo relacionado a transferencia de arma entre titulares ou
contextos permitidos.

## Entradas De Negocio

- Cliente atual.
- Cliente destino quando aplicavel.
- Arma.
- Documentos da arma.
- Documentos das partes.
- Justificativas ou requerimentos.

## Fluxo De Alto Nivel

1. Identificar arma.
2. Identificar partes envolvidas.
3. Conferir documentos.
4. Gerar documentos.
5. Revisar.
6. Assinar.
7. Protocolar.
8. Acompanhar resultado.
9. Atualizar historico de titularidade.

## Pontos De Atencao

- Historico de propriedade deve ser preservado.
- Arma nao deve ser duplicada para representar transferencia.
- Transferencia deve gerar evento auditavel.
