# WS AI Office - Implementation Plan

Status: inicial.

## Fase 1 - Fundação readonly

- Criar schema inicial.
- Criar contratos Python.
- Criar smokes de contratos.
- Não executar comandos reais.
- Não conectar em banco real.
- Não integrar ainda com AI Bridge Local.

## Fase 2 - API mínima

- Criar API para agents.
- Criar API para tasks.
- Criar API para audit_events.
- Criar storage local de desenvolvimento.
- Criar smoke de API readonly.

## Fase 3 - Local runner adapter readonly

- Criar adapter para consultar health/status do AI Bridge Local.
- Não enviar run-command ainda.
- Registrar local_runners.
- Criar smoke readonly.

## Fase 4 - Approval gate

- Criar classificador de risco.
- Bloquear comandos sensíveis por padrão.
- Criar approval records.
- Criar smoke de bloqueio.

## Fase 5 - Execução local controlada

- Enviar comandos readonly para AI Bridge Local.
- Receber AI_LOCAL_RUN.
- Registrar executions.
- Exigir approval para qualquer ação sensível.
