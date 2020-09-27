{-
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
-}

import Text.Printf

main = do
a <- readLn :: IO Int
b <- readLn :: IO Int
c <- readLn :: IO Int
d <- readLn :: IO Int
e <- readLn :: IO Int
let lista = a:b:c:d:e:[]
let pares = length ([i | i <- lista, rem i 2 == 0])
let impares = length ([i | i <- lista, rem i 2 /= 0])
let positivos = length ([i | i <- lista, i > 0])
let negativos = length ([i | i <- lista, i < 0])

printf "%d valor(es) par(es)\n" pares
printf "%d valor(es) impar(es)\n" impares
printf "%d valor(es) positivo(s)\n" positivos
printf "%d valor(es) negativo(s)\n" negativos