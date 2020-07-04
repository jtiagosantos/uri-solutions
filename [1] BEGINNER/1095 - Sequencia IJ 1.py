'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
'''

I = 1
J = 60
while True:
    print('I={} J={}'.format(I,J))
    I += 3
    J -= 5
    if J == 0:
        print('I={} J={}'.format(I,J))
        break