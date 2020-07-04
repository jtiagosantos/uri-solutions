'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

valores = []
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
print('{} valores positivos'.format(positivo))