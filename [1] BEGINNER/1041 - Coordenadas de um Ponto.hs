{-
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1041.png" alt="Cartesian Plan">

Se o ponto estiver na origem, escreva a mensagem “Origem”.
Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
-}

quad :: Double -> Double -> String
quad x y | (x /= 0 && y == 0) = "Eixo X"
         | (x == 0 && y /= 0) = "Eixo Y"
         | (x > 0 && y > 0) = "Q1"
         | (x < 0 && y > 0) = "Q2"
         | (x < 0 && y < 0) = "Q3"
         | (x > 0 && y < 0) = "Q4"
         | otherwise = "Origem"

main = do
  valores <- getLine
  let lista = words valores
  let x = lista !! 0
  let y = lista !! 1
  let saida = quad (read(x)) (read(y))
  putStrLn saida