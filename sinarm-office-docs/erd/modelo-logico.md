# ERD - Modelo Logico

## Objetivo

Listar tabelas candidatas e chaves em nivel logico, ainda antes dos Models
Django.

## Tabelas Candidatas

- organizacoes.
- usuarios.
- perfis.
- grupos.
- permissoes.
- perfil_permissoes.
- usuario_perfis.
- clientes.
- enderecos.
- telefones.
- emails.
- contatos.
- armas.
- calibres.
- fabricantes.
- modelos_armas.
- especies_armas.
- funcionamentos_armas.
- tipos_processos.
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
- knowledge_base_items.
- knowledge_base_sources.
- compliance_checks.
- compliance_findings.
- retention_policies.
- timeline_events.
- agenda.
- tarefas.
- financeiro.
- pagamentos.
- parametros.
- api_keys.
- configuracoes.

## Chaves E Relacoes Iniciais

- `usuarios.organizacao_id -> organizacoes.id`.
- `clientes.organizacao_id -> organizacoes.id`.
- `processos.organizacao_id -> organizacoes.id`.
- `perfil_permissoes.perfil_id -> perfis.id`.
- `perfil_permissoes.permissao_id -> permissoes.id`.
- `usuario_perfis.usuario_id -> usuarios.id`.
- `usuario_perfis.perfil_id -> perfis.id`.
- `clientes.organizacao_id -> organizacoes.id`.
- `enderecos.cliente_id -> clientes.id`.
- `telefones.cliente_id -> clientes.id`.
- `emails.cliente_id -> clientes.id`.
- `contatos.cliente_id -> clientes.id`.
- `armas.cliente_id -> clientes.id`.
- `armas.fabricante_id -> fabricantes.id`.
- `armas.modelo_arma_id -> modelos_armas.id`.
- `armas.calibre_id -> calibres.id`.
- `armas.especie_arma_id -> especies_armas.id`.
- `armas.funcionamento_arma_id -> funcionamentos_armas.id`.
- `processos.cliente_id -> clientes.id`.
- `processos.tipo_processo_id -> tipos_processos.id`.
- `processo_armas.processo_id -> processos.id`.
- `processo_armas.arma_id -> armas.id`.
- `workflow_etapas.workflow_id -> workflows.id`.
- `workflow_transicoes.workflow_id -> workflows.id`.
- `workflow_historico.processo_id -> processos.id`.
- `documentos.processo_id -> processos.id`.
- `documentos.modelo_versao_id -> documento_modelo_versoes.id`.
- `documento_versoes.documento_id -> documentos.id`.
- `ia_execucoes.documento_id -> documentos.id`.
- `knowledge_base_items.source_id -> knowledge_base_sources.id`.
- `compliance_checks.processo_id -> processos.id`.
- `compliance_checks.documento_id -> documentos.id`.
- `compliance_findings.compliance_check_id -> compliance_checks.id`.
- `timeline_events.cliente_id -> clientes.id`.
- `timeline_events.processo_id -> processos.id`.
- `timeline_events.documento_id -> documentos.id`.
- `auditoria.usuario_id -> usuarios.id`.

## Regras Logicas

- Arma pertence ao cliente.
- Processo utiliza arma por tabela associativa.
- Documento preserva versao do modelo usado.
- Workflow deve ser versionavel.
- Auditoria deve ser append-only.
- Timeline deve ser append-only.
- Organizacao prepara multiempresa.
- ACL/RBAC deve considerar organizacao, perfil, permissao e contexto.
- Knowledge Base deve preservar fonte e vigencia quando aplicavel.
- Compliance deve registrar verificacoes e achados auditaveis.
