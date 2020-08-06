'''
O Senhor Claus recebe as mais diversas cartas de crianças do mundo todo. Todo ano, sem exceções, ele seleciona algumas das cartas mais legais para dar maior atenção a elas. Neste ano, uma dessas cartas chamou a atenção de Claus por um motivo bem peculiar: a carta estava criptografada! Nela, continha a carta com o pedido de natal, e um bilhete anexado que dizia o seguinte:

"Sr. Papai Noel: imagino que você deva receber muitas cartas de natal, mas deve ser quase chato ter que ler todas elas sem nenhum desafio. Espero que a minha traga um pouco de diversão ao senhor. Eu troquei todas as vogais das palavras por símbolos. Use essa tabela para traduzir meu pedido!"

https://resources.urionlinejudge.com.br/gallery/images/contests/UOJ_3375.jpg

Vamos ajudar o Senhor Claus a traduzir essa carta?

Entrada
A entrada é composta por diversos casos de teste e termina em EOF. Cada caso de teste corresponde a uma frase F (5 < F < 256), composta por letras minúsculas, os símbolos da tabela de criptografia e espaços em branco. Cada caso de teste é terminado por uma quebra de linha.

Saída
Imprima a frase descriptografada, com auxílio da tabela fornecida pela criança que escreveu a carta.
'''

tabela = {
    '@':'a',
    '&':'e',
    '!':'i',
    '*':'o',
    '#':'u'
    }
    
while True:
    try:
        frase = list(str(input()))
        for i in frase:
            if i in tabela.keys():
                frase[frase.index(i)] = tabela[i]
        print(''.join(frase))
    except EOFError:
        break