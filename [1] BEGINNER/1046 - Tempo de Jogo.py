'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
'''

tempos = str(input()).split()
hora_inicial = int(tempos[0])
hora_final = int(tempos[1])
duracao = 0

if hora_inicial > hora_final:
    while hora_inicial != hora_final:
        hora_inicial += 1
        duracao += 1
        if hora_inicial == 24:
            hora_inicial = 0
elif hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
else:
    duracao = 24
    
print('O JOGO DUROU {} HORA(S)'.format(duracao))