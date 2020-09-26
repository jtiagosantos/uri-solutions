{-
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
-}

soma_impar :: Int -> Int -> Int
soma_impar a b = sum([i | i<- [min a b .. max a b], mod i 2 /= 0, i /=a , i /= b])

loop 0 = return ()
loop n = do
 valores <- getLine
 let lista = words valores
 let a = lista !! 0
 let b = lista !! 1
 let saida = soma_impar (read(a)) (read(b))
 print (saida)
 loop (n-1)

main = do
  n <- readLn :: IO Int
  loop (n)