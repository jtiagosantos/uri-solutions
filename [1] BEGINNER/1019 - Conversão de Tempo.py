'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''

h = m = s = 0
tempo = int(input())
#While pra calcular as horas:
while True:
    if tempo < 3600:
        break
    else:
        tempo -= 3600
        h += 1
#While para calcular os minutos
while True:
    if tempo < 60:
        break
    else:
        tempo -= 60
        m += 1
s = tempo
print(h,m,s, sep=':')        