# WS AI Office - Blueprint Técnico

Data: 2026-06-16
Status: Blueprint inicial após auditoria AI Bridge web/API e AI Bridge Local

## 1. Objetivo

O WS AI Office é uma camada de produto/orquestração para coordenar agentes de IA, tarefas, comandos, execuções locais, auditoria, aprovações e artefatos.

Ele não deve nascer como uma cópia direta de nenhum repositório existente. Deve aproveitar seletivamente conceitos de projetos já validados.

## 2. Decisões base

### 2.1 Base cloud/API

Decisão: usar AI Bridge web/API como referência principal de arquitetura cloud/API.

Origem principal:

- D:\dev\autocode\ai-bridge\apps\watcher-api
- D:\dev\autocode\ai-bridge\db\migrations

Conceitos aproveitados:

- API central
- broker cloud
- fila de comandos
- Postgres/Railway
- command_id
- source_chat_id
- target_chat_id
- delivery_kind
- payload_text
- payload_json
- status queued, claimed, delivered, failed
- claim/ack
- endpoints de health, bridge, ingest, queue, events e stats

### 2.2 Executor local

Decisão: usar AI Bridge Local como executor local oficial.

Origem principal:

- D:\dev\autocode\ai-bridge-local\gateway_local.py
- D:\dev\autocode\ai-bridge-local\brain_worker.py
- D:\dev\autocode\ai-bridge-local\extension

Conceitos aproveitados:

- gateway HTTP local
- fila SQLite local
- worker supervisor
- run-command
- delivery_kind local_capability
- target_chat_id gateway-brain-supervisor
- retorno AI_LOCAL_RUN
- success
- result_is_final
- chat_can_continue
- next_action
- smokes e preflight
- gates de segurança

### 2.3 Referência histórica

Os scripts/delivery da AI Bridge web/API serão tratados como referência histórica, não como linha principal do executor local.

## 3. Camadas do WS AI Office

### 3.1 Product/UI Layer

Responsável por apresentar o escritório virtual:

- painel de agentes
- painel de tarefas
- timeline de execuções
- aprovações pendentes
- logs/auditoria
- artefatos gerados
- estado cloud/local

Referência: apps/nexoai-dashboard da AI Bridge web/API.

### 3.2 Orchestration/API Layer

Responsável por coordenar agentes e tarefas.

Responsabilidades:

- criar tarefas
- dividir tarefas em comandos
- registrar aprovações
- publicar comandos na fila
- receber eventos
- rastrear execuções
- manter histórico auditável
- expor health/status

Referência: apps/watcher-api da AI Bridge web/API.

### 3.3 Persistence Layer

Responsável por persistência cloud.

Banco recomendado: Postgres.

Entidades iniciais:

- agents
- tasks
- commands
- executions
- artifacts
- approvals
- audit_events
- local_runners
- conversations
- messages

Referência: db/migrations da AI Bridge web/API.

### 3.4 Local Runner Layer

Responsável por executar ações locais aprovadas.

Responsabilidades:

- receber comandos locais
- validar payload
- aplicar gates
- executar scripts/comandos
- rodar smokes
- retornar AI_LOCAL_RUN
- manter fila local
- evitar ações destrutivas sem aprovação

Referência: AI Bridge Local.

### 3.5 Browser/Chat Bridge Layer

Responsável por integração com chats e navegador.

Referências:

- extension-next da AI Bridge web/API
- extension do AI Bridge Local

Status: SECURITY_REVIEW_REQUIRED antes de qualquer cópia.

## 4. Entidades principais

### 4.1 Agent

Representa um agente/papel do escritório.

Campos candidatos:

- id
- name
- role
- description
- status
- capabilities
- default_model
- created_at
- updated_at

Exemplos:

- Supervisor
- Builder
- Auditor
- Researcher
- Release Manager
- Local Executor

### 4.2 Task

Representa uma atividade de negócio ou engenharia.

Campos candidatos:

- id
- title
- description
- status
- priority
- owner_agent_id
- source
- project_key
- created_at
- updated_at
- completed_at

Status candidatos:

- draft
- planned
- waiting_approval
- queued
- running
- blocked
- completed
- failed
- cancelled

### 4.3 Command

Representa uma unidade executável ou roteável.

Campos candidatos:

