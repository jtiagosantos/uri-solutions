{-
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

Entrada
A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.

Saída
Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.
-}

teste :: Int -> Int -> String
teste a b = if a > b then "Decrescente" else "Crescente"

loop n m = if n == m then return ()
           else
               do
                 let saida = teste n m
                 putStrLn(saida)
                 main

main = do
  valores <- getLine
  let lista = words valores
  let a = lista !! 0
  let b = lista !! 1
  loop (read(a)) (read(b))