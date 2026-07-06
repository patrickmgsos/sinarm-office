# Table Catalog

## Convencoes

Todas as tabelas de dominio usam:

- Chave primaria: `id uuid`.
- Datas: `created_at timestamptz`.
- Atualizacao quando aplicavel: `updated_at timestamptz`.
- Arquivamento quando juridicamente aplicavel: `status`, `archived_at`,
  `archived_by`.
- Auditoria juridica principal via `audit_events`.

Tipos e constraints finais serao revisados na Architecture Review 2.0 antes de
migrations.

## Core Domain

### organizations

- Finalidade: representar escritorio, unidade ou tenant futuro.
- PK: `id uuid`.
- Colunas: `name text not null`, `legal_name text`, `document_number text`,
  `status text not null`, `created_at timestamptz not null`,
  `updated_at timestamptz`.
- Constraints: `status in ('active','inactive','archived')`,
  `unique(document_number)` quando nao nulo.
- FKs: nenhuma inicial.
- Indices: `document_number`, `status`.
- Arquivamento: `status`, `archived_at`, `archived_by`.
- Justificativa: prepara multiempresa sem impor multi-tenant complexo no inicio.

### users

- Finalidade: usuarios internos autenticados.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `email text not null`,
  `full_name text not null`, `status text not null`, `last_login_at timestamptz`,
  `created_at timestamptz not null`, `updated_at timestamptz`.
- Constraints: `unique(organization_id, email)`, status controlado.
- FKs: `organization_id -> organizations.id`.
- Indices: `organization_id`, `email`, `status`.
- Arquivamento: status inativo/arquivado.
- Justificativa: identidade isolada por organizacao.

### roles

- Finalidade: perfis como administrador, socio, advogado e assistente.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `name text not null`, `code text not null`,
  `is_system boolean not null`, `created_at timestamptz not null`.
- Constraints: `unique(organization_id, code)`.
- FKs: `organization_id -> organizations.id` opcional.
- Indices: `organization_id`, `code`.
- Arquivamento: `is_active boolean`.
- Justificativa: suporta perfis globais e especificos por organizacao.

### permissions

- Finalidade: permissoes atomicas por modulo/acao.
- PK: `id uuid`.
- Colunas: `code text not null`, `description text`, `created_at timestamptz`.
- Constraints: `unique(code)`.
- FKs: nenhuma.
- Indices: `code`.
- Arquivamento: nao aplicavel; permissao e catalogo.
- Justificativa: base do RBAC/ACL.

### role_permissions

- Finalidade: associar roles a permissions.
- PK: `id uuid`.
- Colunas: `role_id uuid not null`, `permission_id uuid not null`,
  `created_at timestamptz not null`.
- Constraints: `unique(role_id, permission_id)`.
- FKs: `role_id -> roles.id`, `permission_id -> permissions.id`.
- Indices: `role_id`, `permission_id`.
- Arquivamento: exclusao logica nao necessaria; associacao pode ser removida.
- Justificativa: separa permissao de perfil.

### user_roles

- Finalidade: associar usuarios a roles.
- PK: `id uuid`.
- Colunas: `user_id uuid not null`, `role_id uuid not null`,
  `created_at timestamptz not null`.
- Constraints: `unique(user_id, role_id)`.
- FKs: `user_id -> users.id`, `role_id -> roles.id`.
- Indices: `user_id`, `role_id`.
- Arquivamento: nao aplicavel.
- Justificativa: usuario pode acumular papeis.

### audit_events

- Finalidade: trilha oficial de auditoria.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `actor_id uuid`, `event_type text not null`,
  `entity_type text not null`, `entity_id uuid`, `action text not null`,
  `occurred_at timestamptz not null`, `metadata jsonb`, `before_data jsonb`,
  `after_data jsonb`, `ip_address inet`, `user_agent text`.
- Constraints: `event_type <> ''`, `action <> ''`.
- FKs: `organization_id -> organizations.id`, `actor_id -> users.id`.
- Indices: `(entity_type, entity_id)`, `actor_id`, `occurred_at`, `action`.
- Arquivamento: append-only, sem soft delete.
- Justificativa: auditoria desacoplada das tabelas operacionais.

