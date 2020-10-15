=begin
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
=end

n = gets.chomp.to_f
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
puts "NOTAS:"
notas.each do |i|
	qt_notas = (n/i).to_i
	puts "#{qt_notas} nota(s) de R$ %.2f" % i
	n -= qt_notas * i
end
puts "MOEDAS:"
moedas.each do |i|
	qt_moedas = (n.round(2)/i).to_i
	puts "#{qt_moedas} moeda(s) de R$ %.2f" % i
	n -= qt_moedas * i
end