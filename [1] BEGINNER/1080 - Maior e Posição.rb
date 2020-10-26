=begin
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
=end

class MaiorPosicao
    
    def initialize count,max,pos
        @count = count
        @max = max
        @pos = pos
        @valores = []
    end
    
    def maior_posicao
    	for i in (1..@count)
            n = gets.chomp.to_i
            @valores.push(n)
        end
        @max = @valores.max
        @pos = @valores.index(@max)
        
        return "#{@max}\n#{@pos+1}"
    end
end

classe = MaiorPosicao.new 100,0,0
puts classe.maior_posicao