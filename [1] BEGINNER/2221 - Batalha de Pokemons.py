'''
Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de duelo é simples, cada treinador coloca um Pomekon na batalha e vence quem tem o Pomekon com maior valor de golpe, que é definido da seguinte maneira:


O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.

Neste problema será dado a você o valor do bônus aplicado, os valores de ataque e defesa do Pomekon de Dabriel e Guarte e seus respectivos níveis, cabe a você informar o ganhador da batalha.

Entrada
A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T indicando o número de instâncias. Cada instância começa com um inteiro B (0 ≤ B ≤ 100), que indica o valor do bônus aplicado. Nas duas linhas seguintes terão três inteiros Ai, Di e Li (1 ≤ Ai, Di ≤ 100, 1 ≤ Li ≤ 50), representado o valor de ataque do Pomekon, o valor de defesa e o level do treinador. A primeira linha representa o Pomekon de Dabriel e a segunda o de Guarte.

Saída
Para instância na entrada você deverá imprimir o nome do treinador que irá vencer a batalha, em caso de empate imprima: "Empate", sem aspas.
'''

T = int(input())
for i in range(T):
    bonus = int(input())
    #Pokemon de Dabriel:
    entrada_1 = str(input()).split()
    atk = int(entrada_1[0])
    defesa = int(entrada_1[1])
    nivel = int(entrada_1[2])
    valor_golpe1 = (atk + defesa) / 2
    if nivel % 2 == 0:
        valor_golpe1 += bonus
    #Pokemon de Guarte:
    entrada_2 = str(input()).split()
    atk = int(entrada_2[0])
    defesa = int(entrada_2[1])
    nivel = int(entrada_2[2])
    valor_golpe2 = (atk + defesa) / 2
    if nivel % 2 == 0:
        valor_golpe2 += bonus
    
    if valor_golpe1 > valor_golpe2:
        print('Dabriel')
    elif valor_golpe2 > valor_golpe1:
        print('Guarte')
    else:
        print('Empate')
        