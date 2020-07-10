'''
Dados dois números inteiros, n e m, quantos dígitos tem nm ?

Exemplos:

2 e 10 - 2^10 = 1024 - 4 dígitos

3 e 9 - 3^9 = 19683 - 5 dígitos

Entrada
A entrada é composta por vários casos de teste. A primeira linha tem um número inteiro C, representando a quantidade de casos de teste. As C linhas seguintes contém dois números inteiros N e M (1 <= N, M <= 100).

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número inteiro contendo a quantidade de dígitos do resultado da potência calculada no respectivo caso de teste.
'''

C = int(input())
for i in range(C):
    valores = str(input()).split()
    n = int(valores[0])
    m = int(valores[1])
    pot = n ** m
    print(len(str(pot)))
    
    