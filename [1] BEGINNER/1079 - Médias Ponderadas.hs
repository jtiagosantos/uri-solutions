{-
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.
-}

import Text.Printf

media :: Double -> Double -> Double -> Double
media a b c = ((a*2) + (b*3) + (c*5)) / 10.0

loop 0 = return ()
loop n = do
  valores <- getLine
  let lista = words valores
  let a = lista !! 0
  let b = lista !! 1
  let c = lista !! 2
  let m = media (read(a)) (read(b)) (read(c))
  printf "%.1f\n" m
  loop (n -1)

main = do
  n <- readLn :: IO Int
  loop (n)