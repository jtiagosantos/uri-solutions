'''
Neste problema sua tarefa será ler vários números e em seguida dizer quantas vezes cada número aparece na entrada de dados, ou seja, deve-se escrever cada um dos valores distintos que aparecem na entrada por ordem crescente de valor.

Entrada
A entrada contém apenas 1 caso de teste. A primeira linha de entrada contem um único inteiro N, que indica a quantidade de valores que serão lidos para X (1 ≤ X ≤ 2000) logo em seguida. Com certeza cada número não aparecerá mais do que 20 vezes na entrada de dados.

Saída
Imprima a saída de acordo com o exemplo fornecido abaixo, indicando quantas vezes cada um deles aparece na entrada por ordem crescente de valor.
'''

N = int(input())
valores = []
valores_unicos = []
for c in range(N):
    valores.append(int(input()))
for num in valores:
    if not num in valores_unicos:
        valores_unicos.append(num)
valores_unicos = sorted(valores_unicos)
for i in valores_unicos:
    print('{} aparece {} vez(es)'.format(i, valores.count(i)))