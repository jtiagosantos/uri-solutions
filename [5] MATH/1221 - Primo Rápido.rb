=begin
Mariazinha sabe que um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7 sem que haja resto. 
Então ela pediu para você fazer um programa que aceite diversos valores e diga se cada um destes valores é primo ou não. Acontece que a paciência não é uma das virtudes de Mariazinha, portanto ela quer que a execução 
de todos os casos de teste que ela selecionar (instâncias) aconteçam no tempo máximo de um segundo, pois ela odeia esperar.

Entrada
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 200), correspondente ao número de casos de teste. Seguem N linhas, cada uma contendo um valor inteiro X (1 < X < 231) que pode ser ou não, um número primo.

Saída
Para cada caso de teste imprima a mensagem “Prime” (Primo) ou “Not Prime” (Não Primo), de acordo com o exemplo abaixo.
=end

n = gets.chomp.to_i
n.times do
    num = gets.chomp.to_i
    num_piso = Math.sqrt(num).to_i
    div = 0
    i = 1
    while i <= num_piso
    	if num % i == 0
    		div += 1
    		if div == 2
    			break
    		end
    	end
    	i += 1
    end
    
    if div == 1
        puts "Prime"
    else
        puts "Not Prime"
    end
end