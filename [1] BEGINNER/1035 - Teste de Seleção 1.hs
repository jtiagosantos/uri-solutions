{-
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.
-}

teste a b c d = if b > c && d > a && c + d > a + b && c >= 0 && d >= 0 && rem a 2 == 0 then "Valores aceitos"
	else do
		"Valores nao aceitos"

main = do
valores <- getLine
let lista = words valores
let x = lista !! 0
let y = lista !! 1
let z = lista !! 2
let w = lista !! 3
let resposta = teste (read(x)) (read(y)) (read(z)) (read(w))

putStrLn resposta