'''
Dada uma pilha de n cartas enumeradas de 1 até n com a carta 1 no topo e a carta n na base.  A seguinte operação é ralizada enquanto tiver 2 ou mais cartas na pilha.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1110.jpg

Jogue fora a carta do topo e mova a próxima carta (a que ficou no topo) para a base da pilha.

Sua tarefa é encontrar a sequência de cartas descartadas e a última carta remanescente.

Cada linha de entrada (com exceção da última) contém um número n ≤ 50. A última linha contém 0 e não deve ser processada. Cada número de entrada produz duas linhas de saída. A primeira linha apresenta a sequência de cartas descartadas e a segunda linha apresenta a carta remanescente.

Entrada
A entrada consiste em um número indeterminado de linhas contendo cada uma um valor de 1 até 50. A última linha contém o valor 0.

Saída
Para cada caso de teste, imprima duas linhas. A primeira linha apresenta a sequência de cartas descartadas, cada uma delas separadas por uma vírgula e um espaço. A segunda linha apresenta o número da carta que restou. Nenhuma linha tem espaços extras no início ou no final. Veja exemplo para conferir o formato esperado.
'''

while True:
    N = int(input())
    if N == 0:
        break
    valores = list(range(1, N+1))
    for k,v in enumerate(valores):
        valores[k] = str(v)
    seq = []
    while len(valores) > 1:
        seq.append(valores[0])
        del valores[0]
        valores.append(valores.pop(0))
    print('Discarded cards:', end=' ')
    for c in range(len(seq)-1):
        print(seq[c]+',', end= ' ')
    print(seq[len(seq)-1])
    print('Remaining card: {}'.format(valores[0]))
        