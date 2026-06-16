# Runbook de Integração dos Projetos

## Objetivo

Guiar a integração entre AI Office, HelpUS AI e AI Bridge Local.

## Ordem segura

1. Inspecionar repositórios.
2. Gerar inventários.
3. Identificar componentes reaproveitáveis.
4. Definir contratos JSON.
5. Criar adapters.
6. Integrar em modo leitura.
7. Integrar em modo sugestão.
8. Integrar execução local com aprovação.
9. Adicionar auditoria.
10. Só depois permitir deploy controlado.

## Proibido no início

- Copiar projetos inteiros sem inventário.
- Fazer deploy automático.
- Fazer push automático.
- Dar autonomia total aos agentes.
- Permitir execução destrutiva.

## Checklist antes de qualquer integração

- git status limpo ou alterações conhecidas
- backup ou branch de trabalho
- escopo pequeno
- relatório de arquivos afetados
- teste específico
- auditoria do diff

## Resultado esperado

Integração incremental, rastreável e segura.
