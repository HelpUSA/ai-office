# 03 - Orquestração

## Papel do orquestrador

O orquestrador é o gerente central do escritório.

Ele deve:

1. Receber uma solicitação.
2. Entender o objetivo.
3. Classificar o risco.
4. Escolher o agente.
5. Criar uma tarefa.
6. Acompanhar execução.
7. Enviar para auditoria quando necessário.
8. Entregar resultado final.

## Tipos de tarefa

### read_only

Apenas leitura.

Exemplos:

- Ler arquivos.
- Inspecionar projeto.
- Gerar resumo.

### suggest_only

Apenas sugestão.

Exemplos:

- Propor patch.
- Sugerir campanha.
- Criar plano.

### write_guarded

Pode escrever em área permitida.

Exemplos:

- Criar documentação.
- Criar template.
- Gerar relatório.

### execute_guarded

Pode executar comandos seguros.

Exemplos:

- Rodar testes.
- Rodar lint.
- Gerar build local.

### approval_required

Exige aprovação humana.

Exemplos:

- Deploy.
- Commit.
- Push.
- Envio externo.
- Campanhas pagas.
- Exclusão de arquivos.
