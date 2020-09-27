{-
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
-}

import Text.Printf

tamanho lista = length lista

main = do
a <- readLn :: IO Double
b <- readLn :: IO Double
c <- readLn :: IO Double
d <- readLn :: IO Double
e <- readLn :: IO Double
f <- readLn :: IO Double
let lista = a : b : c : d: e: f: []
let lista' = [i | i <- lista, i >= 0]
let tam = tamanho lista'
printf "%d valores positivos\n" tam