'''
Nesse problema você deverá descobrir se um conjunto de diversas palavras é bom ou ruim. Por definição, um conjunto é bom quando nenhuma palavra desse conjunto é um prefixo de uma outra palavra. Caso contrário, este é considerado um conjunto ruim.

Por exemplo, {abc, dae, abcde} é um conjunto ruim, pois abc é um prefixo de abcde. Quando duas palavras são iguais, definimos como uma sendo prefixo da outra.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste terá um inteiro N (1 ≤ N ≤ 10⁵), representando a quantidade de palavras no conjunto. Segue então N linhas, cada uma tendo uma palavra de no máximo 100 letras minúsculas. A entrada termina quando N = 0 e não deve ser processada.

Saída
Para cada caso de teste, você deverá imprimir Conjunto Bom, ou Conjunto Ruim, conforme explicado acima.
'''

def teste(conjunto):
    prefixos = []
    prefixos = [i for i in conjunto if not i in prefixos]
    for i in prefixos:
        tamanho_prefixo = len(i)
        conjunto.remove(i)
        for c in conjunto:
            if i in c[:tamanho_prefixo]:
                return 'Conjunto Ruim'
    conjunto.append(i)
    return 'Conjunto Bom'


while True:
    conjunto = []
    N = int(input())
    if N == 0:
        break
    for _ in range(N):
        conjunto.append(input())
        
    conjunto = sorted(conjunto, key = lambda i: len(i))
    validador = teste(conjunto)
    print(validador)