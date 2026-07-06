# Seguranca

## Premissas

O SINARM Office processara dados pessoais, dados documentais sensiveis e
informacoes relacionadas a processos administrativos. Seguranca deve ser tratada
como requisito de arquitetura.

## Controles Basicos

- Autenticacao forte.
- Controle de permissoes por perfil e contexto.
- Protecao CSRF.
- Mitigacao de XSS.
- Uso de ORM e queries parametrizadas contra SQL Injection.
- Logs estruturados.
- Auditoria de acoes sensiveis.
- Criptografia para segredos e dados selecionados.
- Backup testado.
- Politica de retencao e descarte conforme LGPD.

## IA

A IA deve auxiliar na elaboracao de documentos, mas nunca tomar decisoes
juridicas. Toda saida gerada por IA deve ser revisada e aprovada por usuario
humano antes de uso operacional.
