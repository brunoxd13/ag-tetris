# ag-tetris

## Resumo
Neste projeto é aplicado a implementação de um algorítmo genético para obter uma forma de executar o jogo tetris, a fim de conseguir maior pontuação e resolução do jogo. Desenvolvido na linguagem de programação Python 3, em conjunto com a biblioteca  pygame. Além disso utilizada biblioteca matplotlib, para gerar relatórios gráficos evidenciando a evolução do indivíduo com melhor fitness e a média de fitness de todos os indivíduos por geração.

## Introdução
Algoritmos Genéticos, AGs, são métodos de otimização e busca inspirados nos mecanismos de evolução de populações de seres vivos. Neste, populações de indivíduos que sofrem mudanças geracionais, procriam-se, sofrem mutações e no fim as melhores características de indivíduos se destacam nas gerações posteriores.

Este conceito foi aplicado na resolução do jogo Tetris, que consiste em montar um quebra-cabeça encaixando peças de diferentes formatos capazes de girar sobre o próprio eixo em quatro posições diferentes. Cada execução do jogo é considerado um indivíduo a ser analisado pelo algoritimo genético.

## Algoritmo Genético
Para modelar o problema de acordo com o algoritmo, foi necessário entender como calcular a melhor posição da peça para ser posicionada no tetris. Esta é identificada testando todas as possíveis posições da peça e identificando qual é o melhor enquadramento. Com base nisso, foram definidos sete atributos em relação a posição em que a peça será colocada: 
  * Altura total;
  * Número de linhas completas;
  * Buracos formados;
  * Tampas formadas;
  * Lados em contato pecas;
  * Lados em contato com chão; e
  * Lados em contato com parede.
  
Como no jogo tetris a ordem das peças é aleatoria, foi necessario definir uma forma de normalização, para que a solução funcione idependente da ordem de execução das peças. Este problema foi solucionado multiplicando os sete atributos citados anteriomente por sete pesos aleatórios definidos na criação da primeira geração de indivíduos. O resultado desta multiplicação retorna a pontuação de cada indivíduo. Desta forma o objetivo do algoritmo se tornou encontrar os melhores pesos, que funcionem com maior precisão nos mais varidadas execuções do tetris.

Com base na pontuação de cada indivíduo, o algoritmo seleciona os melhores indivíduos, para fazer o cruzamento entre os mesmos e criar a nova geração. Após fazer a seleção dos melhores indivíduos o algoritmo aplica o crossover, a taxa de mutação e o elitismo definidos na inicialização.

O modo de geração do crossover é aleatório, o algoritmo percorre verifica os sete pesos dos indivíduos e gera um número aleatório, se este número for menor do que o número de crossover definido pelo usuário, os pesos dos dois cromossomos são trocados.

Para fazer a mutação o algoritmo percorre todos os sete pesos do indivíduo e gerando um número randômico, caso este número seja menor que a taxa de mutação definida pelo usuário, o peso é substituído randomicamente.

O conceito de elitismo diz que os n melhores idividuos deve ser repassados para a geração seguinte. Neste caso o usuario deve definir este número de individuos na inicialização do programa.

O algoritmo está divido em quatro arquivos, main.py, algoritmoGenetico.py, jogo.py e tetris.py, e as funções de geração, seleção, reprodução e mutação podem ser observadas no arquivo algoritmoGenetico.py
