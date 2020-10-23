=begin
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
=end

valores = gets.chomp.split.map{|valor| valor.to_f}
a = valores[0]
b = valores[1]
c = valores[2]

if a > (b - c).abs and a < b + c
    puts "Perimetro = %.1f" % (a + b + c)
else
	area = (a + b) * c / 2.0
    puts "Area = %.1f" % area
end