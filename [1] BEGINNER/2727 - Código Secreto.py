'''
Joana gosta de brincar de fingir ser uma agente secreta com suas amigas Bruna, Jaqueline e Laura. Joana e Bruna criaram um código secreto para se comunicar sem que suas inimigas descubram seus planos.
O código secreto funciona da seguinte forma:

A letra 'a' é representada por um único ponto '.'
A letra 'b' é representada por dois pontos '..'
A letra 'c' é representada por três pontos '...'
As demais letras seguem a lógica anterior, porém cada conjunto de pontos está separado por um espaço e sempre com um conjunto a mais de pontos, como no exemplo abaixo:

                                . → a
                                .. → b

                                ... → c

                                . . → d

                                .. .. → e
                                ... ... → f

                                . . . → g
                                .. .. .. → h
                                ... ... ... → i

O seu objetivo é criar um programa que decifre as mensagens secretas e ajudar Jaqueline e Laura descobrirem o que Joana e Bruna estão planejando.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada teste deverá conter um inteiro (N ≤ 50), que representa a quantidade de letras a serem decifradas e as N linhas seguintes contêm o código de cada letra.

Saída
Uma string representando a letra do alfabeto correspondente ao código de entrada. Cada string deve estar separada da outra por uma nova linha.
'''

simbolos = {
    '.':'a',
    '..':'b',
    '...':'c',
    '. .':'d',
    '.. ..':'e',
    '... ...':'f',
    '. . .':'g',
    '.. .. ..':'h',
    '... ... ...':'i',
    '. . . .':'j',
    '.. .. .. ..':'k',
    '... ... ... ...':'l',
    '. . . . .':'m',
    '.. .. .. .. ..':'n',
    '... ... ... ... ...':'o',
    '. . . . . .':'p',
    '.. .. .. .. .. ..':'q',
    '... ... ... ... ... ...':'r',
    '. . . . . . .':'s',
    '.. .. .. .. .. .. ..':'t',
    '... ... ... ... ... ... ...':'u',
    '. . . . . . . .':'v',
    '.. .. .. .. .. .. .. ..':'w',
    '... ... ... ... ... ... ... ...':'x',
    '. . . . . . . . .':'y',
    '.. .. .. .. .. .. .. .. ..':'z'
}


while True:
    try:
        lista = []
        N = int(input())
        for n in range(N):
            lista.append(str(input()))
        for l in lista:
            print(simbolos[l])
    except EOFError:
        break
