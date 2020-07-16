'''
João e Maria são amigos desde que se conheceram na creche. Desde então, eles compartilham uma rotina de brincadeiras: todas as vezes que eles se encontram, eles jogam Cara ou Coroa com uma moeda, e quem ganhar tem o privilégio de decidir quais brincadeiras eles irão jogar durante o dia. Maria sempre escolhe cara, e João sempre escolhe coroa.

Hoje em dia eles estão na faculdade, mas continuam sendo bons amigos. Sempre que se encontram, eles ainda jogam Cara ou Coroa, e o vencedor decide que filme assistir, ou em que restaurante jantar, e assim por diante.

Ontem Maria contou a João que ela guarda um registro de todas as vezes que eles jogaram, desde os tempos da creche. João ficou espantado. Porém João está estudando Ciência da Computação e decidiu que essa era uma boa oportunidade para mostrar a Maria suas habilidades em programação, escrevendo um programa que mostrasse o número de vezes que cada um deles venceu ao longo de todos esses anos.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um único inteiro N indicando o número de vezes jogadas (1 ≤ N ≤ 10000). A linha seguinte contém N inteiros Ri, separados por um espaço, descrevendo a lista de resultados. Se Ri = 0 então Maria venceu o iésimo jogo, se Ri = 1 então João venceu o iésimo jogo (1 ≤ i ≤ N). O fim da entrada é indicado por N = 0.

Saída
Para cada caso de teste na entrada, seu programa deverá escrever uma linha contendo a sentença "Mary won X times and John won Y times" ("Maria venceu X vezes e Joao venceu Y vezes"), onde 0 ≤ X e 0 ≤ Y.
'''

while True:
    N = int(input())
    if N == 0:
        break
    resultados = str(input()).split()
    count_joao = count_maria = 0
    for r in resultados:
        if r == '0':
            count_maria += 1
        if r == '1':
            count_joao += 1
    print('Mary won {} times and John won {} times'.format(count_maria, count_joao))
    
    