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
- O modelo separa Reference Data de entidades operacionais?
- O modelo suporta Integration Domain sem acoplar dominio a fornecedores?
- O modelo evita redundancias perigosas?
- Os agregados estao coerentes?
- Os relacionamentos fazem sentido?
- O modelo atende as regras juridicas documentadas?
- Cada tabela possui classificacao por dominio, responsabilidade, agregado,
  dono do dado, arquivamento, auditoria, API, LGPD e retencao?
- Cada indice possui justificativa e consulta esperada?
- Ha constraints suficientes para integridade?
- Toda FK possui politica explicita de `ON DELETE` e `ON UPDATE`?
- A escolha entre UUIDv7 e UUIDv4 foi decidida antes da primeira migration?
- Os nomes tecnicos estao em ingles e a interface permanece em portugues?
- Ha dependencia prematura de Django?

## Gate

Somente apos resposta positiva ou plano de correcao aceito a implementacao em
Django podera ser liberada.
