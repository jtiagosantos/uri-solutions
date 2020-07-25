'''
O problema é simples. Dada uma string x e 5 outras strings, encontre a string com o menor valor de distância de edição com relação a x. Se o valor da distância de edição for maior do que k, imprima -1.

Entrada
A primeira linha contém uma string x ( 1 ≤ len(x) ). A próxima linha contém um inteiro k ( 1 ≤ k ≤ 100 ). Cada uma das próximas 5 linhas contém uma string y ( len(y) ≤ 100000).

Saída
Imprima o índice da string mais próxima da primeira linha. Se este valor for diferente de -1, imprima o valor de distância de edição da segunda linha.
'''

values = []

def controller(x, string):
    global count
    count = 0
    for a,b in zip(x, string):
        if a == b:
            count += 1
    values.append(count)

while True:
    try:
        x = list(str(input()))
        k = int(input())
        for c in range(5):
            string = list(str(input()))
            controller(x, string)

        cont = 0
        pos_maior = values.index(max(values))
        for v in values:
            if v >= k:
                cont += 1

        if cont > 0:
            print(pos_maior+1)
            print(len(x) - max(values))
        else:
            print(-1)
        values = []
    except EOFError:
        break

