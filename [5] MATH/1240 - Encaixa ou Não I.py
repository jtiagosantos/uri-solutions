'''
Paulinho tem em suas mãos um pequeno problema. A professora lhe pediu que ele construísse um programa para verificar, à partir de dois valores inteiros A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois inteiros A (1 ≤ A < 231 ) e B (1 ≤ B < 231) positivos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.
'''

N = int(input())
for c in range(N):
    entrada = str(input()).split()
    A = list(entrada[0])
    B = list(entrada[1])
    x = -1
    count = 0
    for i in A[::-1]:
        if abs(x) <= len(B):
            if i == B[x]:
                count += 1
        x -= 1
    if count == len(B):
        print('encaixa')
    else:
        print('nao encaixa')
        