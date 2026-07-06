# Modelo Conceitual Do Banco

Documento inicial de banco, ainda sem Django Models.

## Tabelas Candidatas

1. empresas
2. usuarios
3. grupos
4. permissoes
5. clientes
6. enderecos
7. telefones
8. emails
9. armas
10. calibres
11. fabricantes
12. modelos_armas
13. processos
14. processo_armas
15. workflow
16. workflow_etapas
17. workflow_transicoes
18. workflow_historico
19. documentos
20. documento_modelos
21. documento_modelo_versoes
22. documento_versoes
23. documento_assinaturas
24. anexos
25. certidoes
26. notificacoes
27. auditoria
28. logs
29. ia_prompts
30. ia_execucoes
31. agenda
32. tarefas
33. financeiro
34. pagamentos
35. parametros
36. api_keys
37. configuracoes

## Diretrizes

- O modelo deve favorecer historico e auditoria.
- Status simples devem ser evitados quando houver workflow.
- Modelos documentais devem ser versionados.
- Documentos gerados devem preservar versao do modelo.
- IA deve registrar prompt, provedor, entrada, saida, usuario e revisao humana.
- Dados sensiveis devem respeitar LGPD e minimizacao.
