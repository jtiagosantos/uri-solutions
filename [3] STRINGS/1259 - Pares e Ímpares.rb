=begin
Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

* Primeiro os Pares
* Depois os Ímpares

Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

Entrada
A primeira linha de entrada contém um único inteiro positivo N (1 < N < 105) Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

Saída
Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo abaixo.
=end

n = gets.chomp.to_i
valores = []
n.times do
     num = gets.chomp.to_i
     valores.push(num)
end

pares = valores.select{|i| i % 2 == 0}
impares = valores.select{|i| i % 2 != 0}

puts pares.sort
puts impares.sort.reverse