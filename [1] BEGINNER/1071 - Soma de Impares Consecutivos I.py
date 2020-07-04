'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
'''

a = int(input())
b = int(input())
X = min(a,b)
Y = max(a,b)
impares = []
for i in range(X+1, Y):
    if i % 2 != 0:
        impares.append(i)
print(sum(impares))
