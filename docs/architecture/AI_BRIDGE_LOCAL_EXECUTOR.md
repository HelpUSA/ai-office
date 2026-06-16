# AI Bridge Local como Executor Seguro

## Papel no AI Office

O AI Bridge Local deve ser usado como braço local executor do escritório.

Ele não deve ser o produto principal, mas sim o componente que permite ao AI Office operar com segurança em repositórios locais.

## Responsabilidades

- Executar comandos locais autorizados.
- Inspecionar repositórios.
- Rodar git status.
- Rodar git diff.
- Rodar testes.
- Rodar smokes.
- Aplicar patches controlados.
- Registrar resultados.
- Retornar status para o orquestrador.

## Fluxo sugerido

1. Usuário cria tarefa no AI Office.
2. HelpUS CEO classifica a tarefa.
3. HelpUS Dev ou outro agente cria plano.
4. Se houver execução local, a tarefa vai para bridge-relay.
5. bridge-relay encaminha para AI Bridge Local.
6. AI Bridge Local executa com gates.
7. Resultado volta como evento padronizado.
8. HelpUS Auditor revisa.
9. Orquestrador consolida resposta.

## O que o bridge não deve fazer sozinho

- Commit.
- Push.
- Deploy.
- Apagar arquivos em massa.
- Alterar produção.
- Acessar secrets sem aprovação.
- Enviar mensagens externas.

## Eventos importantes

- queued
- running
- completed
- failed
- blocked
- waiting_approval

## Resultado esperado

O AI Bridge Local permite que o escritório execute tarefas reais em ambiente local sem perder controle, rastreabilidade e segurança.
