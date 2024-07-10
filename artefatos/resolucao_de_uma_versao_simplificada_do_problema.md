# Resolução de uma versão simplificada do problema

## Sumário

[1. Clusterização](#c1)  
[2. Algoritmos de Rota](#c2) 

## <a name="c1">1. Clusterização</a>

&emsp; Para que seja possível desenvolver uma rota para cada leiturista da empresa, é necessário, antes, definir quais pontos irão para quais leituristas. Para isso, o grupo decidiu utilizar a clusterização, verificando quais pontos estão mais próximos e formando assim clusters de rotas. Cada cluster gerado pelo arquivo _clustering.py_ simboliza uma rota de 22 dias para um leiturista. 

&emsp; A geração dos clusters é feita a partir da inserção de um arquivo CSV que contém as coordenadas e endereços de todos os pontos a serem visitados. Em seguida, os pontos são divididos pelo número de leituristas definido (que pode variar de 1 a 500), gerando um cluster para cada leiturista.

&emsp; O algoritmo utilizado para realizar essa tarefa foi o KMeans da biblioteca `sklearn`, de forma a evitar clusters desbalanceados, ou seja, com mais ou menos pontos do que o ideal. O algoritmo busca implementar um balanceamento, ajustando os clusters após a divisão inicial para garantir que cada leiturista tenha uma carga de trabalho equitativa.

O código `clustering.py` implementa um algoritmo de clusterização utilizando o modelo KMeans da biblioteca `sklearn`. A função `cluster_and_balance` é responsável por agrupar os dados em um número especificado de clusters e, em seguida, balancear esses clusters.

### Funcionamento do Código:

1. **Entrada de Dados:** O código recebe um arquivo CSV contendo as coordenadas e endereços dos pontos a serem visitados.

2. **Inicialização do Modelo:** O modelo KMeans é inicializado com o número de clusters desejado, que corresponde ao número de leituristas.

3. **Ajuste do Modelo:** O modelo é ajustado aos dados, agrupando os pontos em clusters com base na proximidade.

4. **Balanceamento:** Após a clusterização inicial, o balanceamento é realizado para garantir que cada cluster tenha um número similar de pontos.

5. **Saída:** Os clusters gerados são utilizados para definir as rotas dos leituristas, cada um responsável por visitar os pontos de seu respectivo cluster ao longo de 22 dias.

## <a name="c2">2. Algoritmos de Rota</a>

&emsp; Os algoritmos implementados foram: Greedy e Genetic Algorithm. Devido ao tempo computacional elevado do Genetic Algorithm, não foi possível finalizar sua execução para esta versão do projeto. Portanto, apresentamos o resultado do Greedy Algorithm, que possui um tempo computacional $O(n^2)$.

### Greedy Algorithm

&emsp; O algoritmo guloso (Greedy) faz escolhas que parecem ser as melhores naquele momento, sem considerar o quadro geral. No contexto do Problema do Caixeiro Viajante (TSP), isso significa que o algoritmo seleciona a cidade mais próxima disponível em cada etapa, formando um ciclo hamiltoniano. Embora seja rápido e simples de implementar, o algoritmo guloso não garante a solução ótima para o TSP.

### Algoritmo Genético

&emsp; O algoritmo genético é comumente utilizado para resolver problemas complexos como o TSP. Ele inicia com uma população de rotas aleatórias e calcula a aptidão de cada uma, buscando, através de operações de mutação e crossover, otimizar as distâncias entre os pontos e encontrar a solução ótima.


&emsp; A combinação do Greedy Algorithm com o algoritmo genético permite encontrar uma solução de rota eficiente. O Greedy Algorithm fornece uma solução inicial rápida, que é refinada pelo algoritmo genético. A clusterização inicial garante que os pontos não se distanciem muito uns dos outros, enquanto a combinação dos algoritmos de rota otimiza a sequência das visitas.

### Funcionamento do Código:

1. **Criação da Rota:** A função `initialize_population` cria uma população inicial aleatória dentro do pontos fornecidos;

2. **Cálculo de rotas e distância:** A função `genetic_algorithm` inicializa o algoritmo genético a partir dessa população, realiza a troca de rotas e mutações próprios desse tipo de otimização;

3. **Greedy Algorithm:** A função `greedy_algorithm` roda por cima da solução ótima genética para verificar se nenhuma outra rota é melhor;

4. **Mapa:**  A função `draw_map` desenha os diferentes clusters com suas respectivas rotas no mapa.