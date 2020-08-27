'''
Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, 
um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. 
A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão 
ser considerados na operação.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1182.png

Entrada
A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação. 
A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média)
 que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''

coluna_matriz = int(input())
operacao = str(input()).upper()

matriz = []

for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)

elementos_coluna = []

for i in range(12):
    elementos_coluna.append(matriz[i][coluna_matriz])

if operacao == 'S':
    print('{:.1f}'.format(sum(elementos_coluna)))
if operacao == 'M':
    print('{:.1f}'.format(sum(elementos_coluna)/len(elementos_coluna)))
    