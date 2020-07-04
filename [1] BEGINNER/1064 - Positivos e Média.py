'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''

valores = []
positivos = []
positivo = 0
for i in range(6):
    num = str(input())
    if '.' in num:
        valores.append(float(num))
    else:
        valores.append(int(num))
for i in valores:
    if i > 0:
        positivo += 1
        positivos.append(i)
print('{} valores positivos'.format(positivo))
print('{:.1f}'.format(sum(positivos)/len(positivos)))
