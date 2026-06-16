# AI Bridge Web/API - Auditoria e Decisão Inicial

Data: 2026-06-16
Projeto origem: D:\dev\autocode\ai-bridge
Projeto destino: D:\dev\autocode\ai-office
Inventário: D:\dev\autocode\ai-office\reports\ai-bridge-web-inventory\20260616_191308

## Objetivo

Registrar a decisão inicial sobre como a AI Bridge web/API deve influenciar a arquitetura do WS AI Office.

## Estado observado

A AI Bridge web/API não é apenas uma interface. Ela contém uma arquitetura cloud/local com API, broker, fila, Postgres, dashboard, extensão de navegador e watcher local.

Componentes observados:

- apps/watcher-api
- apps/nexoai-dashboard
- extension-next
- scripts/delivery
- db/migrations
- docs relacionados a Railway, gateway e extensão

Também foram observados muitos itens locais, temporários ou de diagnóstico que não devem ser copiados diretamente:

- .chrome-debug-profile
- backups e backupDir
- logs
- temp e tmp
- outbox/candidates
- outbox/ingested
- _quarantine_scripts_cleanup_*
- .env e .env.local

## Decisão inicial

Usar a AI Bridge web/API como referência principal de arquitetura cloud do WS AI Office, especialmente para:

- API central
- broker
- fila de comandos
- contratos de command_id, source_chat_id e target_chat_id
- delivery_kind
- payload_json e payload_text
- status queued, claimed, delivered e failed
- claim/ack
- Postgres/Railway
- endpoints de health, bridge, ingest, events, queue e stats

Não usar o repositório inteiro como base direta.

## Componentes por destino

### apps/watcher-api

Classificação: COPY_AND_ADAPT_CONCEPT

Motivo:

- Parece ser o backend cloud principal.
- Usa Node.js, HTTP nativo, pg/Postgres, broker e fila.
- Contém endpoints de bridge, ingest, claim, ack, events, stats, db-query, file-ops, git-op e codex-analyze.

Uso no AI Office:

- Base conceitual para API central.
- Reaproveitar contratos e fluxo, não copiar tudo automaticamente.
- Separar endpoints seguros de endpoints perigosos.

### db/migrations

Classificação: COPY_AND_ADAPT_SCHEMA

Motivo:

- Define contratos persistentes como ops.message_queue.
- Ajuda a modelar comandos, mensagens, watchers, eventos e execuções.

Uso no AI Office:

- Ler e adaptar schema.
- Nunca copiar banco runtime.
- Nunca commitar secrets ou dumps.

### apps/nexoai-dashboard

Classificação: REFERENCE_UI_AND_ROUTES

Motivo:

- Dashboard operacional com rotas para comandos, mensagens, execuções, watchers e supervisor.

Uso no AI Office:

- Usar como referência funcional.
- Não copiar layout inteiro sem revisão.
- Extrair apenas padrões úteis de UX e rotas.

### extension-next

Classificação: SECURITY_REVIEW_REFERENCE

Motivo:

- Camada de browser/chat.
- Pode conter permissões sensíveis e automação de páginas.

Uso no AI Office:

- Usar como referência após revisão de segurança.
- Não copiar diretamente antes de entender permissões, host_permissions e fluxo de mensagens.

### scripts/delivery

Classificação: COMPARE_WITH_AI_BRIDGE_LOCAL

Motivo:

- Parece conter watcher/local delivery legado ou oficial da AI Bridge web.
- O projeto ai-bridge-local provavelmente tem versão mais avançada e limpa de parte dessas ideias.

Uso no AI Office:

- Comparar com ai-bridge-local.
- Escolher uma linha oficial de execução local.
- Evitar duplicar watchers incompatíveis.

## Riscos identificados

- Endpoints que executam comandos ou mexem em arquivos.
- db-query remoto.
- file-ops remoto.
- git-op remoto.
- codex-analyze remoto.
- secrets em .env e .env.local.
- mistura de código real com scripts temporários, diagnósticos e arquivos locais.
- múltiplas gerações de watcher/local delivery.

## Política recomendada

Antes de copiar qualquer código para o WS AI Office:

1. Classificar cada arquivo como KEEP_REFERENCE, COPY_ADAPT, IGNORE ou SECURITY_REVIEW.
2. Copiar apenas arquivos aprovados.
3. Manter endpoints perigosos atrás de gate explícito.
4. Criar smokes antes de qualquer commit.
5. Nunca copiar .env, logs, bancos runtime ou perfis de navegador.
6. Comparar scripts/delivery com ai-bridge-local antes de decidir o executor local oficial.

## Próximos passos

1. Ler schema Railway em db/migrations.
2. Ler endpoints completos de apps/watcher-api/src/server.mjs.
3. Mapear endpoints seguros versus perigosos.
4. Auditar extension-next/manifest.json.
5. Comparar scripts/delivery com ai-bridge-local.
6. Só depois iniciar blueprint técnico do WS AI Office.

## Decisão

Status: APROVADO COMO REFERÊNCIA PRINCIPAL, NÃO APROVADO PARA CÓPIA DIRETA.

A AI Bridge web/API será tratada como base conceitual cloud/API do WS AI Office. O reaproveitamento será seletivo, auditado e incremental.
