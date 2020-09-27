{-
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com 
mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
-}

import Text.Printf

calculo_triangulo :: Double -> Double -> Double
calculo_triangulo a c = (a * c) / 2

calculo_circulo :: Double -> Double
calculo_circulo c = 3.14159 * (c ** 2)

calculo_trapezio :: Double -> Double -> Double -> Double
calculo_trapezio a b c = (a + b) * c / 2

calculo_quadrado :: Double -> Double
calculo_quadrado b = b ** 2

calculo_retangulo :: Double -> Double -> Double
calculo_retangulo a b = a * b

main = do
valores <- getLine
let lista = words valores
let a = lista !! 0
let b = lista !! 1
let c = lista !! 2
let area_triangulo = calculo_triangulo (read(a)) (read(c))
let area_circulo = calculo_circulo (read(c))
let area_trapezio = calculo_trapezio (read(a)) (read(b)) (read(c))
let area_quadrado = calculo_quadrado (read(b))
let area_retangulo = calculo_retangulo (read(a)) (read(b))

printf "TRIANGULO: %.3f\n" area_triangulo
printf "CIRCULO: %.3f\n" area_circulo
printf "TRAPEZIO: %.3f\n" area_trapezio
printf "QUADRADO: %.3f\n" area_quadrado
printf "RETANGULO: %.3f\n" area_retangulo