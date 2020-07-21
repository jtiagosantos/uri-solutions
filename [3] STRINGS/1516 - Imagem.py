'''
Rafael encontrou um novo hobbie: fazer desenhos usando caracteres do teclado. Por mais simples ou limitada que essa nova forma de arte possa parecer, basta criatividade para se fazer os mais diferentes tipos de desenhos.

Após fazer alguns desenhos, Rafael imaginou como seriam se eles fossem redimensionados, porém ter que refazer todo o desenho pareceu meio cansativo. Para isso, Rafael pediu sua ajuda.

Em um redimensionamento, uma imagem com N linhas e M colunas passa a ter A linhas e B colunas, e, dado que as novas dimensões da imagem redimensionada é maior do que as dimensões da imagem original, alguns caracteres terão que se repetir.

Digamos que A seja 3 vezes maior que N. Nesse caso, cada linha terá que se repetir 3 vezes, para que a imagem seja redimensionada de forma correta.

Dado um desenho feito por Rafael, imprima como seria se o desenho fosse redimensionado para uma determinada nova dimensão.

Entrada
Haverá diversos casos de teste. Cada caso de teste inicia com dois inteiros N e M (1 ≤ N, M ≤ 50), representando, respectivamente, a altura e a largura do desenho de Rafael.

A seguir haverá N linhas, contendo M caracteres cada, representando o desenho feito por Rafael. Após, haverá dois inteiros A e B (N < A ≤ 100, M < B ≤ 100, A é múltiplo de N, e B é multiplo de M), representando, respectivamente, a nova altura e largura que Rafael deseja que seu desenho tenha.

O último caso de teste é indicado quando N = M = 0, o qual não deverá ser processado.

Saída
Para cada caso de teste, imprima A linhas, contendo B caracteres cada, representando o desenho de Rafael redimensionado.

Após cada caso de teste, imprima uma linha em branco.
'''

while True:
    entrada_1 = str(input())
    if entrada_1 == '0 0':
        break
    entrada_1 = entrada_1.split()
    N = int(entrada_1[0])
    M = int(entrada_1[1])
    desenho = []
    new_desenho = []
    new = ''
    for c in range(N):
         desenho.append(str(input()))
    entrada_2 = str(input()).split()
    A = int(entrada_2[0])
    B = int(entrada_2[1])
    new_h = int(A / N)
    new_l = int(B / M)
    for d in desenho:
        new = ''
        for dd in d:
            new += dd*new_l
        new_desenho.append(new)
    for nd in new_desenho:
        for i in range(new_h):
            print(nd)
    print()
    