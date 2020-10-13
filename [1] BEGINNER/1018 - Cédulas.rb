=begin
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
=end

cem = cinquenta = vinte = dez = cinco = dois = um = 0

valor = gets.chomp.to_i
valor_copy = valor

while valor >= 100
	valor -= 100
	cem += 1
end

while valor >= 50
	valor -= 50
	cinquenta =+ 1
end

while valor >= 20
	valor -= 20
	vinte =+ 1
end

while valor >= 10
	valor -= 10
	dez =+ 1
end

while valor >= 5
	valor -= 5
	cinco =+ 1
end

while valor >= 2
	valor -= 2
	dois =+ 1
end

um = valor

puts valor_copy
puts "#{cem} nota(s) de R$ 100,00"
puts "#{cinquenta} nota(s) de R$ 50,00"
puts "#{vinte} nota(s) de R$ 20,00"
puts "#{dez} nota(s) de R$ 10,00"
puts "#{cinco} nota(s) de R$ 5,00"
puts "#{dois} nota(s) de R$ 2,00"
puts "#{um} nota(s) de R$ 1,00"