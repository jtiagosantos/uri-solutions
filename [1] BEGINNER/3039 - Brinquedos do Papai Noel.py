'''
Papai Noel todo ano lê as cartinhas de Natal para saber o que dar de presente para cada criança. O problema é que muitas crianças não mandam suas cartinhas para o Papai Noel. Então ele decidiu que, para poupar o seu tempo, ele irá dar o mesmo presente para crianças que não mandaram cartinhas. Assim, ele decidiu que para os meninos ele irá dar um carrinho de brinquedo e para as meninas, uma boneca.

Entrada
A primeira linha da entrada possui um inteiro N (0 < N ≤ 1000), o número de crianças que não enviaram sua cartinha para o Papai Noel. As próximas N linhas consistem em duas strings, a primeira é o nome da criança, e a segunda é uma letra, que pode ser ‘M’, para dizer que é um menino, ou ‘F’ se for uma menina.

Saída
A saída consiste em 2 linhas. A primeira linha deve conter o número de carrinhos que o papai noel deve fazer, seguido pela palavra “carrinhos”, e na segunda linha, o número de bonecas seguido pela palavra “bonecas”.
'''

N = int(input())
carrinho = boneca = 0
for i in range(N):
    entradas = str(input()).split()
    nome = entradas[0]
    sexo = entradas[1].upper()
    if sexo == 'M':
        carrinho += 1
    if sexo == 'F':
        boneca += 1
print('{} carrinhos'.format(carrinho))
print('{} bonecas'.format(boneca))
    