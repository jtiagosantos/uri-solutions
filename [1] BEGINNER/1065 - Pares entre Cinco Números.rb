=begin
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
=end

count = 0
5.times do
    n = gets.chomp.to_i
    if n % 2 == 0
        count += 1 
    end
end

puts "#{count} valores pares"