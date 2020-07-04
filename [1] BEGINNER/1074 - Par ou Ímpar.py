'''
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

Entrada
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.
'''

valores = []
N = int(input())
for i in range(N):
    num = int(input())
    valores.append(num)
for i in valores:
    if i % 2 == 0 and i != 0:
        print('EVEN', end = ' ')
        if i > 0:
            print('POSITIVE')
        elif i < 0:
            print('NEGATIVE')
    if i % 2 != 0:
        print('ODD', end = ' ')
        if i > 0:
            print('POSITIVE')
        elif i < 0:
            print('NEGATIVE')
    if i == 0:
        print('NULL')
        