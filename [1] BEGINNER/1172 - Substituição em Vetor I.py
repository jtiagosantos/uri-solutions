'''
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
'''

X = []
for i in range(10):
    X.append(int(input()))
for k,v in enumerate(X):
    if v <= 0:
        X[k] = 1
for k,v in enumerate(X):
    print('X[{}] = {}'.format(k,v))