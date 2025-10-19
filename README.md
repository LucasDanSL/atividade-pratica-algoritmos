🧠 Atividade de Algoritmos e Complexidade
📝 Descrição do Projeto

Este repositório reúne três implementações de algoritmos em Python, desenvolvidas para ilustrar conceitos fundamentais da Complexidade de Tempo (Notação Big O).
A atividade integra os conteúdos da disciplina Algoritmos e Complexidade, e tem como objetivo demonstrar, na prática, o comportamento de diferentes ordens de crescimento.

Para a realização da tarefa, foi utilizada a ferramenta Gemini CLI (Cliente MCP) — um ambiente de linha de comando que permite gerar códigos, realizar testes e documentar projetos de forma automatizada, de modo semelhante ao MCP Client (Cliente de Computação Preditiva Multimodal).

💻 Ferramentas e Ambiente

Ferramenta: Gemini CLI

Dependência: Node.js (versão 20 ou superior)

O Gemini CLI foi configurado e utilizado para se comunicar com o modelo Gemini, possibilitando a geração dos códigos Python, suas respectivas documentações e testes de validação.

Prompt principal utilizado:

Gere 3 códigos Python, cada um implementando um algoritmo diferente:
1️⃣ Um com complexidade O(n) (Linear)
2️⃣ Um com complexidade O(n²) (Quadrática)
3️⃣ Um com complexidade O(log n) (Logarítmica)

Inclua em cada função a notação da complexidade no comentário, um exemplo de uso e uma breve explicação do funcionamento.
Salve cada implementação em um arquivo separado.

🔬 Testes e Resultados

A seguir, os testes realizados comprovam o funcionamento e a análise de complexidade de cada implementação:

Algoritmo Linear – O(n)
O script linear_search.py calcula o valor máximo de uma lista, percorrendo todos os elementos.
Print do terminal mostra a execução bem-sucedida e o resultado final.

Algoritmo Quadrático – O(n²)
O script bubble_sort.py executa a ordenação passo a passo, evidenciando o comportamento quadrático.
Print mostra a transformação da lista original em sua versão ordenada.

Algoritmo Logarítmico – O(log n)
O script binary_search.py realiza uma busca binária, localizando um elemento específico em uma lista ordenada.
Print demonstra a busca do número 7, encontrado na posição 3.

Exemplo de execução:
A imagem de saída mostra o Gemini CLI gerando o arquivo linear_search.py, com a função encontrar_maximo documentada e a complexidade indicada como O(n).