- id
- command_id
- task_id
- source_agent_id
- target_runner_id
- source_chat_id
- target_chat_id
- action
- delivery_kind
- payload_json
- payload_text
- status
- priority
- created_at
- claimed_at
- delivered_at
- acked_at
- failed_at

Contratos herdados:

- command_id
- source_chat_id
- target_chat_id
- delivery_kind
- payload_json
- payload_text
- queued/claimed/delivered/failed

### 4.4 Execution

Representa o resultado de um comando executado.

Campos candidatos:

- id
- command_id
- runner_id
- status
- return_code
- stdout_ref
- stderr_ref
- summary
- started_at
- finished_at
- result_is_final
- chat_can_continue
- next_action

### 4.5 Approval

Representa autorização explícita para ações sensíveis.

Campos candidatos:

- id
- task_id
- command_id
- risk_level
- approval_type
- requested_by
- approved_by
- status
- reason
- created_at
- decided_at

Ações que exigem approval:

- deploy
- push
- git reset
- git clean
- remoção em massa
- alteração de secrets
- execução destrutiva
- db migration real
- cleanup real de fila

### 4.6 Artifact

Representa arquivos, relatórios, documentos ou outputs gerados.

Campos candidatos:

- id
- task_id
- command_id
- type
- path
- title
- description
- checksum
- created_at

### 4.7 Audit Event

Representa evento auditável.

Campos candidatos:

- id
- event_type
- actor
- task_id
- command_id
- payload_json
- created_at

## 5. Contratos operacionais

### 5.1 Cloud command contract

Contrato conceitual herdado da AI Bridge web/API:

- command_id obrigatório
- source_chat_id opcional mas recomendado
- target_chat_id obrigatório para roteamento
- action obrigatório
- delivery_kind obrigatório
- payload_json para dados estruturados
- payload_text para mensagens humanas
- status controlado por fila

### 5.2 Local execution contract

Contrato conceitual herdado do AI Bridge Local:

- action: run-command
- delivery_kind: local_capability
- target_chat_id: gateway-brain-supervisor
- payload.cwd
- payload.command ou payload.script_text/script_ext/script_path
- payload.timeout_seconds
- retorno AI_LOCAL_RUN
- success
- result_is_final
- chat_can_continue
- next_action

## 6. Segurança e gates

Regras permanentes:

1. Nunca usar git add ponto em automação assistida.
2. Nunca copiar .env, bancos runtime, logs, builds ou perfis de navegador.
3. Nunca executar cleanup real sem backup e aprovação explícita.
4. Nunca aplicar patch sem smoke relevante.
5. Separar cloud API de executor local.
6. Separar geração de plano de execução real.
7. Endpoints perigosos devem nascer desativados ou protegidos por gate.

Endpoints/conceitos de alto risco:

- db-query
- file-ops
- git-op
- codex-analyze
- run-command
- deploy
- migration real
- cleanup real

## 7. MVP proposto

### MVP 1 - Escritório virtual readonly

Objetivo: criar UI/API que registra agentes, tarefas e decisões sem executar comandos reais.

Escopo:

- cadastro de agentes
- cadastro de tarefas
- timeline manual
- decision log
- artifact registry
- status readonly de projetos locais

Sem execução real.

### MVP 2 - Integração local controlada

Objetivo: conectar ao AI Bridge Local em modo seguro.

Escopo:

- listar status local
- enviar comandos readonly
- receber AI_LOCAL_RUN
- armazenar executions
- exigir approval para comandos sensíveis

### MVP 3 - Orquestração multiagente

Objetivo: permitir que agentes proponham comandos, planos, revisões e aprovações.

Escopo:

- planner
- builder
- auditor
- release manager
- gates
- smokes
- backlog automatizado

## 8. Backlog inicial

1. Criar schema inicial do AI Office.
2. Criar API mínima para agents/tasks/audit_events.
3. Criar dashboard inicial.
4. Criar local runner adapter abstrato.
5. Criar modo readonly de inspeção local.
6. Criar approval gate.
7. Criar command queue interna.
8. Criar registry de artifacts.
9. Criar smokes básicos.
10. Só depois integrar execução local real.

## 9. Decisão final

O WS AI Office será construído como produto novo, usando:

- AI Bridge web/API como referência cloud/API.
- AI Bridge Local como executor local oficial.
- HelpUS AI como referência futura de multiagente/brain runtime.

Status: BLUEPRINT_INICIAL_APROVADO_PARA_PROXIMO_MICRO.
