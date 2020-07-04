'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
'''

N = int(input())
for i in range(N):
    valores = str(input()).split()
    v1 = int(valores[0])
    v2 = int(valores[1])
    v3 = [v1,v2]
    X = min(v3)
    Y = max(v3)
    impares = []
    for i in range(X+1, Y):
        if i % 2 != 0:
            impares.append(i)
    print(sum(impares))
