{-
Um número natural é um inteiro não-negativo (0, 1, 2, 3, 4, 5,...). A sua tarefa neste problema é calcular a soma dos números 
naturais que estão presentes em um determinado intervalo [A, B] inclusive.
Por exemplo, a soma dos números naturais no intervalo [2, 5] é 14 = (2+3+4+5).

Entrada
Cada caso de teste contém dois inteiros A e B (1 ≤ A ≤ B ≤ 10^9), representando o limite inferior e o superior respectivamente.

Saída
Para cada caso de teste, a saída consiste de uma linha contendo a soma dos números naturais do intervalo.
-}

import Text.Printf

soma :: Double -> Double -> Double
soma a1 an = ((a1+an) * ((an-a1)+1))/2

main = do
  valores <- getLine
  let lista = words valores
  let a1 = lista !! 0
  let an = lista !! 1
  let saida = soma (read(a1)) (read(an))
  printf "%.f\n" saida