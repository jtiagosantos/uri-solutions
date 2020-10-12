=begin
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com 
mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
=end

valores = gets.chomp.split.map{|valor| valor.to_f}
a = valores[0]
b = valores[1]
c = valores[2]
area_triang = (a * c) / 2.0
area_circ = 3.14159 * c ** 2
area_trap = (a + b) * c / 2.0
area_quad = b ** 2
area_retang = a * b

puts "TRIANGULO: %.3f" % area_triang
puts "CIRCULO: %.3f" % area_circ
puts "TRAPEZIO: %.3f" % area_trap
puts "QUADRADO: %.3f" % area_quad
puts "RETANGULO: %.3f" % area_retang