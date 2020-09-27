{-
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
-}

import Text.Printf

calculo :: Double -> Double -> Double
calculo a b = a * b

main = do
valores <- getLine
let lista = words valores
let qtp1 = lista !! 1
let valorp1 = lista !! 2
valores <- getLine
let lista = words valores
let qtp2 = lista !! 1
let valorp2 = lista !! 2

let ttpeça1 = calculo (read(qtp1)) (read(valorp1))
let ttpeça2 = calculo (read(qtp2)) (read(valorp2))

let total = ttpeça1 + ttpeça2

printf "VALOR A PAGAR: R$ %.2f\n" total