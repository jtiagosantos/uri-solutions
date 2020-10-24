=begin
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salary	  Readjustment Rate
0 - 400.00				15%
400.01 - 800.00			12%
800.01 - 1200.00		10%
1200.01 - 2000.00		 7%
Above 2000.00			 4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
=end

salario = gets.chomp.to_f

novo_salario = 0
reajuste = 0
percentual = ""

if salario >= 0 and salario <= 400
    novo_salario = (salario * 0.15) + salario
    reajuste = novo_salario - salario
    percentual = "15 %"
elsif salario > 400 and salario <= 800
    novo_salario = (salario * 0.12) + salario
    reajuste = novo_salario - salario
    percentual = "12 %"
elsif salario > 800 and salario <= 1200
    novo_salario = (salario * 0.10) + salario
    reajuste = novo_salario - salario
    percentual = "10 %"
elsif salario > 1200 and salario <= 2000
    novo_salario = (salario * 0.07) + salario
    reajuste = novo_salario - salario
    percentual = "7 %"
elsif salario > 2000
    novo_salario = (salario * 0.04) + salario
    reajuste = novo_salario -salario
    percentual = "4 %"
end

puts "Novo salario: %.2f" % novo_salario
puts "Reajuste ganho: %.2f" % reajuste
puts "Em percentual: #{percentual}"