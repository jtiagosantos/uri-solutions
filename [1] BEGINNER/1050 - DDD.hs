{-
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

DDD     DESTINATION
61		Brasilia
71		Salvador
11		Sao Paulo
21		Rio de Janeiro
32		Juiz de Fora
19		Campinas
27		Vitoria
31		Belo Horizonte

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.
-}

tabela a = if a == 61 then "Brasilia"
else if a == 71 then "Salvador"
else if a == 11 then "Sao Paulo"
else if a == 21 then "Rio de Janeiro"
else if a == 32 then "Juiz de Fora"
else if a == 19 then "Campinas"
else if a == 27 then "Vitoria"
else if a == 31 then "Belo Horizonte"
else "DDD nao cadastrado"

main = do
ddd <- readLn :: IO Int
let resposta = tabela ddd
putStrLn resposta