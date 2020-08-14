'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
'''

I = [1,1,1,3,3,3,5,5,5,7,7,7,9,9,9]
J = [7,6,5,9,8,7,11,10,9,13,12,11,15,14,13]

for i,j in zip(I,J):
    print('I={} J={}'.format(i,j))
    