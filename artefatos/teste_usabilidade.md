# Testes de usabilidade
&emsp;O teste de usabilidade é uma etapa crucial no desenvolvimento de software e produtos digitais, pois permite avaliar a facilidade de uso e a experiência do usuário com o sistema. Este documento visa detalhar o processo de teste de usabilidade realizado, incluindo os objetivos, metodologia, participantes, tarefas, resultados e conclusões.

&emsp;Os testes de usabilidade foram conduzidos para identificar possíveis pontos de melhoria na interface e na interação dos usuários com o sistema. As informações coletadas durante os testes fornecerão insights valiosos para orientar as futuras iterações do design, garantindo uma experiência de usuário eficiente e satisfatória.

## Objetivos
- Avaliar a facilidade de uso do sistema;
- Identificar obstáculos e dificuldades enfrentadas pelos usuários;
- Coletar feedback qualitativo sobre a experiência do usuário;
- Propor melhorias baseadas nos resultados dos testes.

## Condução dos testes
### Participantes
&emsp;Os testes foram conduzidos com um grupo diversificado de usuários representativos do público-alvo do sistema. Cada participante foi selecionado com base em critérios como familiaridade com tecnologias semelhantes, variando em níveis de experiência e conhecimento técnico.

### Tarefas
&emsp;Os participantes foram solicitados a completar um conjunto de tarefas específicas no sistema. Essas tarefas foram projetadas para cobrir as principais funcionalidades e fluxos de uso do sistema. As tarefas incluíram, mas não se limitaram a:

- Upload do arquivo de rotas;
- Identificar clusters;
- Filtros nos clusters;
- Realizar otimização de um cluster;
- Buscar uma rota oitmizada;
- Analisar o inicio da rota.

### Procedimentos
**Preparação:** Os participantes foram recebidos e orientados sobre o propósito do teste e o que seria esperado deles. 

**Execução:** Durante os testes, cada participante foi observado e suas ações foram registradas. Pedimos aos participantes que "pensassem em voz alta" enquanto realizavam as tarefas, expressando seus pensamentos, dificuldades e reações.

**Coleta de Dados:** Dados qualitativos e quantitativos foram coletados, incluindo:
- Tempo para completar cada tarefa;
- Número de erros cometidos;
- Observações sobre comportamentos notáveis;
- Feedback verbal dos participantes.


# Resultados dos testes
Os testes foram realizados com alunos do inteli, explicando o contexto do problema e solução desenvolvida. Foi apresentado uma contextualização dos algoritmos utilizados, proporcionando maior conhecimento dos usuários sobre a aplicação desenvolvida.

## Teste: Upload do arquivo
**Tarefa 1:** Realizar o upload de um arquivo.
- **Descrição da Tarefa:** Inserir um arquivo com as rotas no sistema.
- **Expectativa:** É esperado que o usuário consiga inserir o arquivo `.csv` para que seja calculado as rotas, sem esforço.
- **Observações:** Para esse teste foi fornecido um arquivo de teste e explicado o que teria que ter nesse arquivo. Foi preciso explicar para os usuários sobre a utilização do botão para que dessem prosseguimento aos outros testes.
- **Feedback do Usuário:** Os usuário não encontraram o botão de 'selecionar arquivo', confundiram com o botão de 'adicionar arquivo'. Acreditam que isso possa ser melhorado deixando mais intuitivo.
- **Resultado:**  100% dos usuários que testaram a aplicação não conseguiram encontrar o botão

## Exemplo de teste: Identificar Identificar Clusters
**Tarefa 2:** Analisar os clusters gerados e os resultados dos clusters.
- **Descrição da Tarefa:** Após a inserção do arquivo, o usuário será redirecionado para a tela dos clusters. Nessa tela terá um mapa com os clusters e alguns dados sobre distância, número de clusters e tempo de execução.
- **Expectativa:** É esperado que o usuário compreenda onde está localizado cada cluster e os dados gerados a partir do algoritmo.
- **Observações:** --
- **Feedback do Usuário:** Um dos usuários, Raphaela Ferraz, enquanto esperava o carregamento dos clusters, sugeriu colocar o 'loading data' em português, visto que a nossa aplicação é para uma empresa brasileira. Todos os usuários acharam muito bom a tela informando o carregamento e não tiveram dificuldade em identificar os clusters, nem os dados. Gostaram da disposição da tela e acreditam que outros usuários não terão problemas.
- **Resultado:**  100% das pessoas que testaram a aplicação não tiveram problemas, acharam útil as informações e disposição dos componentes nas telas.


