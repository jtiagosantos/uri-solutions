'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, 
calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal principal da 
matriz, conforme ilustrado abaixo (área verde).

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1183.png

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média)
que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''

operacao = str(input()).upper()

matriz = []
elementos = []
i = 1

for _ in range(12):
    linha_matriz = []
    for _ in range(12):
        linha_matriz.append(float(input()))
    matriz.append(linha_matriz)

for linha in matriz:
    elementos.append(sum(linha[i:]))
    i += 1

if operacao == 'S':
    print('{:.1f}'.format(sum(elementos)))
if operacao == 'M':
    print('{:.1f}'.format(sum(elementos)/66))
    