### notifications

- Finalidade: alertas internos e notificacoes operacionais.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `recipient_id uuid`,
  `title text not null`, `body text`, `status text not null`,
  `priority text not null`, `source_type text`, `source_id uuid`,
  `read_at timestamptz`, `created_at timestamptz not null`.
- Constraints: status e prioridade controlados.
- FKs: `organization_id -> organizations.id`, `recipient_id -> users.id`.
- Indices: `recipient_id,status`, `source_type,source_id`, `created_at`.
- Arquivamento: status lida/arquivada.
- Justificativa: notificacoes podem nascer de workflow, compliance ou agenda.

### settings

- Finalidade: configuracoes por organizacao.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `key text not null`, `value jsonb not null`,
  `is_sensitive boolean not null`, `created_at timestamptz not null`,
  `updated_at timestamptz`.
- Constraints: `unique(organization_id, key)`.
- FKs: `organization_id -> organizations.id`.
- Indices: `organization_id`, `key`.
- Arquivamento: nao aplicavel inicialmente.
- Justificativa: configuracao sem hardcode.

## Customer Domain

### customers

- Finalidade: cliente pessoa fisica ou juridica.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `person_type text not null`,
  `name text not null`, `trade_name text`, `cpf text`, `cnpj text`, `rg text`,
  `birth_date date`, `status text not null`, `created_at timestamptz not null`,
  `updated_at timestamptz`, `archived_at timestamptz`, `archived_by uuid`.
- Constraints: `person_type in ('individual','company')`,
  unique parcial `(organization_id, cpf)` quando CPF nao nulo,
  unique parcial `(organization_id, cnpj)` quando CNPJ nao nulo.
- FKs: `organization_id -> organizations.id`, `archived_by -> users.id`.
- Indices: `organization_id`, `name`, `cpf`, `cnpj`, `status`.
- Arquivamento: status/archived_at/archived_by.
- Justificativa: agregado central de clientes, sem exclusao fisica.

### customer_addresses

- Finalidade: enderecos do cliente.
- PK: `id uuid`.
- Colunas: `customer_id uuid not null`, `type text not null`, `street text`,
  `number text`, `complement text`, `district text`, `city text`,
  `state char(2)`, `postal_code text`, `is_primary boolean not null`,
  `created_at timestamptz not null`, `updated_at timestamptz`.
- Constraints: pelo menos cidade/UF ou CEP conforme regra final.
- FKs: `customer_id -> customers.id`.
- Indices: `customer_id`, `postal_code`.
- Arquivamento: nao; registros podem ser inativados com `is_active`.
- Justificativa: cliente pode mudar de endereco e manter historico.

### customer_contacts

- Finalidade: contatos complementares e representantes.
- PK: `id uuid`.
- Colunas: `customer_id uuid not null`, `name text not null`,
  `relationship text`, `phone text`, `email text`, `notes text`,
  `created_at timestamptz not null`.
- Constraints: email valido em nivel aplicacao/dominio.
- FKs: `customer_id -> customers.id`.
- Indices: `customer_id`, `name`.
- Arquivamento: `is_active boolean`.
- Justificativa: separa contatos de telefone/email principais.

### customer_documents

- Finalidade: documentos cadastrais do cliente.
- PK: `id uuid`.
- Colunas: `customer_id uuid not null`, `document_type text not null`,
  `attachment_id uuid`, `valid_until date`, `status text not null`,
  `created_at timestamptz not null`.
- Constraints: status controlado.
- FKs: `customer_id -> customers.id`, `attachment_id -> attachments.id`.
- Indices: `customer_id`, `document_type`, `valid_until`, `status`.
- Arquivamento: status.
- Justificativa: dossie do cliente sem misturar com processo.

## Firearms Domain

### manufacturers

- Finalidade: catalogo de fabricantes.
- PK: `id uuid`.
- Colunas: `name text not null`, `country text`, `is_active boolean not null`.
- Constraints: `unique(name)`.
- FKs: nenhuma.
- Indices: `name`.
- Arquivamento: `is_active`.
- Justificativa: evita duplicidade e melhora relatorios.

