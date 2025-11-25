# Grafos_LeetCode_20

## Alunos  
| Matrícula | Nome |  
|-----------|------|  
| 200035703 | Breno Alexandre Soares Garcia |  
| 211062900 | Caio Lucas Lelis Borges |  

## Descrição do projeto
Para essa entrega nossa dupla optou pela prática de questões envolvendo grafos no LeetCode.

## Vídeo


## Sobre as questões

### Questão 133(Breno Alexandre) - Clone Graph
O que a questão pede:
Copiar um grafo não direcionado onde cada nó possui um valor e uma lista de vizinhos.
É necessário criar uma nova estrutura de grafo totalmente independente, preservando conexões e evitando loops infinitos em grafos com ciclos.

Como resolvi:
Usei DFS com um dicionário para mapear cada nó original ao seu clone.
A função recursiva cria o clone do nó atual, armazena no dicionário e continua clonando os vizinhos.
Se um nó já tiver sido clonado, retorna a cópia imediatamente.
Isso evita recriação de nós e impede recursão infinita em grafos cíclicos.

### Questão 329(Breno Alexandre) - Longest Increasing Path in a Matrix
O que a questão pede:
Encontrar o comprimento do maior caminho estritamente crescente em uma matriz 2D.
O caminho pode seguir para cima, baixo, esquerda ou direita, mas apenas se o próximo valor for maior que o atual.

Como resolvi:
Usei DFS com memoização.
Para cada célula `(i, j)`, aplico DFS para explorar vizinhos com valores maiores.
Guardo em `dp[i][j]` o maior caminho começando naquela posição para evitar recomputações.
O resultado final é o maior valor encontrado entre todas as células.

### Questão N(Caio Lelis) - nome da questao
O que a questão pede:


Como resolvi:


### Questão N(Caio Lelis) - nome da questao
O que a questão pede:


Como resolvi:


## Conclusões
A prátiva das questões nos ajudou bastante a fixar os conceitos de grafos, além de nos proporcionar o contato com diferentes tipos de problemas que podem ser resolvidos com essas estruturas de dados.

## Referências
> LEETCODE. Problem 133 – Clone Graph. Disponível em: https://leetcode.com/problems/clone-graph. Acesso em: 24 nov. 2025.
> 
> LEETCODE. Problem 329 – Longest Increasing Path in a Matrix. Disponível em: https://leetcode.com/problems/longest-increasing-path-in-a-matrix. Acesso em: 24 nov. 2025.