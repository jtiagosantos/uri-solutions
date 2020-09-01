'''
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a
 matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. 
O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem 
ser formatados em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos
do maior número da matriz. Após o último caractere de cada linha da matriz não deve haver espaços em branco. 
Após a impressão de cada matriz deve ser deixada uma linha em branco.
'''

while True:
    matriz = []; c = i = 0
    num = int(input())
    if num == 0:
        break
    for _ in range(num):
        linha = []
        for _ in range(num):
            linha.append(2 ** c)
            c += 1
        matriz.append(linha)
        i += 1; c = i

    esp = len(str(matriz[-1][-1]))

    for linha in matriz:
        for i in linha[:-1]:
            print(f'{str(i).rjust(esp)}', end = ' ')
        print(f'{str(linha[-1]).rjust(esp)}')
    print()