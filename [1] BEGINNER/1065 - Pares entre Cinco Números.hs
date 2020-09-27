{-
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
-}

import Text.Printf

main = do
a <- readLn
b <- readLn
c <- readLn
d <- readLn
e <- readLn
let lista = [i | i <- [a,b,c,d,e], rem i 2 == 0]
let tamanho = length (lista)

printf "%d valores pares\n" tamanho