'''
Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.
'''

N = int(input())
for i in range(1, N):
    if N % i == 0:
        print(i)
print(N)