### firearm_models

- Finalidade: catalogo de modelos de arma.
- PK: `id uuid`.
- Colunas: `manufacturer_id uuid`, `name text not null`, `is_active boolean`.
- Constraints: `unique(manufacturer_id, name)`.
- FKs: `manufacturer_id -> manufacturers.id`.
- Indices: `manufacturer_id`, `name`.
- Arquivamento: `is_active`.
- Justificativa: modelo e entidade propria para filtros.

### calibers

- Finalidade: catalogo de calibres.
- PK: `id uuid`.
- Colunas: `name text not null`, `description text`, `is_active boolean`.
- Constraints: `unique(name)`.
- FKs: nenhuma.
- Indices: `name`.
- Arquivamento: `is_active`.
- Justificativa: normaliza calibre.

### firearms

- Finalidade: arma vinculada ao cliente.
- PK: `id uuid`.
- Colunas: `customer_id uuid not null`, `manufacturer_id uuid`,
  `firearm_model_id uuid`, `caliber_id uuid`, `serial_number text`,
  `species text`, `operation_type text`, `status text not null`,
  `created_at timestamptz not null`, `updated_at timestamptz`,
  `archived_at timestamptz`, `archived_by uuid`.
- Constraints: serial rastreavel; unique parcial de serial quando regra aprovar.
- FKs: `customer_id -> customers.id`, `manufacturer_id -> manufacturers.id`,
  `firearm_model_id -> firearm_models.id`, `caliber_id -> calibers.id`,
  `archived_by -> users.id`.
- Indices: `customer_id`, `serial_number`, `status`.
- Arquivamento: status/archived_at/archived_by.
- Justificativa: arma pertence ao cliente, nao ao processo.

### firearm_registrations

- Finalidade: registros, CRAF e dados documentais da arma.
- PK: `id uuid`.
- Colunas: `firearm_id uuid not null`, `registration_number text`,
  `craf_number text`, `issued_at date`, `valid_until date`,
  `attachment_id uuid`, `status text not null`, `created_at timestamptz`.
- Constraints: validade posterior a emissao quando ambas existirem.
- FKs: `firearm_id -> firearms.id`, `attachment_id -> attachments.id`.
- Indices: `firearm_id`, `craf_number`, `valid_until`.
- Arquivamento: status.
- Justificativa: registros variam ao longo do tempo.

## Case Management Domain

### cases

- Finalidade: processo administrativo.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `customer_id uuid not null`,
  `case_type text not null`, `responsible_user_id uuid`, `workflow_id uuid`,
  `current_step_id uuid`, `protocol_number text`, `protocol_date date`,
  `status text not null`, `created_at timestamptz not null`,
  `updated_at timestamptz`, `archived_at timestamptz`, `archived_by uuid`.
- Constraints: etapa atual deve pertencer ao workflow em regra de dominio.
- FKs: `organization_id -> organizations.id`, `customer_id -> customers.id`,
  `responsible_user_id -> users.id`, `workflow_id -> workflows.id`,
  `current_step_id -> workflow_steps.id`, `archived_by -> users.id`.
- Indices: `organization_id`, `customer_id`, `case_type`, `current_step_id`,
  `protocol_number`, `status`.
- Arquivamento: status/archived_at/archived_by.
- Justificativa: agregado operacional central.

### case_firearms

- Finalidade: associar processos a armas usadas.
- PK: `id uuid`.
- Colunas: `case_id uuid not null`, `firearm_id uuid not null`,
  `created_at timestamptz not null`.
- Constraints: `unique(case_id, firearm_id)`.
- FKs: `case_id -> cases.id`, `firearm_id -> firearms.id`.
- Indices: `case_id`, `firearm_id`.
- Arquivamento: nao aplicavel.
- Justificativa: processo usa arma, mas arma pertence ao cliente.

### workflows

- Finalidade: definicao versionada de workflow.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `name text not null`, `case_type text`,
  `version integer not null`, `status text not null`, `created_at timestamptz`.
