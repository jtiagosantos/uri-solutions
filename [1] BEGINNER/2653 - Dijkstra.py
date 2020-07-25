'''
No jogo O Bruxo, Sigismund Dijkstra é o líder do Serviço Secreto Redaniano, por causa disso ele é uma das pessoas mais importantes do mundo.

Além disso Dijkstra possui um grande tesouro, o qual possui diversos tipos de jóias.

Dijkstra está muito curioso para saber quantos tipos de jóias diferentes seu tesouro possui.

Sabendo que você é o melhor programador do continente Dijkstra te contratou para verificar quantos tipos de jóias distintas ele tem em seu tesouro.

Entrada
A entrada consiste de várias linhas e cada uma contém uma string que descreve uma das jóias de Dijkstra. Essa string é composta apenas dos caracteres '(' e ')', a soma do tamanho de todas as string não excede 106.

Saída
Imprima quantos tipos de jóias distintas Dijkstra tem.
'''

joias = []
while True:
    try:
        joia = str(input())
        if not joia in joias:
            joias.append(joia)
    except EOFError:
        break
print(len(joias))