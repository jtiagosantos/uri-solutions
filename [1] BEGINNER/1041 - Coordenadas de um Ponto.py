'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1041.png" alt="Cartesian Plan">

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
'''

valores = str(input()).split()
x = float(valores[0])
y = float(valores[1])

if x == 0.0 and y == 0.0:
    print('Origem')
else:
    if x == 0.0 and y != 0.0:
        print('Eixo Y')
    elif x != 0.0 and y == 0.0:
        print('Eixo X')
    elif x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    elif x > 0 and y < 0:
        print('Q4')
