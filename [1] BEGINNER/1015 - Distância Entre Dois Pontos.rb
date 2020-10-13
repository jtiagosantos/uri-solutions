=begin
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = <img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1015.png" alt="Distance Formula">

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
=end

p1 = gets.chomp.split.map{|i| i.to_f}
x1 = p1[0]
y1 = p1[1]
p2 = gets.chomp.split.map{|i| i.to_f}
x2 = p2[0]
y2 = p2[1]

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2.0)

puts "%.4f" % dist