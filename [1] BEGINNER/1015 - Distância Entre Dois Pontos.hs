{-
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = <img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1015.png" alt="Distance Formula">

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
-}

import Text.Printf

distancia :: Double -> Double -> Double -> Double -> Double
distancia a b c d = (((a - b) ** 2) + ((c - d) ** 2)) ** (1/2)

main = do
valores <- getLine
let lista = words valores
let x1 = lista !! 0
let y1 = lista !! 1
valores <- getLine
let lista = words valores
let x2 = lista !! 0
let y2 = lista !! 1
let d = distancia (read(x2)) (read(x1)) (read(y2)) (read(y1))

printf "%.4f\n" d