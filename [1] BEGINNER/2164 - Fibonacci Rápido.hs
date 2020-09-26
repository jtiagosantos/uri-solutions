{-
A fórmula de Binet é uma forma de calcular números de Fibonacci.

https://resources.urionlinejudge.com.br/gallery/images/contests/944.png

Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

Entrada
A entrada é um número natural n (0 < n ≤ 50).

Saída
A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.
-}

import Text.Printf

fibonacci :: Int -> Double
fibonacci n = (((0.5+sqrt(5)/2)^n) - ((0.5-sqrt(5)/2)^n)) / sqrt(5)

main = do
  n <- readLn :: IO Int
  let saida = fibonacci (n)
  printf "%.1f\n" saida
  