'''
Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno, 
isóceles ou equilátero e se trata-se de um triângulo retângulo ou não.

Entrada
A entrada consiste em três números inteiros A,B e C (0 < A,B,C < 105).

Saída
A saída deve conter a string "Invalido" se os valores lidos não formarem um triângulo. Se os valores formarem um 
triângulo a saída deve ser "Valido-Equilatero", "Valido-Escaleno" ou "Valido-Isoceles" de acordo com a característica 
do triângulo seguido de "Retangulo: S" se o triângulo for retângulo ou "Retangulo: N" se não for, conforme os exemplos.
'''

valores = str(input()).split()
valores = sorted([int(i) for i in valores], reverse=True)
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if a >= b + c:
    print('Invalido')
else:
    if a == b == c:
        print('Valido-Equilatero\nRetangulo: N')
    elif a != b and b != c and c != a:
        print('Valido-Escaleno')
        if a == int(((b ** 2) + (c ** 2)) ** (1/2)):
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print('Valido-Isoceles\nRetangulo: N')
        