- Constraints: `unique(organization_id, name, version)`.
- FKs: `organization_id -> organizations.id`.
- Indices: `organization_id`, `case_type`, `status`.
- Arquivamento: status.
- Justificativa: workflow configuravel e versionavel.

### workflow_steps

- Finalidade: etapas de workflow.
- PK: `id uuid`.
- Colunas: `workflow_id uuid not null`, `code text not null`,
  `name text not null`, `position integer not null`, `is_terminal boolean`.
- Constraints: `unique(workflow_id, code)`.
- FKs: `workflow_id -> workflows.id`.
- Indices: `workflow_id`, `position`.
- Arquivamento: nao em workflow publicado; versionar workflow.
- Justificativa: evita status fixo.

### workflow_history

- Finalidade: historico de transicoes do processo.
- PK: `id uuid`.
- Colunas: `case_id uuid not null`, `from_step_id uuid`, `to_step_id uuid not null`,
  `changed_by uuid`, `changed_at timestamptz not null`, `reason text`,
  `metadata jsonb`.
- Constraints: `from_step_id <> to_step_id` quando ambos existirem.
- FKs: `case_id -> cases.id`, `from_step_id -> workflow_steps.id`,
  `to_step_id -> workflow_steps.id`, `changed_by -> users.id`.
- Indices: `case_id, changed_at`, `to_step_id`.
- Arquivamento: append-only.
- Justificativa: rastreia workflow sem sobrescrever estado historico.

### requirements

- Finalidade: exigencias emitidas pela PF ou orgao competente.
- PK: `id uuid`.
- Colunas: `case_id uuid not null`, `description text not null`,
  `received_at date not null`, `due_date date`, `status text not null`,
  `response_protocol text`, `responded_at date`, `created_at timestamptz`.
- Constraints: due_date >= received_at quando informado.
- FKs: `case_id -> cases.id`.
- Indices: `case_id`, `status`, `due_date`.
- Arquivamento: status.
- Justificativa: exigencia e subfluxo rastreavel.

### timelines

- Finalidade: linha do tempo operacional.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `customer_id uuid`, `case_id uuid`,
  `document_id uuid`, `event_type text not null`, `description text not null`,
  `occurred_at timestamptz not null`, `actor_id uuid`, `metadata jsonb`.
- Constraints: ao menos um alvo entre customer/case/document.
- FKs: `organization_id -> organizations.id`, `customer_id -> customers.id`,
  `case_id -> cases.id`, `document_id -> documents.id`, `actor_id -> users.id`.
- Indices: `customer_id, occurred_at`, `case_id, occurred_at`,
  `document_id, occurred_at`.
- Arquivamento: append-only.
- Justificativa: acompanhamento amigavel sem substituir auditoria.

## Document Domain

### document_templates

- Finalidade: modelo juridico versionavel.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `name text not null`, `template_type text not null`,
  `status text not null`, `created_at timestamptz`.
- Constraints: `unique(organization_id, template_type, name)`.
- FKs: `organization_id -> organizations.id`.
- Indices: `template_type`, `status`.
- Arquivamento: status.
- Justificativa: textos juridicos fora do codigo.

### document_template_versions

- Finalidade: versoes dos modelos.
- PK: `id uuid`.
- Colunas: `template_id uuid not null`, `version integer not null`,
  `content text not null`, `variables_schema jsonb`, `status text not null`,
  `created_by uuid`, `created_at timestamptz not null`, `activated_at timestamptz`.
- Constraints: `unique(template_id, version)`.
- FKs: `template_id -> document_templates.id`, `created_by -> users.id`.
- Indices: `template_id, version`, `status`.
- Arquivamento: status; nunca sobrescrever.
- Justificativa: permite alterar modelo sem deploy.

### documents

- Finalidade: documento juridico ou operacional.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `case_id uuid`, `customer_id uuid`,
  `document_type text not null`, `template_version_id uuid`, `status text not null`,
  `created_at timestamptz not null`, `updated_at timestamptz`,
  `archived_at timestamptz`, `archived_by uuid`.
