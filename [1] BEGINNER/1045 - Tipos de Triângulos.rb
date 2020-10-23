=begin
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
=end

valores = gets.chomp.split.map{|valor| valor.to_f}.sort
a = valores[-1]
b = valores[-2]
c = valores[-3]

if a >= b + c
    puts "NAO FORMA TRIANGULO"
else
	if (a ** 2) == (b ** 2) + (c ** 2)
	    puts "TRIANGULO RETANGULO"
	end
	if (a ** 2) > (b ** 2) + (c ** 2)
	    puts "TRIANGULO OBTUSANGULO"
	end
	if (a ** 2) < (b ** 2) + (c ** 2)
	    puts "TRIANGULO ACUTANGULO"
	end
	if a == b and b == c
	    puts "TRIANGULO EQUILATERO"
	end
	if (a == b and b != c) or (a == c and c != b) or (b === c and c != a)
	    puts "TRIANGULO ISOSCELES"
	end
end