=begin
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
=end

segundo = gets.chomp.to_i
hora = min = seg = 0

while segundo >= 3600
    segundo -= 3600
    hora += 1
end

while segundo >= 60
    segundo -= 60
    min += 1
end

seg = segundo
    
puts "#{hora}:#{min}:#{seg}"