- Constraints: ao menos um alvo case/customer.
- FKs: `organization_id -> organizations.id`, `case_id -> cases.id`,
  `customer_id -> customers.id`, `template_version_id -> document_template_versions.id`.
- Indices: `case_id`, `customer_id`, `document_type`, `status`.
- Arquivamento: status/archived_at/archived_by.
- Justificativa: documento e artefato versionado, nao apenas PDF.

### document_versions

- Finalidade: versoes oficiais e rascunhos de documentos.
- PK: `id uuid`.
- Colunas: `document_id uuid not null`, `version integer not null`,
  `content text`, `attachment_id uuid`, `status text not null`,
  `created_by uuid`, `created_at timestamptz not null`, `reviewed_by uuid`,
  `reviewed_at timestamptz`.
- Constraints: `unique(document_id, version)`.
- FKs: `document_id -> documents.id`, `attachment_id -> attachments.id`,
  `created_by -> users.id`, `reviewed_by -> users.id`.
- Indices: `document_id, version`, `status`.
- Arquivamento: append-only/versionado.
- Justificativa: Time Machine documental.

### attachments

- Finalidade: arquivos anexados.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `file_name text not null`,
  `storage_path text not null`, `mime_type text`, `file_size bigint`,
  `checksum text`, `created_by uuid`, `created_at timestamptz`.
- Constraints: checksum unico quando aplicavel.
- FKs: `organization_id -> organizations.id`, `created_by -> users.id`.
- Indices: `organization_id`, `checksum`, `created_at`.
- Arquivamento: status quando arquivo juridicamente relevante.
- Justificativa: arquivo e recurso compartilhavel por documentos/processos.

### signatures

- Finalidade: registro de assinatura.
- PK: `id uuid`.
- Colunas: `document_version_id uuid not null`, `signed_by_name text not null`,
  `signed_at timestamptz`, `signature_type text`, `attachment_id uuid`,
  `metadata jsonb`.
- Constraints: assinatura aponta para versao, nao documento generico.
- FKs: `document_version_id -> document_versions.id`, `attachment_id -> attachments.id`.
- Indices: `document_version_id`, `signed_at`.
- Arquivamento: append-only.
- Justificativa: assinatura deve preservar versao assinada.

## Legal Automation Domain

### automation_rules

- Finalidade: regras usadas pelo Legal Automation Engine.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `code text not null`, `name text not null`,
  `rule_type text not null`, `definition jsonb not null`, `status text not null`,
  `created_at timestamptz`.
- Constraints: `unique(organization_id, code)`.
- FKs: `organization_id -> organizations.id`.
- Indices: `code`, `rule_type`, `status`.
- Arquivamento: status.
- Justificativa: regras fora de templates.

### automation_variables

- Finalidade: catalogo de variaveis renderizaveis.
- PK: `id uuid`.
- Colunas: `code text not null`, `path text not null`, `description text`,
  `data_type text not null`, `is_active boolean`.
- Constraints: `unique(code)`.
- FKs: nenhuma.
- Indices: `code`, `path`.
- Arquivamento: `is_active`.
- Justificativa: padroniza `cliente.nome`, `arma.calibre` etc.

### automation_executions

- Finalidade: execucoes do Legal Automation Engine.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `case_id uuid`, `document_id uuid`,
  `execution_type text not null`, `status text not null`, `input_data jsonb`,
  `output_data jsonb`, `executed_by uuid`, `executed_at timestamptz not null`.
- Constraints: status controlado.
- FKs: `organization_id -> organizations.id`, `case_id -> cases.id`,
  `document_id -> documents.id`, `executed_by -> users.id`.
- Indices: `case_id`, `document_id`, `execution_type`, `executed_at`.
- Arquivamento: append-only.
- Justificativa: rastreia automacoes, checklists e renderizacoes.

### prompts

- Finalidade: prompts versionados para IA assistiva.
- PK: `id uuid`.
- Colunas: `code text not null`, `version integer not null`, `content text not null`,
  `status text not null`, `created_at timestamptz`.
