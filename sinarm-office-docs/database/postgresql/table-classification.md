# Table Classification

## Objetivo

Classificar tabelas por responsabilidade, sensibilidade, retencao e exposicao.
Essa classificacao complementa o catalogo de tabelas.

## Legenda

- API: indica se a tabela tende a ser exposta direta ou indiretamente por API.
- LGPD: indica se contem dado pessoal ou sensivel.
- Retencao: politica conceitual antes da definicao legal final.

## Core Domain

| Tabela | Responsabilidade | Agregado | Dono do dado | Arquivavel | Auditavel | API | LGPD | Retencao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| organizations | Representar organizacao/tenant | Organization | Core | Sim | Sim | Sim | Sim | Permanente |
| users | Representar usuario interno | User | Identity | Sim | Sim | Sim | Sim | Permanente |
| roles | Catalogar papeis | Role | Identity | Sim | Sim | Sim | Nao | Permanente |
| permissions | Catalogar permissoes | Permission | Identity | Nao | Sim | Sim | Nao | Permanente |
| audit_events | Registrar auditoria | AuditEvent | Audit | Nao | Sim | Nao direta | Pode conter | Permanente |
| audit_event_types | Catalogar tipos de auditoria | AuditEventType | Audit | Nao | Sim | Nao direta | Nao | Permanente |
| audit_sessions | Registrar contexto de sessao | AuditSession | Audit | Nao | Sim | Nao direta | Sim | Retencao definida |
| notifications | Notificar usuarios | Notification | Core | Sim | Sim | Sim | Pode conter | Retencao definida |
| settings | Configurar organizacao | Setting | Configuration | Nao | Sim | Parcial | Pode conter | Enquanto vigente |

## Customer Domain

| Tabela | Responsabilidade | Agregado | Dono do dado | Arquivavel | Auditavel | API | LGPD | Retencao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| customers | Representar cliente | Customer | Customer | Sim | Sim | Sim | Sim | Permanente |
| customer_addresses | Enderecos do cliente | Customer | Customer | Sim | Sim | Sim | Sim | Permanente |
| customer_contacts | Contatos do cliente | Customer | Customer | Sim | Sim | Sim | Sim | Permanente |
| customer_documents | Dossie cadastral | Customer | Customer | Sim | Sim | Sim | Sim | Permanente |

## Firearms Domain

| Tabela | Responsabilidade | Agregado | Dono do dado | Arquivavel | Auditavel | API | LGPD | Retencao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| firearms | Representar arma | Firearm | Firearms | Sim | Sim | Sim | Pode conter | Permanente |
| firearm_registrations | Registrar CRAF/registro | Firearm | Firearms | Sim | Sim | Sim | Pode conter | Permanente |
| manufacturers | Catalogo de fabricantes | ReferenceData | Reference Data | Sim | Sim | Sim | Nao | Permanente |
| firearm_models | Catalogo de modelos | ReferenceData | Reference Data | Sim | Sim | Sim | Nao | Permanente |
| calibers | Catalogo de calibres | ReferenceData | Reference Data | Sim | Sim | Sim | Nao | Permanente |

## Case Management Domain

| Tabela | Responsabilidade | Agregado | Dono do dado | Arquivavel | Auditavel | API | LGPD | Retencao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cases | Representar processo | Case | Case Management | Sim | Sim | Sim | Sim | Permanente |
| case_firearms | Associar armas ao processo | Case | Case Management | Nao | Sim | Sim | Pode conter | Permanente |
| workflows | Definir fluxo | Workflow | Workflow | Sim | Sim | Sim | Nao | Permanente |
| workflow_steps | Definir etapas | Workflow | Workflow | Nao | Sim | Sim | Nao | Permanente |
| workflow_history | Historico de transicoes | Case | Workflow | Nao | Sim | Sim | Pode conter | Permanente |
| requirements | Exigencias | Case | Case Management | Sim | Sim | Sim | Sim | Permanente |
| timelines | Linha do tempo | Timeline | Case Management | Nao | Sim | Sim | Pode conter | Permanente |

## Document Domain

| Tabela | Responsabilidade | Agregado | Dono do dado | Arquivavel | Auditavel | API | LGPD | Retencao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| document_templates | Modelos juridicos | Template | Document | Sim | Sim | Sim | Nao | Permanente |
| document_template_versions | Versoes de modelos | Template | Document | Nao | Sim | Sim | Nao | Permanente |
| documents | Documento juridico | Document | Document | Sim | Sim | Sim | Sim | Permanente |
| document_versions | Versoes do documento | Document | Document | Nao | Sim | Sim | Sim | Permanente |
| attachments | Arquivos | Attachment | Document | Sim | Sim | Sim | Sim | Permanente |
| signatures | Assinaturas | Signature | Document | Nao | Sim | Sim | Sim | Permanente |

## Legal Automation, Knowledge, Compliance E Integration

| Tabela | Responsabilidade | Agregado | Dono do dado | Arquivavel | Auditavel | API | LGPD | Retencao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| automation_rules | Regras de automacao | AutomationRule | Legal Automation | Sim | Sim | Sim | Nao | Permanente |
| automation_variables | Variaveis de automacao | AutomationVariable | Legal Automation | Sim | Sim | Sim | Nao | Permanente |
| automation_executions | Execucoes de automacao | AutomationExecution | Legal Automation | Nao | Sim | Nao direta | Pode conter | Permanente |
| prompts | Prompts versionados | Prompt | Legal Automation | Sim | Sim | Sim | Pode conter | Permanente |
| ai_reviews | Revisoes humanas de IA | AIReview | Legal Automation | Nao | Sim | Sim | Sim | Permanente |
| knowledge_sources | Fontes juridicas | KnowledgeSource | Knowledge | Sim | Sim | Sim | Nao | Permanente |
| knowledge_items | Itens de conhecimento | KnowledgeItem | Knowledge | Sim | Sim | Sim | Nao | Permanente |
| legal_references | Referencias juridicas | LegalReference | Knowledge | Nao | Sim | Sim | Nao | Permanente |
| compliance_checks | Verificacoes | ComplianceCheck | Compliance | Nao | Sim | Sim | Pode conter | Permanente |
| findings | Achados de compliance | Finding | Compliance | Sim | Sim | Sim | Pode conter | Permanente |
| retention_policies | Politicas de retencao | RetentionPolicy | Compliance | Sim | Sim | Sim | Nao | Enquanto vigente |
| integration_endpoints | Endpoints externos | IntegrationEndpoint | Integration | Sim | Sim | Parcial | Pode conter | Enquanto vigente |
| integration_logs | Logs de integracao | IntegrationLog | Integration | Nao | Sim | Nao direta | Pode conter | Retencao definida |
| integration_credentials | Credenciais externas | IntegrationCredential | Integration | Sim | Sim | Nao direta | Sensivel | Enquanto vigente |
| integration_jobs | Jobs de integracao | IntegrationJob | Integration | Sim | Sim | Parcial | Pode conter | Retencao definida |
