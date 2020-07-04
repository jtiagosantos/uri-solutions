'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''

valores = []
par = impar = pos = neg = 0
for i in range(5):
    num = int(input())
    valores.append(num)
for i in valores:
    if i % 2 == 0:
        par += 1
    if i % 2 != 0:
        impar += 1
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
