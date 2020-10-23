=begin
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1038_en.png" alt="Price Table">

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
=end

entrada = gets.chomp.split.map{|i| i.to_i}
cod = entrada[0]
qt = entrada[1]
total = 0

case cod
    when 1
        total = qt * 4.00
    when 2
        total = qt * 4.50
    when 3
        total = qt * 5.00
    when 4
        total = qt * 2.00
    when 5
        total = qt * 1.50
end

puts "Total: R$ %.2f" % total