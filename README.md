# Analise-de-Dados-do-BTC

Criei um programa em Python para análise de dados do BTC. A finalidade desse programa é permitir que os usuários realizem diversas operações de análise em um conjunto de dados do Bitcoin.

Ao executar o programa, você terá acesso a um menu inicial, onde pode selecionar as opções disponíveis. Vou explicar brevemente como o programa foi construído.

Primeiro, importei os dados do arquivo btc_usd.csv e os organizei em um dicionário, convertendo as datas para o formato "DD/MM/AAAA" e os preços para o formato "$0,00". O volume é mantido no formato original.

Em seguida, exibo o menu inicial, que apresenta uma breve descrição do programa e as opções disponíveis para você.

Dentre as opções, temos:

    1. Alterar período: permite que você selecione um novo intervalo de datas para análise.
    2. Consultar lista de dados do período: exibe os primeiros resultados correspondentes ao período selecionado.
    3. Consultar recordes de valores do período: apresenta os valores mínimos e máximos encontrados no período para cada categoria (abertura, fechamento, preço global, volume e taxa de variação).
    4. Calcular médias de valores do período: calcula as médias de cada coluna no período selecionado.

O programa também trata erros de entrada, garantindo que as datas escolhidas estejam dentro do intervalo disponível nos dados e que a data inicial seja menor que a data final.

Durante o desenvolvimento, utilizei conceitos como dicionários e tuplas para manipular os dados, funções para modularizar o código, manipulação de arquivos para importar os dados, tratamento de exceções para lidar com erros de entrada e programação funcional para realizar cálculos e formatação dos dados.


