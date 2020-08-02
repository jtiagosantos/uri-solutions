'''
Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que Humberto pudesse responder, o papagaio gritou: “Ai eu caio, idiota!”.

Entrada
A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a situação de levantamento de pernas do papagaio.

Saída
Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. Caso ele levante as duas pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.
'''

while True:
    try:
        string = str(input())
        if string == 'esquerda':
            print('ingles')
        elif string == 'direita':
            print('frances')
        elif string == 'nenhuma':
            print('portugues')
        elif string == 'as duas':
            print('caiu')
    except EOFError:
        break
    