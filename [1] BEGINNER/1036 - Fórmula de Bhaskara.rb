=begin
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as 
raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o 
resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o 
final de linha após cada mensagem.
=end

def calcula_raiz a,b,c
    delta = (b ** 2) - 4 * a * c
    if delta < 0 or a == 0
       puts "Impossivel calcular"
    else
        raiz_delta = Math.sqrt(delta)
        r1 = (-b + raiz_delta) / (2.0 * a)
        r2 = (-b - raiz_delta) / (2.0 * a)

        puts "R1 = %.5f" % r1
        puts "R2 = %.5f" % r2
    end
end

valores = gets.chomp.split.map{|valor| valor.to_f}
a = valores[0]
b = valores[1]
c = valores[2]

calcula_raiz a,b,c