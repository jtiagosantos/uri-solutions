'''
A fórmula de Binet é uma forma de calcular números de Fibonacci.

https://resources.urionlinejudge.com.br/gallery/images/contests/944.png

Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

Entrada
A entrada é um número natural n (0 < n ≤ 50).

Saída
A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.
'''

from math import sqrt

n = int(input())

f1 = ((1+sqrt(5))/2)**n
f2 = ((1-sqrt(5))/2)**n

fib = (f1 - f2) / sqrt(5)

print('{:.1f}'.format(fib))
