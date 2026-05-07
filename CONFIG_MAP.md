# CONFIG_MAP — Mapa de Itens de Configuração

**Projeto:** Todo CLI  
**Versão do documento:** 1.0.0  
**Data:** 2026-05-07  
**Responsável:** Equipe de Desenvolvimento  

---

## 1. Política de Nomenclatura de Versões

Este projeto adota o **Versionamento Semântico (SemVer 2.0.0)** — [semver.org](https://semver.org).

### Formato

```
MAJOR.MINOR.PATCH[-PRE_RELEASE][+BUILD]
```

| Campo        | Quando incrementar                                                              | Exemplo                  |
|--------------|---------------------------------------------------------------------------------|--------------------------|
| `MAJOR`      | Mudanças incompatíveis com versões anteriores (quebra de API/contrato)          | `1.0.0` → `2.0.0`       |
| `MINOR`      | Nova funcionalidade compatível com versões anteriores                           | `1.0.0` → `1.1.0`       |
| `PATCH`      | Correção de bug compatível com versões anteriores                               | `1.0.0` → `1.0.1`       |
| `PRE_RELEASE`| Versões instáveis antes do lançamento oficial                                   | `1.1.0-alpha.1`          |
| `BUILD`      | Metadados de build (não afeta precedência)                                      | `1.0.0+20260507`         |

### Exemplos de Progressão

```
1.0.0-alpha.1   → Primeira versão de testes internos
1.0.0-beta.1    → Versão para testes externos
1.0.0           → Lançamento estável inicial
1.0.1           → Correção de bug (ex: validação de nome de tarefa)
1.1.0           → Nova funcionalidade (ex: comando `edit`)
1.1.1           → Correção de bug na nova funcionalidade
2.0.0           → Quebra de compatibilidade (ex: migração de JSON para banco de dados)
```

### Regras Complementares

- A versão `0.y.z` indica fase de desenvolvimento inicial — tudo pode mudar.
- Uma vez publicada, uma versão **nunca deve ser modificada**. Correções geram nova versão.
- Tags Git devem seguir o padrão `v<MAJOR>.<MINOR>.<PATCH>` (ex: `v1.0.0`).
- O `CHANGELOG.md` deve ser atualizado a cada nova versão.

---

## 2. Itens de Configuração (ICs)

### 2.1 Legenda de Tipos

| Tipo  | Descrição                                 |
|-------|-------------------------------------------|
| `SRC` | Código-fonte                              |
| `TST` | Arquivo de teste                          |
| `DOC` | Documentação                              |
| `CFG` | Arquivo de configuração / ambiente        |
| `SCR` | Script de automação                       |
| `ENV` | Plataforma / ambiente de execução         |
| `LIB` | Biblioteca ou framework externo           |

---

### 2.2 Código-Fonte

| ID     | Item de Configuração       | Caminho                    | Tipo  | Versão Atual | Descrição                                      |
|--------|----------------------------|----------------------------|-------|--------------|------------------------------------------------|
| IC-001 | Main — Ponto de entrada    | `src/main.py`              | `SRC` | 1.0.0        | CLI principal: comandos add, list, done, remove |
| IC-002 | Helpers — Utilitários      | `src/utils/helpers.py`     | `SRC` | 1.0.0        | Funções `format_task` e `validate_task_name`   |

---

### 2.3 Testes

| ID     | Item de Configuração       | Caminho                    | Tipo  | Versão Atual | Descrição                                      |
|--------|----------------------------|----------------------------|-------|--------------|------------------------------------------------|
| IC-003 | Testes unitários           | `tests/test_main.py`       | `TST` | 1.0.0        | Testes das funções do módulo `helpers`         |

---

### 2.4 Documentação

| ID     | Item de Configuração       | Caminho                    | Tipo  | Versão Atual | Descrição                                      |
|--------|----------------------------|----------------------------|-------|--------------|------------------------------------------------|
| IC-004 | Requisitos do sistema      | `docs/requisitos.md`       | `DOC` | 1.0.0        | Requisitos funcionais e não funcionais         |
| IC-005 | Arquitetura do sistema     | `docs/arquitetura.md`      | `DOC` | 1.0.0        | Visão geral dos componentes e fluxo de dados   |
| IC-006 | README                     | `README.md`                | `DOC` | 1.0.0        | Documentação de uso e exemplos de comandos     |
| IC-007 | Changelog                  | `CHANGELOG.md`             | `DOC` | 1.0.0        | Histórico de versões do projeto                |
| IC-008 | Mapa de Configuração       | `CONFIG_MAP.md`            | `DOC` | 1.0.0        | Este documento — lista de ICs e política SemVer|

---

### 2.5 Configuração de Ambiente

| ID     | Item de Configuração       | Caminho                    | Tipo  | Versão Atual | Descrição                                      |
|--------|----------------------------|----------------------------|-------|--------------|------------------------------------------------|
| IC-009 | Configurações da aplicação | `config/settings.json`     | `CFG` | 1.0.0        | Parâmetros: nome, versão, caminho de dados     |
| IC-010 | Gitignore                  | `.gitignore`               | `CFG` | 1.0.0        | Arquivos excluídos do controle de versão       |
| IC-011 | Dependências               | `requirements.txt`         | `CFG` | 1.0.0        | Lista de pacotes externos (atualmente vazia)   |

---

### 2.6 Scripts de Automação

| ID     | Item de Configuração       | Caminho                    | Tipo  | Versão Atual | Descrição                                      |
|--------|----------------------------|----------------------------|-------|--------------|------------------------------------------------|
| IC-012 | Script de build            | `scripts/build.sh`         | `SCR` | 1.0.0        | Executa testes e valida o build do projeto     |

---

### 2.7 Ambiente de Execução (Plataforma)

| ID     | Item de Configuração       | Versão Utilizada | Tipo  | Descrição                                             |
|--------|----------------------------|------------------|-------|-------------------------------------------------------|
| IC-013 | Python                     | 3.12.3           | `ENV` | Linguagem principal — runtime da aplicação            |
| IC-014 | Git                        | ≥ 2.x            | `ENV` | Sistema de controle de versão                         |
| IC-015 | Sistema Operacional        | Linux (Ubuntu)   | `ENV` | Plataforma de desenvolvimento e execução              |

---

### 2.8 Bibliotecas e Módulos (stdlib Python)

> Estas bibliotecas fazem parte da biblioteca padrão do Python (stdlib) e são controladas indiretamente pela versão do Python (IC-013). Não possuem versão independente.

| ID     | Item de Configuração       | Módulo Python    | Tipo  | Descrição                                             |
|--------|----------------------------|------------------|-------|-------------------------------------------------------|
| IC-016 | Serialização JSON          | `json`           | `LIB` | Leitura e escrita de dados em formato JSON            |
| IC-017 | Interface com sistema      | `os`             | `LIB` | Manipulação de caminhos e verificação de arquivos     |
| IC-018 | Argumentos de linha de cmd | `sys`            | `LIB` | Leitura de argumentos CLI (`sys.argv`)                |

---

## 3. Dados em Tempo de Execução (NÃO controlados)

Os itens abaixo são gerados em runtime e **não devem ser versionados** (estão no `.gitignore`):

| Item                   | Caminho               | Motivo da Exclusão                          |
|------------------------|-----------------------|---------------------------------------------|
| Dados das tarefas      | `config/tasks.json`   | Gerado em runtime; varia por usuário/ambiente|
| Cache Python           | `**/__pycache__/`     | Gerado automaticamente pelo interpretador   |
| Bytecode compilado     | `**/*.pyc`            | Derivado do código-fonte                    |

---

## 4. Resumo Quantitativo

| Tipo  | Quantidade |
|-------|-----------|
| `SRC` | 2         |
| `TST` | 1         |
| `DOC` | 5         |
| `CFG` | 3         |
| `SCR` | 1         |
| `ENV` | 3         |
| `LIB` | 3         |
| **Total** | **18** |

---

*Documento mantido sob controle de versão Git. Atualizar sempre que novos ICs forem adicionados ou removidos.*
