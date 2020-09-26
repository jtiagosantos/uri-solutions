{-
Você tem em mãos dois cabos circulares de energia. O primeiro cabo tem raio R1 e o segundo raio R2. Você precisa comprar um conduite circular (veja a imagem abaixo que ilustra um conduite) de maneira a passar os dois cabos por dentro dele:

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1589.jpg

Qual o menor raio do conduite que você deve comprar? Em outras palavras, dado dois círculos, qual o raio do menor círculo que possa englobar ambos os dois?

Entrada
Na primeira linha teremos um inteiro T (T ≤ 10000), indicando o número de casos de teste.

Na única linha de cada caso teremos dois números inteiros R1 e R2, indicando os respectivos raios. Os inteiros serão positivos e todas as contas caberão em um inteiro normal de 32 bits.
Saída
Em cada caso, imprima o menor raio possível em uma única linha
-}

loop 0 = return ()
loop n = do
  valores <- getLine
  let lista = words valores
  let a = lista !! 0
  let b = lista !! 1
  let soma = (read(a)) + (read(b))
  print(soma)
  loop (n-1)

main = do
  n <- readLn :: IO Int
  loop n