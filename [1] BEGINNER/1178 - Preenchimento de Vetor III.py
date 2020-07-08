'''
Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.

Entrada
A entrada contem um valor de dupla precisão com 4 casas decimais.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.
'''

X = float(input())
vetor_N = []
for i in range(100):
    vetor_N.append(X)
    X = X / 2
for i,Y in enumerate(vetor_N):
    print('N[{}] = {:.4f}'.format(i, Y))