- Constraints: `unique(code, version)`.
- FKs: nenhuma.
- Indices: `code`, `status`.
- Arquivamento: status.
- Justificativa: prompts fazem parte do produto e precisam de versao.

### ai_reviews

- Finalidade: revisoes humanas sobre saidas de IA.
- PK: `id uuid`.
- Colunas: `automation_execution_id uuid not null`, `reviewed_by uuid not null`,
  `review_status text not null`, `review_notes text`, `reviewed_at timestamptz`.
- Constraints: uma revisao oficial por execucao quando regra final aprovar.
- FKs: `automation_execution_id -> automation_executions.id`,
  `reviewed_by -> users.id`.
- Indices: `automation_execution_id`, `reviewed_by`, `review_status`.
- Arquivamento: append-only.
- Justificativa: IA nao gera documento oficial sem humano.

## Knowledge Domain

### knowledge_sources

- Finalidade: fontes de conhecimento juridico.
- PK: `id uuid`.
- Colunas: `name text not null`, `source_type text not null`, `url text`,
  `authority text`, `created_at timestamptz`.
- Constraints: `unique(name, source_type)`.
- FKs: nenhuma.
- Indices: `source_type`, `authority`.
- Arquivamento: `is_active`.
- Justificativa: IA e automacao precisam citar fonte.

### knowledge_items

- Finalidade: itens pesquisaveis de conhecimento.
- PK: `id uuid`.
- Colunas: `source_id uuid`, `title text not null`, `item_type text not null`,
  `content text not null`, `effective_from date`, `effective_until date`,
  `status text not null`, `created_at timestamptz`.
- Constraints: vigencia valida quando ambas as datas existirem.
- FKs: `source_id -> knowledge_sources.id`.
- Indices: `source_id`, `item_type`, `status`, `effective_from`.
- Arquivamento: status.
- Justificativa: base juridica versionavel e rastreavel.

### legal_references

- Finalidade: referencias juridicas citadas por documentos, regras ou respostas.
- PK: `id uuid`.
- Colunas: `knowledge_item_id uuid not null`, `target_type text not null`,
  `target_id uuid not null`, `created_at timestamptz`.
- Constraints: evita duplicidade por alvo e item.
- FKs: `knowledge_item_id -> knowledge_items.id`.
- Indices: `target_type,target_id`, `knowledge_item_id`.
- Arquivamento: nao aplicavel.
- Justificativa: rastreia embasamento juridico.

## Compliance Domain

### compliance_checks

- Finalidade: verificacoes de conformidade.
- PK: `id uuid`.
- Colunas: `organization_id uuid not null`, `case_id uuid`, `document_id uuid`,
  `check_type text not null`, `status text not null`, `checked_at timestamptz`,
  `checked_by uuid`.
- Constraints: ao menos um alvo case/document.
- FKs: `organization_id -> organizations.id`, `case_id -> cases.id`,
  `document_id -> documents.id`, `checked_by -> users.id`.
- Indices: `case_id`, `document_id`, `check_type`, `status`.
- Arquivamento: append-only ou status.
- Justificativa: compliance deve ser rastreavel.

### findings

- Finalidade: achados de compliance.
- PK: `id uuid`.
- Colunas: `compliance_check_id uuid not null`, `severity text not null`,
  `description text not null`, `status text not null`, `resolved_at timestamptz`.
- Constraints: severidade/status controlados.
- FKs: `compliance_check_id -> compliance_checks.id`.
- Indices: `compliance_check_id`, `severity`, `status`.
- Arquivamento: status.
- Justificativa: pendencias e riscos ficam explicitados.

### retention_policies

- Finalidade: politicas de retencao de dados/documentos.
- PK: `id uuid`.
- Colunas: `organization_id uuid`, `target_type text not null`,
  `retention_period_days integer not null`, `action text not null`,
  `status text not null`, `created_at timestamptz`.
- Constraints: `retention_period_days > 0`.
- FKs: `organization_id -> organizations.id`.
- Indices: `target_type`, `status`.
- Arquivamento: status.
- Justificativa: LGPD e governanca documental.
