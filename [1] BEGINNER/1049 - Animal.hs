{-
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1049_b.png" alt="Animal Species Table">

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
-}

classificacao :: String -> String -> String -> String
classificacao x y z | (x == "vertebrado" && y == "ave" && z == "carnivoro") = "aguia"
                    | (x == "vertebrado" && y == "ave" && z == "onivoro") = "pomba"
                    | (x == "vertebrado" && y == "mamifero" && z == "onivoro") = "homem"
                    | (x == "vertebrado" && y == "mamifero" && z == "herbivoro") = "vaca"
                    | (x == "invertebrado" && y == "inseto" && z == "hematofago") = "pulga"
                    | (x == "invertebrado" && y == "inseto" && z == "herbivoro") = "lagarta"
                    | (x == "invertebrado" && y == "anelideo" && z == "hematofago") = "sanguessuga"
                    | otherwise = "minhoca"

main = do
  p1 <- getLine
  p2 <- getLine
  p3 <- getLine
  let saida = classificacao p1 p2 p3
  putStrLn saida