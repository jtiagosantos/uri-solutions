'''
Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
'''

N = int(input())
cont = 1
for i in range(N):
    print(cont, cont ** 2, cont **3, sep = ' ')
    cont +=1