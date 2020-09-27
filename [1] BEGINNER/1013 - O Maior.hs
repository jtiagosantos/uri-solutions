{-
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png" alt="Greatest Formula">


Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
-}

import Text.Printf

maior_3 :: Double -> Double -> Double -> Double
maior_3 a b c = max a (max b c)

main = do
valores <- getLine
let lista = words valores
let a = lista !! 0
let b = lista !! 1
let c = lista !! 2
let teste = maior_3 (read(a)) (read(b)) (read(c))
printf "%.f eh o maior\n" teste