'''
A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata de numerar as 
páginas de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas pois, 
quando necessário, dividem o livro em volumes.

Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na numeração romana.

Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000.

Entrada
A entrada é um número inteiro positivo N (0 < N < 1000).

Saída
A saída é o número N escrito na numeração romana em uma única linha. Use sempre letras maiúsculas.
'''

unidade = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX'
    }

dezena = {
    0: '',
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC'
    }

centena = {
    0: '',
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'DCCC',
    9: 'CM'
    }

N = int(input())
N = [int(i) for i in list(str(N))]

if len(N) == 1:
    print('{}'.format(unidade[N[0]]))

if len(N) == 2:
    print('{}{}'.format(dezena[N[0]], unidade[N[1]]))

if len(N) == 3:
    print('{}{}{}'.format(centena[N[0]], dezena[N[1]], unidade[N[2]]))