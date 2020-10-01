{-
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
-}

import Data.List

ordena :: [Int] -> [Int]
ordena lista = sort(lista)

main = do
  valores <- getLine
  let lista = words valores
  let a = lista !! 0
  let b = lista !! 1
  let c = lista !! 2
  let lista' = [(read(a)), (read(b)), (read(c))]
  let saida = ordena (lista')
  putStrLn (show(saida !! 0))
  putStrLn (show(saida !! 1))
  putStrLn (show(saida !! 2))
  putStrLn("")
  putStrLn(a)
  putStrLn(b)
  putStrLn(c)