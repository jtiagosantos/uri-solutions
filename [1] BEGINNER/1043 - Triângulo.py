'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''

valores = str(input()).split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

#Condição para a existência de um triângulo:
if A < B + C and B < A + C and C < A + B:
    perimetro = A + B + C
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area_trapezio = ((A + B) * C) / 2
    print('Area = {:.1f}'.format(area_trapezio))
