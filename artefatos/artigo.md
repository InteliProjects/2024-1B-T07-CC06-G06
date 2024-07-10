---
title: Modelo para o artigo
author: Inteli
date: Abril de 2024
abstract: Escreva aqui o resumo deste artigo.
---


# Introdução


<div align="justify">


&emsp;A otimização de rotas de leitura de hidrômetros é uma questão crucial para empresas de saneamento, especialmente em grandes cidades onde a demanda e a extensão territorial aumentam a complexidade operacional. A Aegea, uma das maiores empresas de saneamento básico no Brasil, enfrenta o desafio de gerenciar e otimizar as rotas de leitura de hidrômetros de seus clientes, um processo essencial para o registro do consumo mensal de água e a consequente faturação. Este processo envolve a definição diária de rotas de leitura para cerca de 400 leituristas, que atendem mais de 1,6 milhões de pontos de leitura mensalmente apenas na região de Águas do Rio, no estado do Rio de Janeiro.


&emsp;A importância da otimização dessas rotas reside não apenas na melhoria da produtividade, mas também na eficiência operacional e na redução de custos. A otimização logística é uma ferramenta poderosa para melhorar a competitividade das empresas, proporcionando uma melhor utilização dos recursos disponíveis e uma maior satisfação dos clientes. No contexto da Aegea, essa otimização é fundamental para garantir que os leituristas possam realizar o maior número possível de leituras dentro do seu horário de trabalho, respeitando as restrições de tempo e segurança no deslocamento entre as leituras.


&emsp;O objetivo deste projeto é desenvolver um algoritmo capaz de maximizar a eficiência na geração de rotas para a leitura de hidrômetros, buscando reduzir o número total de rotas e o tempo de conclusão de cada uma. Isto não só melhora a eficácia da leitura e entrega das contas, mas também contribui para a sustentabilidade do processo de faturamento da empresa. A literatura "Modelo Heurístico para Otimização de Rotas nos Serviços de Leitura de Hidrômetros" sobre otimização de rotas e logística urbana destaca que a integração de técnicas avançadas de análise de dados e algoritmos de otimização pode levar a melhorias significativas na eficiência operacional (PUREZA, 2015)[^9].


&emsp;A resolução deste problema é limitada por algumas restrições operacionais e recursos finitos. A primeira delas é a carga horária diária dos leituristas, que estabelece um limite máximo de horas de trabalho. Outra limitação envolve a quantidade de leituristas disponíveis e a velocidade de deslocamento de cada um. Por fim, o ponto inicial de cada rota também é uma restrição importante, pois deve ser considerado no planejamento para garantir trajetos mais eficientes. Estas limitações influenciam diretamente a capacidade de leitura diária de cada leiturista e, consequentemente, a eficácia do processo de leitura de hidrômetros (INOVAMOBIL, 2024)[^10].


&emsp;A natureza do problema da Aegea traz uma complexidade tão alta que torna-o computacionalmente inviável de ser solucionado de maneira determinística em um período de tempo aceitável, já que esse tipo de problema não possui soluções determinísticas em tempo polinomial. Contudo, apesar de atualmente ser impossível encontrar a solução ótima, existem técnicas para encontrar soluções muito boas. As aproximações são feitas a partir de heurísticas, ou seja, são utilizadas informações e intuição a respeito da instância do problema e da sua estrutura para resolvê-lo de forma rápida e com resultados satisfatórios.




# Trabalhos Relacionados


&emsp;O problema enfrentado na Aegea na roteirização de seus leituristas é análogo aos desafios de logística que diversas empresas de diferentes setores enfrentam no seu cotidiano. Alguns exemplos desse tipo de problema estão no supply chain de empresas de varejo, onde deve-se coordenar quais veículos de transporte irão fazer as entregas para determinados clientes, ou até mesmo no setor público, com a roteirização de caminhões de lixo para realizarem a coleta de modo mais eficiente.


&emsp;Um problema muito similar ao da Aegea também já foi abordado em um estudo conduzido por SINHA ROY et al(2022)[^5], onde o desafío enfrentado era a criação de rotas robustas e econômicas dos leituristas de empresas do setor público, sendo essas leituras realizadas dentro de um sistema automático utilizando tags RFID para registrar os valores dos contadores nas casas. Tendo em vista o sistema de leituras automáticas, apesar de serem muito mais eficientes, elas podem falhar devido à natureza descontínua dos sinais RFID e à variabilidade no alcance devido às  condições climáticas, obstáculos e vida útil das baterias. Essas falhas aumentam os custos operacionais ao exigir visitas adicionais. Para abordar essas incertezas, foram desenvolvidos modelos estatísticos Bayesianos hierárquicos, que demonstram melhor desempenho em simulações com dados reais, oferecendo uma solução mais robusta e econômica para gerar rotas de leitura.


