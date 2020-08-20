'''
Nick é um cientista que viaja por diversos universos paralelos, juntamente com o seu neto, Mory. Em um desses universos, havia um programa de televisão, que premiava quem adivinhasse as alturas máximas de arremessos de frutas. Neste local, a massa da fruta não influenciava na altura máxima do arremesso. Nick calculava o ângulo do arremesso, que formava sempre uma parábola, e extraía uma função de segundo grau da trajetória. Ajude Nick e Mory a ganhar muitos prêmios neste programa.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro T (2 <= T <= 99) relativo ao número de casos de teste. As T linhas seguintes possuem três valores inteiros A (A < 0), B e C (-100 <= B, C <= 100), representando os coeficientes de uma função de segundo grau, na forma ax2 + bx + c.

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número real, com aproximação de duas casas decimais, a altura máxima do arremesso de uma fruta.
'''

num_casos = int(input())
for _ in range(num_casos):
    valores = str(input()).split()
    a = int(valores[0])
    b = int(valores[1])
    c = int(valores[2])
    delta = (b**2) - 4 * a * c
    alt_max = -delta / (4*a)
    print('{:.2f}'.format(alt_max))