## Exemplo de teste: Filtros no cluster
**Tarefa 3:** Utilizar o filtro na tela do cluster
- **Descrição da Tarefa:** Utilizar o filtro de data e número de cluster na tela gerada pós a inserção dos arquivos
- **Expectativa:** É esperado que o usuário mexa nos filtros e identifique o que está sendo gerado.
- **Observações:** Os filtros ainda não estão implementados, então foi feito uma contextualização da página e perguntado ao usuário quais seriam os resultados dos filtros.
- **Feedback do Usuário:** Não encontraram dificuldade, acharam muito inteligente os filtros estarem localizado no header da página. 
- **Resultado:** Os usuários não tiveram dificuldade nessa etapa.


## Exemplo de teste: Realizar a otimização de um cluster
**Tarefa 4:** Utilzar o algoritmo das rotas após gerar o cluster.
- **Descrição da Tarefa:** Clicar em um cluster para que este seja otimizado.
- **Expectativa:** É esperado que o usuário consiga identificar um cluster, clicar nele e ser redirecionado para a próxima página onde está localizado a otimização de rota.
- **Observações:** --
- **Feedback do Usuário:** Um dos usuários que teve dificuldade sugeriu uma mudança em como são gerados os clusters, não sendo pontilhado, mas um círculo, o que facilita o 'pointer' do mouse.
- **Resultado:** 75% dos usuários não tiveram dificuldade em clicar no cluster e prosseguir para a próxima tela. 


## Exemplo de teste: Buscar uma rua otimizada
**Tarefa 5:** Após a geração da rota, identificar os resultados gerados na tabela e no mapa.
- **Descrição da Tarefa:** Clicando em um cluster, o usuário será redirecionado para a tela do algoritmo otimizado. O objetivo é identificar as rotas geradas e a disposição dessas rotas na tabela.
- **Expectativa:** É esperado que o usuário consiga idnetificar os dados gerados pela otimização e consiga se localizar na tela.
- **Observações:** --
- **Feedback do Usuário:** Tiveram dificuldade em identificar a coluna de cada dia de leitura da rota. o usuário Victor Gabriel Marques, achou bem fácil e objetivo a identificação de cada ponto na rota.
- **Resultado:** Todos os usuários tiveram dificuldade com a coluna que mostrava os dias de leitura, mas com o resto dos componentes da tela soube identificar e compreender os resultados.


## Exemplo de teste: Analisar o inicio da rota
**Tarefa 6:** Após gerar o cluster, identifique o ponto de partida da rota que o leiturista irá percorrer.
- **Descrição da Tarefa:** Gerando as rotas, o usuário poderá localizar o inicio da rota do leiturista.
- **Expectativa:** É esperado que o usuário consiga clicar no botão 'inicio da rota' que está no header, sem esforço.
- **Observações:** --
- **Feedback do Usuário:** Não tiveram dificuldade, pensam que a localização do botão é muito estratégica, mas recomendam que leve mais próximo ao inicio da rota. Em algumas rotas o 'inicio da rota' apenas centralizava no mapa o caminho, não identificando o ponto inicial.
- **Resultado:** Nenhum usuário obteve dificuldade em encontrar o botão.

# Pontos de atenção
&emsp;Diante do teste realizado, foram observados alguns pontos de atenção:
- Problema de usabilidade, dificuldade em identificar botão de upload do arquivo: Sendo considerado um problema com severidade alta, visto que é o inicio da aplicação e que é uma tarefa relativamente simples;
- Problema de conteúdo, falta de informações sobre como utilizar a plataforma - como roteirizar um cluster: Um problema com baixa severidade. O grupo acredita que esse erro possa ser consertado com a inserção de um card ou modal que dê uma instrução ao usuário;
- Problema de conteúdo, falta de informações sobre como utilizar a plataforma - o que significam os pontos: Um problema com baixa severidade. O grupo acredita que esse erro possa ser consertado com a inserção de um card ou modal que dê uma instrução ao usuário;
- Problema de significado, não souberam dizer o que significa a coluna 'grupo' na tela de otimização: Esse problema é algo pequeno em relação aos demais. Foi uma falta de atenção do grupo e no uso das palavras, é possível apenas trocar 'grupo' por 'dias'.

# Conclusão
&emsp;Este documento fornece uma visão detalhada do processo e dos resultados dos testes de usabilidade realizados. As informações coletadas serão fundamentais para guiar melhorias no sistema, assegurando que ele atenda às necessidades e expectativas dos usuários de maneira eficaz e intuitiva. As sugestões de mudanças, como a melhoria na identificação do botão de 'inserir arquivo' e a tradução dos avisos de carregamento, serão essenciais para aprimorar a experiência do usuário. A implementação das recomendações dos usuários contribuirá significativamente para a usabilidade e a aceitação do sistema, facilitando a interação e promovendo uma utilização mais eficiente e satisfatória.