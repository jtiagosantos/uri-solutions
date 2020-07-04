'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo
'''

I = 1
J = 7

while I <= 9:
    print('I={} J={}'.format(I, J))
    J -= 1
    if J == 5:
        print('I={} J={}'.format(I, J))
        J = 7
        I += 2
    