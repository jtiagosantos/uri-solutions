=begin
O prédio do Departamento de Ilhas Naturais Federais (DINF) está passando por uma reforma para deixá-lo mais acessível. No prédio há uma escada de N degraus. Cada degrau tem H centímetros de altura, C centímetros de comprimento e L centímetros de largura. A figura (a) exemplifica uma escada com N=4 degraus.

https://www.urionlinejudge.com.br/gallery/images/problems/UOJ_2518.png

Para tornar o prédio mais acessível, o chefe do DINF decidiu colocar uma rampa sobre a escada. A rampa é rígida e tem forma retangular. Ela será colocada sobre a escada de forma a cobrir todos os seus degraus, como indicado pela figura (b).
Sua tarefa é, dado o número de degraus e suas medidas, determinar qual deve ser área total da superfície da rampa.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 1000), o número de degraus na escada. A segunda linha contém três inteiros H, C e L (1 ≤ H, C, L ≤ 100), as medidas de cada degrau, em centímetros.
A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma linha contendo a área total da superfície da rampa, em metros quadrados. Arredonde e imprima este valor com exatamente 4 casas decimais.
=end

class AreaRampa

	def initialize valores
		@h = valores[0]
		@c = valores[1]
		@l = valores[2]
		@n = valores[3]
	end

	def calcula_area
		area = ((@c ** 2 + @h ** 2) ** (1/2.0)) * @l * @n
		return "%.4f" % (area / 10000.0)
	end

end

while num_deg = gets
	num_deg = num_deg.to_i
	valores = gets.chomp.split.map{|valor| valor.to_i}.push(num_deg)
	area = AreaRampa.new valores
	puts area.calcula_area
end