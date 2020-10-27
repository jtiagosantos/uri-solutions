=begin
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
=end

class Cobaias

	def initialize n
		@n = n
		@total = @total_c = @total_r = @total_s = 0
		@perc_c = @perc_r = @perc_s = 0
	end

	def describe
		@n.times do
			entrada = gets.chomp.split
			qt = entrada[0].to_i
			animal = entrada[1]
			@total += qt
			case animal
				when "C"
					@total_c += qt
				when "R"
					@total_r += qt
				when "S"
					@total_s += qt
			end
		end

		@perc_c = (@total_c * 100.0) / @total
		@perc_r = (@total_r * 100.0) / @total
		@perc_s = (@total_s * 100.0) / @total

		puts "Total: #{@total} cobaias"
		puts "Total de coelhos: #{@total_c}"
		puts "Total de ratos: #{@total_r}"
		puts "Total de sapos: #{@total_s}"
		puts "Percentual de coelhos: %.2f %%" % @perc_c
		puts "Percentual de ratos: %.2f %%" % @perc_r
		puts "Percentual de sapos: %.2f %%" % @perc_s
	end

end

n = gets.chomp.to_i
classe = Cobaias.new n
classe.describe