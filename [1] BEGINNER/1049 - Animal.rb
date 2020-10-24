=begin
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1049_b.png" alt="Animal Species Table">

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
=end
palavra1 = gets.chomp
palavra2 = gets.chomp
palavra3 = gets.chomp

case palavra1
    when "vertebrado"
        case palavra2
            when "ave"
                case palavra3
                    when "carnivoro"
                        puts "aguia"
                    when "onivoro"
                        puts "pomba"
                end
            when "mamifero"
                case palavra3
                    when "onivoro" 
                        puts "homem"
                    when "herbivoro"
                        puts "vaca"
                end
        end
    when "invertebrado"
        case palavra2
            when "inseto"
                case palavra3
                    when "hematofago"
                        puts "pulga"
                    when "herbivoro"
                        puts "lagarta"
        		end
            when "anelideo"
                case palavra3
                    when "hematofago"
                        puts "sanguessuga"
                    when "onivoro"
                        puts "minhoca"
                end
        end
end