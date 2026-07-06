# Architecture Review 2.0 Checklist

## Objetivo

Validar o modelo PostgreSQL antes de qualquer Django Model ou migration.

## Perguntas De Revisao

- O modelo suporta aquisicao, renovacao, transferencia e porte?
- O modelo suporta exigencias e respostas?
- O modelo preserva documentos, versoes, assinaturas e anexos?
- O modelo evita que arma pertença ao processo?
- O modelo permite workflow configuravel e versionavel?
- O modelo suporta Timeline sem substituir Auditoria?
- O modelo suporta Knowledge Base e Compliance?
- O modelo evita redundancias perigosas?
- Os agregados estao coerentes?
- Os relacionamentos fazem sentido?
- O modelo atende as regras juridicas documentadas?
- Ha indices para consultas criticas?
- Ha constraints suficientes para integridade?
- Ha dependencia prematura de Django?

## Gate

Somente apos resposta positiva ou plano de correcao aceito a implementacao em
Django podera ser liberada.
