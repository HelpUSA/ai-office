# AI Bridge Local - Decisão de Executor Local

Data: 2026-06-16
Projeto origem: D:\dev\autocode\ai-bridge-local
Projeto destino: D:\dev\autocode\ai-office

## Objetivo

Registrar a decisão sobre qual componente deve servir como linha oficial de execução local do WS AI Office.

## Contexto

A auditoria anterior da AI Bridge web/API concluiu que apps/watcher-api e db/migrations devem ser usados como base conceitual cloud/API.

A auditoria inicial do ai-bridge-local mostrou que ele é uma aplicação standalone, sem dependência de Railway/API cloud, voltada especificamente para execução local segura.

Arquitetura observada no ai-bridge-local:

- Chat
- Extensão Chrome em modo local
- Gateway HTTP local na porta 8766
- SQLite queue_local.db
- Worker supervisor
- Execução de comandos
- Retorno estruturado para o chat

## Decisão

Status: AI_BRIDGE_LOCAL_APROVADO_COMO_EXECUTOR_LOCAL_OFICIAL

O ai-bridge-local será tratado como a linha oficial de execução local do WS AI Office.

## Justificativa

- Está limpo e alinhado com origin/main.
- Tem histórico de versões focadas em segurança, smoke, preflight, release runner e autorização interchat.
- Usa gateway local dedicado.
- Usa fila SQLite local.
- Tem worker supervisor com suporte a run-command.
- Usa delivery_kind local_capability.
- Usa target_chat_id gateway-brain-supervisor.
- Retorna AI_LOCAL_RUN estruturado.
- Já possui padrão de success, result_is_final, chat_can_continue e next_action.
- Possui guardrails documentados contra git add ponto, cleanup real sem aprovação e PowerShell frágil em envelopes.

## Relação com AI Bridge web/API

A AI Bridge web/API permanece como referência principal cloud/API.

Divisão recomendada:

### Cloud/API

- apps/watcher-api
- db/migrations
- broker cloud
- Postgres/Railway
- endpoints de bridge, ingest, queue, claim, ack, events e stats

### Local executor

- ai-bridge-local/gateway_local.py
- ai-bridge-local/brain_worker.py
- ai-bridge-local/extension
- ai-bridge-local/queue_local.db como runtime local, não versionar banco
- smokes e preflight do ai-bridge-local

### Referência legado/histórica

- AI Bridge web scripts/delivery
- AI Bridge web extension-next

## Política de reaproveitamento

Não copiar código automaticamente.

Regras:

1. Usar ai-bridge-local como referência primária de execução local.
2. Usar scripts/delivery da AI Bridge web apenas para comparação histórica.
3. Não copiar queue_local.db, logs, builds, dist, temp, backups ou runtime.
4. Separar claramente cloud API de executor local.
5. Manter comandos locais atrás de gateway local e worker supervisor.
6. Manter qualquer operação destrutiva atrás de gate explícito.
7. Exigir smoke antes de commit.

## Implicação para o WS AI Office

O WS AI Office deve nascer com duas camadas:

### Camada cloud/orquestração

Responsável por agentes, tarefas, filas cloud, eventos, auditoria, dashboard e coordenação.

Base conceitual: AI Bridge web/API.

### Camada local/executor

Responsável por executar comandos locais, ler estado local, rodar smokes, aplicar patches aprovados e retornar resultados estruturados.

Base conceitual: ai-bridge-local.

## Próximos passos

1. Criar blueprint do WS AI Office com separação cloud/local.
2. Mapear entidades principais: agent, task, command, execution, artifact, approval, audit_event.
3. Definir quais contratos vêm da AI Bridge web/API.
4. Definir quais contratos vêm do ai-bridge-local.
5. Criar backlog de implementação incremental.

## Decisão final deste micro

AI Bridge web/API = base cloud/API.

AI Bridge Local = executor local oficial.

Scripts/delivery da AI Bridge web = referência histórica, não base principal.
