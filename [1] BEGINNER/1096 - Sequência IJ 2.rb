class Sequencia
    
    def initialize
        @i = 1
        @j = 7
    end
    
    def sequencia
        5.times do
            puts "I=#{@i} J=#{@j}"
            puts "I=#{@i} J=#{@j-1}"
            puts "I=#{@i} J=#{@j-2}"
            @i += 2
        end
    end
end

classe = Sequencia.new
classe.sequencia