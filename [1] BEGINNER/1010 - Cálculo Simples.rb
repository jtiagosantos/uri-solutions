=begin
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
=end

peça_1 = gets.chomp.split.map{|valor| valor.to_f}
peça_2 = gets.chomp.split.map{|valor| valor.to_f}

tt_peça_1 = peça_1[1] * peça_1[2]
tt_peça_2 = peça_2[1] * peça_2[2]

total_peças = tt_peça_1 + tt_peça_2

puts "VALOR A PAGAR: R$ %.2f" % total_peças