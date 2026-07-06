# ERD - Modelo Logico

## Objetivo

Listar tabelas candidatas e chaves em nivel logico, ainda antes dos Models
Django.

## Tabelas Candidatas

- empresas.
- usuarios.
- grupos.
- permissoes.
- clientes.
- enderecos.
- telefones.
- emails.
- armas.
- calibres.
- fabricantes.
- modelos_armas.
- processos.
- processo_armas.
- workflows.
- workflow_etapas.
- workflow_transicoes.
- workflow_historico.
- documentos.
- documento_modelos.
- documento_modelo_versoes.
- documento_versoes.
- documento_assinaturas.
- anexos.
- certidoes.
- notificacoes.
- auditoria.
- logs.
- ia_prompts.
- ia_execucoes.
- agenda.
- tarefas.
- financeiro.
- pagamentos.
- parametros.
- api_keys.
- configuracoes.

## Chaves E Relacoes Iniciais

- `clientes.empresa_id -> empresas.id`.
- `armas.cliente_id -> clientes.id`.
- `processos.cliente_id -> clientes.id`.
- `processo_armas.processo_id -> processos.id`.
- `processo_armas.arma_id -> armas.id`.
- `workflow_etapas.workflow_id -> workflows.id`.
- `workflow_transicoes.workflow_id -> workflows.id`.
- `workflow_historico.processo_id -> processos.id`.
- `documentos.processo_id -> processos.id`.
- `documentos.modelo_versao_id -> documento_modelo_versoes.id`.
- `documento_versoes.documento_id -> documentos.id`.
- `ia_execucoes.documento_id -> documentos.id`.
- `auditoria.usuario_id -> usuarios.id`.

## Regras Logicas

- Arma pertence ao cliente.
- Processo utiliza arma por tabela associativa.
- Documento preserva versao do modelo usado.
- Workflow deve ser versionavel.
- Auditoria deve ser append-only.
