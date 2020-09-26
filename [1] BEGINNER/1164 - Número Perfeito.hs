{-
Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”, de acordo com a especificação fornecida.
-}

teste :: Int -> String
teste a | (a == sum([i | i <- [1..a], mod a i == 0, i /= a])) = " eh perfeito"
        | otherwise = " nao eh perfeito"

loop 0 = return ()
loop n = do
  num <- readLn :: IO Int
  let saida = teste (num)
  putStr (show(num))
  putStrLn saida
  loop (n-1)

main = do
  n <- readLn :: IO Int
  loop n