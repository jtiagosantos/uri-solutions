'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''

valores = []
pares = 0
for i in range(5):
    num = int(input())
    valores.append(num)
for i in valores:
    if i % 2 == 0:
        pares += 1
print('{} valores pares'.format(pares))
