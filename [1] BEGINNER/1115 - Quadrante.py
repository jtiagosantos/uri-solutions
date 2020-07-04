'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.
'''

while True:
    coord = str(input()).split()
    X = int(coord[0])
    Y = int(coord[1])
    if X == 0 or Y == 0:
        break
    else:
        if X > 0 and Y > 0:
            print('primeiro')
        elif X < 0 and Y > 0:
            print('segundo')
        elif X < 0 and Y < 0:
            print('terceiro')
        elif X > 0 and Y < 0:
            print('quarto')
    