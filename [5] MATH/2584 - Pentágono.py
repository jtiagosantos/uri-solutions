'''
É possível calcular a área de um pentágono regular, ou seja, uma figura geométrica com cinco lados iguais, dado o comprimento de um dos lados. Sendo assim, calcule.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2584.png

Escreva um programa que, dado o comprimento de um lado de um pentágono regular, calcule a sua área.

Entrada
Haverá um valor C que indica a quantidade de casos de teste. Em seguida, haverá um número inteiro N para cada caso (1 ≤ N ≤ 10000), indicando o comprimento do lado de um pentágono regular.

Saída
Para cada caso de teste, imprima o valor correspondente da área do respectivo pentágono, com três casas decimais de precisão.
'''

import math

N = int(input())
for _ in range(N):
    n = int(input())
    num = 5 * (n ** 2)
    den = 4 * (math.tan(math.radians(36)))
    area = num / den
    print('{:.3f}'.format(area))