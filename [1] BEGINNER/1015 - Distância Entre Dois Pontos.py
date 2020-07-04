'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = <img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1015.png" alt="Distance Formula">

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''

#Para o ponto 1:
p1 = str(input()).split()
x1 = float(p1[0])
y1 = float(p1[1])

#Para o ponto 2:
p2 = str(input()).split()
x2 = float(p2[0])
y2 = float(p2[1])

d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print('{:.4f}'.format(d))
