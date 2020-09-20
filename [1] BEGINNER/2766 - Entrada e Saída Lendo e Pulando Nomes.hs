{-
O seu professor gostaria de fazer um programa com as seguintes características:

Leia 10 nomes, sem espaço em branco;
Imprima o terceiro nome da lista;
Imprima o sétimo nome da lista;
Imprima o nono nome da lista.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem dez linhas. Em cada linha tem um nome de no máximo 30 caracteres e sem espaço em branco. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas conforme os procedimentos 2, 3 e 4. Conforme mostra o exemplo de saída a seguir.
-}

main = do
a <- getLine
b <- getLine
c <- getLine
d <- getLine
e <- getLine
f <- getLine
g <- getLine
h <- getLine
i <- getLine
j <- getLine
let lista = a:b:c:d:e:f:g:h:i:j:[]
putStrLn (lista !! 2)
putStrLn (lista !! 6)
putStrLn (lista !! 8)