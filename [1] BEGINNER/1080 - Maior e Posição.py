'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

valores = []
for i in range(100):
    valores.append(int(input()))
pos = 0
for k,v in enumerate(valores):
    if v == max(valores):
        pos = k + 1
print(max(valores))
print(pos)
