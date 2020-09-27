{-
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1038_en.png" alt="Price Table">

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
-}

import Text.Printf

conta :: Double -> Double -> Double
conta a b = if a == 1 then b * 4.00
else if a == 2 then b * 4.50
else if a == 3 then b * 5.00
else if a == 4 then b * 2.00
else b * 1.50

main = do
valores <- getLine
let lista = words valores
let cod = lista !! 0
let qt = lista !! 1
let total = conta (read(cod)) (read(qt))
printf "Total: R$ %.2f\n" total