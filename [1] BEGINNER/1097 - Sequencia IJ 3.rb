=begin
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
=end

i = 1
j = [7,9,11,13,15]
for v in (0..4)
    puts "I=#{i} J=#{j[v]}"
    puts "I=#{i} J=#{j[v]-1}"
    puts "I=#{i} J=#{j[v]-2}"
    
    i += 2
end