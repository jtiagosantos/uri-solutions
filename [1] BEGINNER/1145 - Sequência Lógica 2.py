'''
Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.
'''

valores = str(input()).split()
X = int(valores[0])
Y = int(valores[1])
cont = 0
for i in range(1, Y+1):
    while cont != X:
        if cont != X -1:
            print(i, end = ' ')
        else:
            print(i)
        cont += 1
        break
    if cont == X:
        cont = 0