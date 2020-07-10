'''
João e Maria criaram sua própria versão de jogar dardos, dardos por distância. Cada um jogava 3 dardos, escolhendo qual distância irão jogar do alvo. No jogo normal de dardos, se pontua um número 
x
  pela distância entre onde o dardo acertou e o centro do alvo. No jogo de João e Maria se pontua 
x
×
d
 onde 
d
 é a distancia do atirador e o alvo.

João pede para você fazer um algorítimo que dado a pontuação e a distância de cada jogada devolve o vencedor

Entrada
A primeira linha da entrada consite em um número N de casos de teste. Em cada caso de teste haverão 6 linhas, onde as primeiras 3 linhas correspondem aos arremessos de João e as próximas 3 linhas aos arremessos de Maria. Cada linha de um caso de teste consiste em dois números X e D onde X é a pontuação e D é a distância 

Saída
A saída consiste no vencedor de cada caso de teste.
'''

N = int(input())
for i in range(N):
    pt_joao = []
    pt_maria = []
    for i in range(3):
        valores = str(input()).split()
        x = int(valores[0])
        d = int(valores[1])
        pt_joao.append(x*d)
    for i in range(3):
        valores = str(input()).split()
        x = int(valores[0])
        d = int(valores[1])
        pt_maria.append(x*d)
    if sum(pt_joao) > sum(pt_maria):
        print('JOAO')
    else:
        print('MARIA')