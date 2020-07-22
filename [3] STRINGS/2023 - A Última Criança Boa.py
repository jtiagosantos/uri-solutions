'''
Papai Noel classifica todas as crianças do mundo em duas listas: uma das boazinhas e outra das malcriadas. Ele gostaria de saber qual das crianças do mundo é a última da lista de boazinhas, se usar a ordem alfabética. Para isso, ele pediu a todos seus elfos ajudantes que escrevessem os nomes das crianças boas em uma folha.

Entretanto, cada elfo escreveu os nomes de um jeito: maiúscula no início e minúsculas depois, todas maiúsculas, todas minúsculas, e todo tipo de combinação entre maiúsculas e minúsculas.

Papai Noel quer sua ajuda para, dada a lista de nome das crianças boas, dizer qual delas é a última.

Entrada
A entrada possui várias linhas. Em cada linha há o nome de uma criança boa. Nenhum elfo escreveu os nomes com acentos. O maior nome tem no máximo 80 caracteres. Não existem mais de 1000 crianças na lista. Todos os nomes são distintos. A lista de nomes termina com EOF.

Saída
A saída é dada em uma linha. O nome da criança que fica na última posição da lista deve ser mostrado. Mostre o nome exatamente como foi lido na entrada. Use a ordem alfabética dos nomes para ordenar, mas considere maiúsculas e minúsculas como iguais.
'''

lista = []
while True:
    try:
        lista.append(str(input()))
    except EOFError:
        break
lista = sorted(lista, key=str.lower)
print(lista[-1])
