'''
Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

Entrada
A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

Saída
Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.
'''

vetor_A = []
for i in range(100):
    num = str(input())
    if '.' in num:
        vetor_A.append(float(num))
    else:
        vetor_A.append(int(num))
for i,x in enumerate(vetor_A):
    if x <= 10:
        print('A[{}] = {:.1f}'.format(i,x))