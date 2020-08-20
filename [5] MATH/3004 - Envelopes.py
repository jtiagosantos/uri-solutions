'''
Uma empresa quer mandar um envelope para obter uma resposta de um cliente e quer saber se é possível colocar esse envelope dentro de outro. Ambos envelopes são retangulares e um só pode ser colocado dentro do outro se as dimensões forem ambas menores. Dadas as dimensões dos dois envelopes, responda se é possível ou não colocar o primeiro dentro do segundo.

Entrada
A entrada consiste de uma série de testes. A primeira linha contém um único inteiro indicando o número n (1 ≤ n ≤ 20) de casos de testes. A seguir vêm n linhas contendo, cada uma, um caso de teste. Cada caso de teste se compõe de 4 inteiros: os dois primeiros são as dimensões do envelope que deve ir dentro e os dois últimos, a dimensão do envelope principal.

Saída
Para cada caso de teste imprima, em uma linha:

. 'S' se for possível colocar o primeiro envelope dentro do segundo, ou

. 'N', caso contrário.
'''

N = int(input())
for _ in range(N):
    env_1 = []
    env_2 = []
    count = 0
    entrada = str(input()).split()
    env_1.append(int(entrada[0]))
    env_1.append(int(entrada[1]))
    env_2.append(int(entrada[2]))
    env_2.append(int(entrada[3]))
    env_1 = sorted(env_1)
    env_2 = sorted(env_2)
    for a, b in zip(env_1, env_2):
        if b > a:
            count += 1
    if count == 2:
        print('S')
    else:
        print('N')