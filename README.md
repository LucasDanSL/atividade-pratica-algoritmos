# 🧠 Atividade de Algoritmos e Complexidade

## 📝 Descrição do Projeto

Este repositório reúne três implementações de algoritmos em Python, desenvolvidas para ilustrar conceitos fundamentais da Complexidade de Tempo (Notação Big O). A atividade integra os conteúdos da disciplina Algoritmos e Complexidade, e tem como objetivo demonstrar, na prática, o comportamento de diferentes ordens de crescimento.

Para a realização da tarefa, foi utilizada a ferramenta **Gemini CLI (Cliente MCP)** — um ambiente de linha de comando que permite gerar códigos, realizar testes e documentar projetos de forma automatizada, de modo semelhante ao MCP Client (Cliente de Computação Preditiva Multimodal).

## 💻 Ferramentas e Ambiente

* Ferramenta: Gemini CLI
* Dependência: Node.js (versão 20 ou superior)

O Gemini CLI foi configurado e utilizado para se comunicar com o modelo Gemini, possibilitando a geração dos códigos Python, suas respectivas documentações e testes de validação.

## Prompt Principal Utilizado

Gere 3 códigos Python, cada um implementando um algoritmo diferente:
1️⃣ Um com complexidade O(n) (Linear)
2️⃣ Um com complexidade O(n²) (Quadrática)
3️⃣ Um com complexidade O(log n) (Logarítmica)

Inclua em cada função a notação da complexidade no comentário, um exemplo de uso e uma breve explicação do funcionamento. Salve cada implementação em um arquivo separado.

## 🔬 Testes e Resultados

### Algoritmo Linear – O(n)

O script `linear_search.py` calcula o valor máximo de uma lista, percorrendo todos os elementos.

### Algoritmo Quadrático – O(n²)

O script `bubble_sort.py` executa a ordenação passo a passo, evidenciando o comportamento quadrático.

### Algoritmo Logarítmico – O(log n)

O script `binary_search.py` realiza uma busca binária, localizando um elemento específico em uma lista ordenada.

## 📌 Exemplo de Execução

O Gemini CLI gera o arquivo `linear_search.py`, com a função `encontrar_maximo` documentada e a complexidade indicada como O(n).

## ⚙️ Como Acessar e Executar

1️⃣ Clone o repositório:

```bash
git clone https://github.com/LucasDanSL/atividade-pratica-algoritmos.git
```

2️⃣ Acesse o diretório:

```bash
cd atividade-pratica-algoritmos
```

3️⃣ Execute qualquer script (exemplo):

```bash
python bubble_sort.py
```

Repita para `linear_search.py` ou `binary_search.py` conforme desejar testar os algoritmos.

## 🧠 Aprendizados

* Implementação prática de algoritmos com diferentes complexidades
* Visualização do comportamento do tempo de execução com listas de diferentes tamanhos
* Aplicação da notação Big O na análise de desempenho
