# Documento de Requisitos - Projeto de Programação Funcional

## Capa
**Nome do Projeto:** Sistema de Tarefas Funcional  
**Disciplina:** Programação Funcional  
**Integrantes da Equipe:**
- Maycon Andrade – Matrícula XXXXX – Implementação / Testes  
- Amanda Alves Eloi - 2326260 – Implementação / Documentação  
- Esther de Souza Ramalho - 2313582 – Documentação / Revisão  
-  - 2418803 – Testes / Auxílio  

---

## Papéis
| Integrante                       | Papel no Projeto                 |
|----------------------------------|----------------------------------|
| Maycon Barroso Andrade           | Implementação do código e testes |
| Amanda Alves Eloi                | Implementação e documentação     |
| Esther de Souza Ramalho          | Documentação e revisão           |
| Marcos Aurélio Sousa de Carvalho | Testes e auxílio na implementação|

---

## Requisitos Funcionais
1. Criar, listar e filtrar tarefas.  
2. Marcar tarefas como concluídas.  
3. Filtrar tarefas por prioridade.  
4. Execução de um fluxo de demonstração das funcionalidades.  

### Mapeamento de Requisitos para Funções
| Requisito                                      | Função / Código Correspondente                    |
|------------------------------------------------|--------------------------------------------------|
| Criar tarefas com prioridade                   | `criar_adicionador_prioridade(prioridade)`      |
| Listar tarefas de prioridade alta             | `listar_tarefas_altas()`                        |
| Filtrar tarefas                                | `filtrar_tarefas(filtro)`                       |
| Marcar tarefa como concluída                   | `marcar_concluida` (lambda)                     |
| Fluxo de demonstração                           | `executar_demo()` (opcional)                    |

---

## Requisitos Não Funcionais
1. Código em Python, legível e organizado.  
2. Aplicação de conceitos de Programação Funcional.  
3. Testes unitários para validação das funcionalidades principais.  

---

## Programação Funcional
No código-fonte do sistema, os seguintes conceitos foram aplicados:

1. **Função Lambda**  
   - **Local de uso:** marcar tarefas como concluídas.  
   - **Código:**  
     ```python
     marcar_concluida = lambda tarefa: {**tarefa, 'concluida': True}
     ```

2. **List Comprehension**  
   - **Local de uso:** listar nomes de tarefas de prioridade alta.  
   - **Código:**  
     ```python
     def listar_tarefas_altas():
         return [t['nome'] for t in tarefas if t['prioridade'] == 'alta']
     ```

3. **Closure**  
   - **Local de uso:** criar função de adição de tarefa com prioridade fixa.  
   - **Código:**  
     ```python
     def criar_adicionador_prioridade(prioridade):
         def adiciona_tarefa(nome):
             tarefa = {'nome': nome, 'prioridade': prioridade, 'concluida': False}
             tarefas.append(tarefa)
             return tarefa
         return adiciona_tarefa
     ```

4. **Função de Alta Ordem**  
   - **Local de uso:** filtrar tarefas usando função passada como parâmetro.  
   - **Código:**  
     ```python
     def filtrar_tarefas(filtro):
         return list(filter(filtro, tarefas))
     ```

---

## Casos de Teste
- Testar adição de tarefas com diferentes prioridades.  
- Testar listagem de tarefas de prioridade alta.  
- Testar filtragem de tarefas.  
- Testar marcação de tarefas como concluídas.  

Todos os testes foram implementados em `tests.py` e executados com sucesso.

---

## Observações
- **Uso do ChatGPT:** Para a estruturação do projeto, fizemos a seguinte pergunta ao ChatGPT: "Sugira uma estrutura de arquivos para um projeto Python simples com interface Tkinter e testes unitários." A resposta sugerida pelo chatbot foi uma estrutura contendo os arquivos main.py, tests.py e um README.md, que serviu de base inicial para nossa organização. P ara as ideias de saída, perguntamos: "Como posso exibir uma lista de tarefas em Python de forma clara no terminal?" O chatbot sugeriu formatos de texto como "Tarefa X [Prioridade] - Status (Concluída/Pendente)", o que nos inspirou no design da exibição das tarefas na interface gráfica.
- Todas as funções do código estão mapeadas neste documento, garantindo a fidedignidade entre documentação e implementação.

---

## Conclusão
O projeto atende a todos os requisitos da disciplina de Programação Funcional, utilizando lambda, list comprehension, closure e função de alta ordem. Todos os casos de teste estão contemplados e executáveis.
