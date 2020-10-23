=begin
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1041.png" alt="Cartesian Plan">

Se o ponto estiver na origem, escreva a mensagem “Origem”.
Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
=end

coord = gets.chomp.split.map{|i| i.to_f}
x = coord[0]
y = coord[1]

if x > 0 and y > 0
    puts "Q1"
elsif x < 0 and y > 0
    puts "Q2"
elsif x < 0 and y < 0
    puts "Q3"
elsif x > 0 and y < 0 
    puts "Q4"
elsif x == 0 and y != 0
    puts "Eixo Y"
elsif x != 0 and y == 0
    puts "Eixo X"
else
    puts "Origem"
end