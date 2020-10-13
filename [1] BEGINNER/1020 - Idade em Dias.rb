=begin
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
=end

idade = gets.chomp.to_i
ano = mes = dia = 0

while idade >= 365
    idade -= 365
    ano += 1
end

while idade >= 30
    idade -= 30
    mes += 1
end

dia = idade

puts "#{ano} ano(s)\n#{mes} mes(es)\n#{dia} dia(s)"