&emsp;Um exemplo de heurística são os algoritmos genéticos, que foram aplicados e testados no projeto. Eles se baseiam na intuição da evolução e da seleção natural dos seres vivos, tendo como teoria de que o cruzamento das melhores soluções de cada geração, junto com sua seleção e também possíveis mutações, o resultado final tende à uma solução próxima da ótima. Um exemplo de estudo baseado em algoritmos genéticos foi o conduzido por OUERTANI et al(2023)[^6]. O artigo aborda o problema de transporte de resíduos de saúde (HCW), modelado como um problema de roteamento de veículos (uma variação do problema do caixeiro viajante, onde existem diversos 'caixeiros' para realizar as menores rotas possíveis) com múltiplos compartimentos (MC-VRP). Foi proposto um algoritmo genético adaptativo para otimizar as rotas, garantindo a separação dos resíduos perigosos dos não perigosos durante o transporte. Os resultados experimentais mostraram que a abordagem proposta supera as metodologias existentes, oferecendo soluções mais eficazes e econômicas.


&emsp;Outra heurística testada no projeto foi a Ant Colony Optimization (ACO), que simula o comportamento das colônias de formigas, em que, de maneira simplificada, através dos feromônios que são depositados por cada formiga, os caminhos mais curtos que possuem comida são mais explorados pela colônia. Dessa forma, é possível assimilar esse comportamento para o Problema do Caixeiro Viajante (TSP) ou para o Problema de Roteamento de Veículos (VRP), em que as formigas exploram e conseguem encontrar soluções de rotas próximas da solução ótima. O artigo de BELL e MCMULLEN(2004)[^7] aborda o assunto aplicando a otimização ACO à VRP. A metodologia simula processos de tomada de decisão das formigas, adaptando o algoritmo ACO para buscar múltiplas rotas no VRP. A pesquisa mostrou que o ACO é eficaz em encontrar soluções próximas ao ótimo conhecido, especialmente para problemas maiores, comparando favoravelmente com outros métodos de solução em termos de tempo computacional e eficiência.


&emsp;Uma abordagem distinta das heurísticas tradicionais é a utilização de redes neurais, como discutido no artigo  de RODRÍGUEZ-ESPARZA et al(2024)[^8]. Este estudo propõe um novo método que combina Simulated Annealing adaptativo com aprendizado por reforço, tratado como um problema multi-armed bandit. Os resultados experimentais demonstram que esta metodologia proporciona uma solução mais eficiente e robusta, especialmente ao lidar com a incerteza e a variabilidade das condições de leitura dos medidores, oferecendo uma alternativa inovadora e eficaz às heurísticas tradicionais.




# Resultados obtidos


&emsp;No estudo realizado, foi explorada a aplicação da otimização de rotas para leitura de hidrômetros da empresa parceira do projeto, Aegea. A otimização das rotas dos leituristas foi feita através do algoritmo de clusterização k-means e dos algoritmos de rota ant-colony, algoritmo genético e algoritmo guloso. Foi minimizado o número de leituras necessárias para percorrer todos os pontos e foi minimizado o tempo total de deslocamento. Isso foi feito considerando restrições operacionais como a jornada de trabalho dos leituristas e a distância percorrida, além de dados extras como o tempo de leitura, distância percorrida, e a quantidade de hidrômetros lidos por dia.


## Métricas estabelecidas


&emsp;Para avaliar a eficácia do algoritmo de otimização de rotas, foram estabelecidas várias métricas chave que foram cuidadosamente medidas e analisadas. A seguir, detalhamos cada métrica e seu impacto no processo de otimização:


1. Redução no número de leituristas: Reduzir o número de leituristas necessários diminui os custos operacionais, isso ocorre porque um menor número de leituristas é capaz de cobrir a mesma área de serviço. Isso resulta em economias de escala, permitindo que a Aegea possa alocar recursos de forma mais eficiente e potencialmente expandir a cobertura de leitura sem aumentar os custos proporcionais.


2. Tempo Total de Conclusão das Rotas: A redução no tempo total de conclusão das rotas aumenta a produtividade dos leituristas, permitindo que eles completem mais leituras em um período de tempo menor. Isso pode levar a um menor desgaste dos funcionários e a possibilidade de incorporar um número maior de leituras dentro da mesma jornada de trabalho, minimizando, por consequência, o número de leituristas necessários para realizar as rotas.


