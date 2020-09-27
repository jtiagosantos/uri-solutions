{-
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
-}

multiplos a b = 
	if rem b a == 0 || rem a b == 0 then "Sao Multiplos\n" 
		else do
		 "Nao sao Multiplos\n"


main = do
valores <- getLine
let lista = words valores
let a = lista !! 0
let b = lista !! 1
let mul = multiplos (read(a)) (read(b))
putStr mul