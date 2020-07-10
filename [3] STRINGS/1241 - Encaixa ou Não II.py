'''
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

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
        