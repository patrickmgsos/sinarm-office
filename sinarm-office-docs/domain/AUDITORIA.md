# Auditoria

## Proposito

Registrar eventos relevantes para seguranca, LGPD, rastreabilidade operacional e
responsabilidade juridica.

## Entidade

Evento de auditoria e uma entidade historica imutavel.

## Eventos Candidatos

- Login.
- Alteracao cadastral sensivel.
- Criacao de processo.
- Transicao de workflow.
- Geracao de documento.
- Revisao de documento.
- Uso de IA.
- Alteracao de modelo.
- Exportacao ou download.
- Arquivamento.

## Regras Iniciais

- Eventos de auditoria nao devem ser alterados.
- Eventos devem registrar usuario, data, origem e alvo.
- Quando possivel, registrar valores anteriores e novos.
- Dados sensiveis devem respeitar LGPD e principio de minimizacao.

## Questoes Em Aberto

- Qual politica de retencao sera adotada?
- Como tratar logs tecnicos versus auditoria de negocio?
- Quais eventos exigem justificativa obrigatoria?