3. Cobertura Completa das Leituras: Garantir a cobertura completa das leituras é essencial para manter a precisão e a consistência dos dados de consumo, que são críticos para o faturamento e a satisfação do cliente. A falta de cobertura pode resultar em leituras estimadas, que podem ser imprecisas e causar problemas de cobrança e insatisfação do cliente.




## Resultados da otimização


&emsp;O algoritmo desenvolvido foi capaz de recomendar a formação de 57 clusters, representando o número de leituristas necessários para cobrir a área de leitura. Cada cluster, portanto, corresponde a um leiturista e sua respectiva área de atuação. Além da recomendação de clusters, a próxima etapa envolveu a roteirização das leituras dentro de cada cluster. O resultado dessa fase foi uma média de 160 km percorridos por cada cluster, representando a rota total de um leiturista em 22 dias de trabalho. Para facilitar a operação diária, essa rota foi subdividida em sub-rotas diárias, garantindo que cada leiturista tivesse um trajeto otimizado e gerenciável dentro de sua jornada de trabalho.


&emsp;Os resultados a seguir estão ordenados pelo tempo total de cada rota e apresentam na primeira coluna o identificador de cada cluster e na segunda coluna o tempo total necessário para percorrer o cluster. O tempo total foi calculado a partir da velocidade média de caminhada dos leituristas com valor de 5 km/h. Leve em conta que cada cluster representa uma rota que pode ser realizada por um leiturista no curso de um mês. Cada leiturista possui 6 horas de carga diária e 22 dias de trabalho por mês, ou seja, 132 horas mensais destinadas ao trabalho.


| Identificador | Tempo necessário (horas)     |
|-------|-----------|
| 49    | 116.9135  |
| 7     | 119.8178  |
| 46    | 120.4005  |
| 37    | 121.7602  |
| 42    | 122.0942  |
| 41    | 122.2997  |
| 28    | 123.0279  |
| 1     | 123.4516  |
| 3     | 123.5435  |
| 23    | 123.9606  |
| 16    | 124.0612  |
| 55    | 124.1557  |
| 0     | 124.2088  |
| 21    | 124.6749  |
| 27    | 124.8729  |
| 35    | 125.2099  |
| 9     | 125.5244  |
| 12    | 125.6926  |
| 44    | 125.7517  |
| 10    | 125.9267  |
| 34    | 125.9893  |
| 38    | 126.0228  |
| 32    | 126.0853  |
| 25    | 126.3547  |
| 29    | 126.3756  |
| 15    | 126.4523  |
| 6     | 126.5385  |
| 56    | 126.5849  |
| 48    | 126.6241  |
| 24    | 126.8147  |
| 14    | 126.9478  |
| 40    | 126.9584  |
| 5     | 127.0577  |
| 11    | 127.0985  |
| 53    | 127.4252  |
| 20    | 127.6069  |
| 2     | 127.6776  |
| 54    | 127.7578  |
| 33    | 127.7947  |
| 50    | 127.8996  |
| 26    | 127.9363  |
| 17    | 128.2757  |
| 51    | 128.6665  |
| 45    | 128.6869  |
| 22    | 128.8001  |
| 47    | 128.8884  |
| 19    | 128.9774  |
| 36    | 129.1821  |
| 4     | 129.2910  |
| 8     | 129.6183  |
| 43    | 130.8496  |
| 52    | 130.9082  |
| 39    | 130.9572  |
| 31    | 131.6070  |
| 18    | 131.8239  |
| 30    | 132.1948  |
| 13    | 132.2942  |






## Discussão e Análise de resultados


&emsp;Note que os resultados apresentados possuem pouca variabilidade no tempo total das rotas, demonstrando uma distribuição equalizada dos pontos em clusters e uma alta consistência na solução das rotas. Isso possibilita uma abordagem simplificada na distribuição das rotas para os leituristas, uma vez que permite estabelecer como meta mensal para cada leiturista a finalização de um cluster.


&emsp;Esses resultados não apenas demonstram a eficácia do algoritmo na criação de rotas otimizadas, mas também apontam para uma potencial redução nos custos operacionais e um aumento na eficiência do processo de leitura de hidrômetros. Com rotas mais curtas e bem definidas, a Aegea pode melhorar a produtividade dos seus leituristas, reduzir o tempo de deslocamento e assegurar uma cobertura completa e precisa das leituras mensais.


&emsp;A eficácia do algoritmo desenvolvido foi avaliada com base nas métricas estabelecidas. A redução no número de leituristas necessários resultou em uma diminuição significativa dos custos operacionais, pois menos leituristas foram necessários para cobrir a mesma área de serviço. A análise mostrou que a empresa poderia economizar recursos significativos, permitindo uma alocação mais eficiente e potencialmente expandindo a cobertura de leitura sem aumentar os custos proporcionais.


