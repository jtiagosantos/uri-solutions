=begin
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
=end

valores = []
6.times do
    n = gets.chomp.to_f
    valores.push(n)
end

positivos = valores.select{|i| i > 0}
media = (positivos.inject(:+)) / (positivos.size)

puts "#{positivos.size} valores positivos"
puts "%.1f" % media