=begin
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
=end

class Sequencia
    
    def initialize i,j
        @i = i
        @j = j
    end
    
    def sequencia
        while @j >= 0
            puts "I=#{@i} J=#{@j}"
            @i += 3
            @j -= 5
        end
    end
    
end

classe = Sequencia.new 1,60
classe.sequencia