&emsp;Em termos de aplicação prática, os resultados indicam que a Aegea pode implementar o algoritmo para otimizar suas operações de leitura de hidrômetros, trazendo benefícios significativos em termos de redução de custos e aumento de eficiência. O uso de técnicas de otimização baseadas em clustering e roteirização mostrou-se eficaz na resolução de problemas complexos de logística, como demonstrado no estudo.


## Conclusão


&emsp;O presente estudo teve como objetivo otimizar as rotas de leitura de hidrômetros da Aegea, uma grande empresa de saneamento básico, visando maximizar a eficiência operacional e reduzir custos. Com base nos resultados obtidos, foi possível concluir que o algoritmo desenvolvido, utilizando técnicas de clustering e roteirização, proporcionou melhorias significativas na logística de leitura de hidrômetros. O número de leituristas necessários foi reduzido, o que diminuiu os custos operacionais e permitiu uma alocação mais eficiente dos leituristas. Além disso, a diminuição do tempo total de deslocamento possibilitou um aumento na quantidade de casas visitadas pelos funcionários, assegurando uma cobertura mais completa das leituras.


&emsp;Entretanto, alguns problemas não foram totalmente resolvidos pela nossa solução. Obstáculos físicos como avenidas de tráfego intenso, edifícios e outras barreiras urbanas podem impactar significativamente a eficácia do algoritmo de roteirização. Essas barreiras não foram completamente integradas na modelagem atual, o que pode levar a trajetos subótimos em áreas urbanas densas e complexas. Portanto, apesar das melhorias obtidas, ainda há espaço para ajustes que possam acomodar essas variáveis urbanas.


&emsp;Para trabalhos futuros, sugere-se explorar o uso de outras heurísticas e metaheurísticas, como algoritmos baseados em aprendizado de máquina, para aprimorar ainda mais a eficiência da roteirização. Além disso, a investigação da integração de dados em tempo real, como condições de tráfego e clima, bem como a consideração de obstáculos físicos como avenidas e edifícios no processo de roteirização, seria interessante para tornar o algoritmo ainda mais dinâmico e responsivo às condições operacionais.
# Referências




[^1]: Página Inicial da Aegea. Disponível em: <https://www.aegea.com.br/>. Acesso em: 9 maio. 2024.
[^5]: SINHA ROY, D.; DEFRYN, C.; GOLDEN, B.; WASIL, E. (2022). Data-driven optimization and statistical modeling to improve meter reading for utility companies. Computers & Operations Research, 145, 105844. Disponível em : <https://www.sciencedirect.com/science/article/abs/pii/S0305054822001216?via%3Dihub>.
[^6]: OUERTANI, N.; BEN-ROMDHANE, H .; NOUAOURI, I.; ALLAOUI, H.; KRICHEN, S.; "A multi-compartment VRP model for the health care waste transportation problem" Journal of Computational Science, Volume 72, September 2023, 102104. Disponível em : <https://www.sciencedirect.com/science/article/abs/pii/S1877750323001643>.
[^7]: BELL, J. E.; MCMULLEN, P. R. (2004). Ant colony optimization techniques for the vehicle routing problem. Advanced Engineering Informatics, 18(1), 41-48. Disponível em : <https://www.sciencedirect.com/science/article/abs/pii/S1474034604000060?via%3Dihub>.
[^8]: RODRÍGUEZ-ESPARZA, E.; MASEGOSA, A. D.; OLIVA, D.; ONIEVA, E. (2024). A new Hyper-heuristic based on Adaptive Simulated Annealing and Reinforcement Learning for the Capacitated Electric Vehicle Routing Problem. Expert Systems with Applications, 252(Part B), 124197. Disponível em: <https://www.sciencedirect.com/science/article/pii/S0957417424010637?via%3Dihub>
[^9]: PUREZA, S.A.O. Modelo Heurístico para Otimização de Rotas nos Serviços de Leitura de Hidrômetros. XXXV CNMAC, Natal-RN, 2015. Disponível em: https://www.researchgate.net/publication/300688888_Modelo_Heuristico_para_Otimizacao_de_Rotas_nos_Servicos_de_Leitura_de_Hidrometros
[^10]: INOVAMOBIL. Leitura de Hidrômetros: Processo Manual Vs. Automatizado. Disponível em: https://inovamobil.com.br/blog/leitura-de-hidrometros-de-agua-processo-manual-vs-automatizado/. Acesso em 17/06/2024.





