# Arquitetura Alvo do WS AI Office

## Estrutura conceitual

Usuário -> Painel AI Office -> Orquestrador -> HelpUS Agent Runtime -> Agentes Especializados -> Ferramentas -> Auditoria -> Resultado

## Estrutura de repositório sugerida

`	ext
ai-office
  apps
    office-web
  services
    office-api
    agent-runtime
    office-worker
    bridge-relay
  packages
    agents
    policies
    prompts
    tools
    schemas
  local
    ai-bridge-local
  docs
  config
`",
    ",
    

### apps/office-web

Frontend do escritório.

Responsável por:

- dashboard dos agentes
- fila de tarefas
- aprovações pendentes
- relatórios
- histórico
- visão de custos

## Services

### services/office-api

API principal do escritório.

Responsável por:

- autenticação
- tarefas
- agentes
- aprovações
- logs
- relatórios

### services/agent-runtime

Camada baseada na HelpUS AI.

Responsável por:

- orquestração de agentes
- prompts
- memória
- uso de modelos
- ferramentas
- handoff entre agentes

### services/office-worker

Worker para tarefas assíncronas.

Responsável por:

- processar fila
- retentar falhas
- gerar relatórios
- executar jobs agendados

### services/bridge-relay

Adaptador entre AI Office e AI Bridge Local.

Responsável por:

- enviar tarefas locais ao bridge
- receber resultados
- registrar AI_LOCAL_RUN
- acionar auditoria

## Packages

### packages/agents

Definições dos agentes.

### packages/policies

Regras de risco, permissões e aprovação.

### packages/prompts

Prompts base dos agentes.

### packages/tools

Ferramentas disponíveis para agentes.

### packages/schemas

Contratos JSON para tarefas, agentes, ferramentas e aprovações.

## Local

### local/ai-bridge-local

Código reaproveitado ou integrado do AI Bridge Local.

O objetivo não é duplicar sem controle, mas adaptar como executor local seguro.
