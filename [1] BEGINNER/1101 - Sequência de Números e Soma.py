'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
'''

while True:
    valores = str(input()).split()
    valores_lista = []
    M = int(valores[0])
    N = int(valores[1])
    if M <= 0 or N <= 0:
        break
    else:
        for i in range(min(M,N), max(M,N)+1):
            valores_lista.append(i)
        for i in sorted(valores_lista):
            print(i, end = ' ')
        print('Sum={}'.format(sum(valores_lista)))
        