'''
O professor Genesio recebeu várias camisetas da OBI (Organização dos Bacharéis Intelectuais) para doar a seus alunos de Ciência da Computação. Para fazer a distribuição destas camisetas ele organizou os alunos de cada turma do curso em pequenos grupos (de no máximo 10 pessoas) e definiu que faria o sorteio de uma camiseta para cada um dos grupos. Como Genesio não quer perder muito tempo com este sorteio, ele pediu que você o ajudasse com um programa que determinasse quem foi o aluno ganhador de acordo com a seguinte regra: O primeiro de cada grupo a acertar um número escolhido pelo professor obviamente ganha a camiseta, mas se ninguém acertar este número, ganha a camiseta o primeiro que chegar o mais próximo deste número.

Não faz diferença quem do grupo o professor escolhe para tentar iniciar a adivinhação. Este sempre será o aluno número 1, e assim sucessivamente.

Entrada
A primeira linha de entrada contém um inteiro N que determina a quantidade de casos de teste, ou de camisetas que serão sorteadas. Cada caso de teste é composto por duas linhas. A primeira linha contém dois valores inteiros QT (4 ≤ QT ≤ 10) e S (1 ≤ S ≤ 100) separados por um espaço, que indicam respectivamente a quantidade de alunos do grupo e o número secreto que deve ser adivinhado. A segunda linha contém cada um dos QT valores, separados por um espaço.

Saída
Para cada caso de teste, seu programa deve imprimir um número inteiro que indica a posição do ganhador da camiseta, conforme as regras descritas acima.
'''

N = int(input())
for n in range(N):
    entrada = str(input()).split()
    num_sorteio = int(entrada[1])
    valores = str(input()).split()
    for k, v in enumerate(valores):
        valores[k] = int(v)
    ganhador = 0
    ganhou = []
    diferencas = []
    for x, y in enumerate(valores):
        if y == num_sorteio:
            ganhou.append(y)
            ganhador += 1
    if ganhador > 0:
        print(valores.index(ganhou[0])+1)
    else:
        for i in valores:
            diferencas.append(abs(num_sorteio - i))
        menor_dif = min(diferencas)
        pos_menor_dif = diferencas.index(menor_dif)
        print(pos_menor_dif+1)
