=begin
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
=end

x = gets.chomp.to_i
y = gets.chomp.to_i

valores = [x,y]
count = 0

for i in (valores.min..valores.max)
    if i != valores.min and i != valores.max and i % 2 != 0
        count += i 
    end
end

puts count