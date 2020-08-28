'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área 
inferior da matriz, conforme ilustrado abaixo (área verde).

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1188.png

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação
(Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto
flutuante de dupla precisão (double) que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''

operacao = input().upper(); matriz = []; elementos = []; a,b = 5, 7

for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)
    
for linha in matriz[7:]:
    elementos.append(sum(linha[a:b]))
    a -= 1; b += 1
    
if operacao == 'S':
    print('{:.1f}'.format(sum(elementos)))
if operacao == 'M':
    print('{:.1f}'.format(sum(elementos)/30))