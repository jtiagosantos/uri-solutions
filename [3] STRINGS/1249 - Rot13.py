'''
Escreva um programa que receba uma mensagem "secreta" e retorne esta mensagem codificada. A mensagem é codificada com uma cifra chamada rot13. Rot13 funciona da seguinte maneira, é atribuido para cada letra um índice, baseado em sua posição no alfabeto. a = 1, b = 2, c = 3, ..., z = 26. Cada letra da mensagem deve ser deslocada 13 posições para a direita, se o fim do alfabeto for atingido, a contagem recomeça no primeiro caracter do alfabeto. Por exemplo, o caracter "a" (aspas apenas para evidenciar), seria mapeado para "n", "y" para "l", "f" para "s", e assim por diante. O mesmo processo é feito para letras maiúsculas também. Quaisquer caracteres não-alfabéticos devem ser repassados para a saída sem alterações.

Entrada
A entrada contém vários casos de teste e termina com final de arquivo (EOF). Cada caso de teste consiste de uma linha que contém uma mensagem com no mínimo 1 no máximo 50 caracteres inclusive, contendo letras, números, e os símbolos: !@#$%^&*()-_=+[]{}|;':,./<>?"

Saída
Para cada linha da entrada, imprima uma linha na saída com a mensagem cifrada pelo método rot13.
'''

caracteres = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        mensagem = str(input())
        new_msg = str()
        for m in mensagem:
            if m.lower() in caracteres:
                pos_m = caracteres.index(m.lower()) + 13
                if pos_m > 25:
                    pos_m -= 26
                if m == m.upper():
                    new_msg += caracteres[pos_m].upper()
                if m == m.lower():
                    new_msg += caracteres[pos_m].lower()
            else:
                new_msg += m
        print(new_msg)
    except EOFError:
        break
