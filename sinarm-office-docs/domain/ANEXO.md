# Anexo

## Proposito

Representa arquivos anexados a clientes, armas, processos, certidoes ou
documentos.

## Entidade

Anexo possui identidade, arquivo, origem, tipo, metadados e historico.

## Possiveis Value Objects

- NomeArquivo
- HashArquivo
- TipoMime
- TamanhoArquivo

## Regras Iniciais

- Arquivo deve ter integridade verificavel por hash.
- Anexos sensiveis devem respeitar permissoes.
- Exclusao deve preferir remocao logica quando houver valor juridico.
- Download de anexos sensiveis deve ser auditavel.

## Relacionamentos

- Pode pertencer a cliente.
- Pode pertencer a arma.
- Pode pertencer a processo.
- Pode comprovar protocolo, assinatura ou exigencia.

## Questoes Em Aberto

- Onde os arquivos ficarao em producao: disco, S3 ou outro storage?
- Havera criptografia em repouso por arquivo?
- Quais tipos e tamanhos serao permitidos?
