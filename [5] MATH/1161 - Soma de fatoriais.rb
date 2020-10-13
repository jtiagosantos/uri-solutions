=begin
Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.

Entrada
O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 ≤ M ≤ 20) e N (0 ≤ N ≤ 20). O fim da entrada é determinado por eof.

Saída
Para cada caso de teste de entrada, seu programa deve imprimir uma única linha, contendo um número que é a soma de ambos os fatoriais (de M e N).
=end

def fatorial n
	resultado = 1
	while n >= 2
		resultado *= n
		n -= 1
	end
	return resultado
end


while valores = gets
	valores = valores.chomp.split.map {|valor| valor.to_i}
    m = valores[0]
    n = valores[1]
    fact_1 = fatorial m
    fact_2 = fatorial n
    soma = fact_1 + fact_2
    puts "#{soma}"
end