{-
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
-}

import Text.Printf

main = do
a <- readLn :: IO Int 
b <- readLn :: IO Int
let lista = a:b:[]
let max_lista = maximum lista
let min_lista = minimum lista
let lista' = [i | i <- [min_lista..max_lista], rem i 2 /= 0 , i /= min_lista, i /= max_lista]
let soma = sum lista'

printf "%d\n" soma