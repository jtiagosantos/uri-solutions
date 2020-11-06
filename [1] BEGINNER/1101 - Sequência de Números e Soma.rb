=begin
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
=end

loop do
    valores = gets.chomp.split.map{|i| i.to_i}
    m = valores[0]
    n = valores[1]
    break if m <= 0 or n <= 0
    i = [m,n]
    lista = (i.min..i.max).map{|i| i}
    soma_lista = lista.inject(:+)
    puts "#{lista.join(' ')} Sum=#{soma_lista}"
end