'''
Armandinho tem um amigo o tanto quanto chato, chamado Laércio. Quando jogam o jogo do mestre manda, um jogo onde alguém 
dá uma ordem e alguém a cumpre, e em vez de dar ordens legais como subir em uma árvore, pular o muro, plantar bananeira
ou organizar manifestações para derrubar o governo (independente de quem estiver no poder) ele sempre pede algo maçante. 
Em sua última partido, Laércio exigiu que Armandinho ordenasse uma lista de números, de forma que apenas os números ímpares 
aparecessem e o primeiro item seja o maior, o segundo seja o menor, o terceiro o segundo maior, o quarto seja o segundo menor 
e assim por diante. Como fazer isso a mão é muito chato, Armandinho procurou sua ajuda.

Entrada
A entrada consiste de um inteiro N que representa o número de casos testes ( 1<N<1000 ). Cada caso teste começa com um 
inteiro M, que representa o tamanho da lista (0<M<100). Seguem M inteiros Mi (0<Mi < 1000) que representam a lista de Laércio.

Saída
Imprima a lista ordenada como Laércio requisitou, com um espaço entre os valores, pulando uma linha a cada caso teste.
'''

def ordenacao(lista):
    array = []
    for k, v in enumerate(lista[::]):
        if k % 2 == 0:
            array.append(max(lista))
            lista.remove(max(lista))
        else:
            array.append(min(lista))
            lista.remove(min(lista))
    return array
    

N = int(input())
for _ in range(N):
    M = int(input())
    lista = str(input()).split(); lista = [int(i) for i in lista if int(i) % 2 != 0]
    array = ordenacao(lista)
    if array == []:
        print()
    else:
        print(' '.join([str(i) for i in array]))