=begin
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
=end

par = impar = positivo = negativo = 0

5.times do
    n = gets.chomp.to_i
    if n % 2 == 0
        par += 1
    else
        impar += 1
    end
    if n > 0
        positivo += 1
    elsif n < 0
        negativo += 1
    end
end

puts "#{par} valor(es) par(es)"
puts "#{impar} valor(es) impar(es)"
puts "#{positivo} valor(es) positivo(s)"
puts "#{negativo} valor(es) negativo(s)"