# Arquitetura do Sistema

## Visão Geral
Aplicação CLI de gerenciamento de tarefas (To-Do List).

## Componentes
- `main.py`: Ponto de entrada, interface CLI
- `src/utils/helpers.py`: Funções auxiliares de validação e formatação
- `config/settings.json`: Configurações da aplicação

## Fluxo de Dados
CLI → main.py → src/ → tasks.json (persistência)
