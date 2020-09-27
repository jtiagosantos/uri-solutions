{-
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.
-}

mes n = if n == 1 then "January"
else if n == 2 then "February"
else if n == 3 then "March"
else if n == 4 then "April"
else if n == 5 then "May"
else if n == 6 then "June"
else if n == 7 then "July"
else if n == 8 then "August"
else if n == 9 then "September"
else if n == 10 then "October"
else if n == 11 then "November"
else "December"

main = do
num <- getLine
let resposta = mes (read(num))
putStrLn resposta