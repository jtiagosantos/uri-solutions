'''
É dado na entrada uma string A e outra B. Em uma operação você pode escolher uma letra da primeira string e avançar esta letra. 
Avançar uma letra significa transformá-la na próxima letra do alfabeto, veja que a próxima letra depois de z vem a letra a novamente!

Por exemplo, podemos transformar a string ab em bd em no mínimo 3 operações: ab -> bb -> bc -> bd. Podemos aplicar operações nas letras 
em qualquer ordem, outra possibilidade seria: ab -> ac -> bc -> bd.

Dadas as duas strings, calcule o mínimo número de operações necessárias para transformar a primeira na segunda.

Entrada
Na primeira linha terá um inteiro T (T ≤ 100) indicando o número de casos de teste.

Para cada caso, na única linha teremos as duas strings A (1 ≤ |A| ≤ 100* ou 1 ≤ |A| ≤ 104** - sendo que |A| significa o tamanho da string 
A) e B (|B| = |A|* ou |B| = |A​|**) separadas por um espaço. Ambas as strings são compostas por letras do alfabeto minúsculas apenas e são do mesmo tamanho.

*Ocorre em aproximadamente 90% dos casos de teste;

**Ocorre nos demais casos de teste.

Saída
Para cada caso imprima o número mínimo de operações.
'''

alfabeto = list('abcdefghijklmnopqrstuvwxyz')
T = int(input())
for _ in range(T):
    num_operacoes = 0
    entrada = input().split()
    lista_1 = list(entrada[0])
    lista_2 = list(entrada[1])
    for x,y in zip(lista_1, lista_2):
        if alfabeto.index(x) < alfabeto.index(y):
            num_operacoes += alfabeto.index(y) - alfabeto.index(x)
        elif alfabeto.index(x) > alfabeto.index(y):
            num_operacoes += 26 - alfabeto.index(x) + alfabeto.index(y)
          
    print(num_operacoes)