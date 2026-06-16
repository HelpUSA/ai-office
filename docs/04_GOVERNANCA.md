# 04 - Governança

## Princípios

- Humano no comando.
- Menor privilégio.
- Logs sempre.
- Aprovação para ações sensíveis.
- Auditoria antes de produção.
- Rollback planejado.
- Separação entre leitura, sugestão e execução.

## Matriz de risco

| Ação | Risco | Aprovação |
|---|---:|---|
| Ler arquivo | Baixo | Não |
| Criar documentação | Baixo | Não |
| Sugerir patch | Baixo | Não |
| Alterar código | Médio | Sim, se relevante |
| Rodar teste | Baixo | Não |
| Commit | Médio | Sim |
| Push | Alto | Sim |
| Deploy | Alto | Sim |
| Enviar e-mail externo | Alto | Sim |
| Alterar campanha paga | Alto | Sim |
| Apagar arquivos | Crítico | Sim |
| Acessar secrets | Crítico | Sim |

## Regra de ouro

Quando houver dúvida, o agente deve parar e pedir aprovação.
