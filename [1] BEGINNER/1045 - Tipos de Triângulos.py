'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''

valores = str(input()).split()
for k,v in enumerate(valores):
    valores[k] = float(v)
A = max(valores)
valores.remove(max(valores))
B = valores[0]
C = valores[1]

while True:
    if A >= B + C:
        print('NAO FORMA TRIANGULO')
        break
    else:
        if A**2 == B**2 + C**2:
            print('TRIANGULO RETANGULO')
        if A**2 > B**2 + C**2:
            print('TRIANGULO OBTUSANGULO')
        if A**2 < B**2 + C**2:
            print('TRIANGULO ACUTANGULO')
        if A == B == C:
            print('TRIANGULO EQUILATERO')
        if A == B and A != C or B == C and B != A or C == A and C != B:
            print('TRIANGULO ISOSCELES')
        break