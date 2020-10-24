=begin
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
=end

valores = []
6.times do
    n = gets.chomp.to_f
    valores.push(n)
end

count = valores.select{|i| i > 0}.size

puts "#{count} valores positivos"