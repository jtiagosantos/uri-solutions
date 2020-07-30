'''
Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

Entrada
Uma linha contendo um número  0 < X < 107.

Saída
Uma linha contendo a resposta do problema.
'''

X = int(input())
if X % 2 == 0:
    print(X + 2)
else:
    print(X + 1)