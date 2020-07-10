'''
Os habitantes de Nlogônia são muito supersticiosos. Uma de suas crenças é que os números das casas de rua que têm um dígito repetido traz sorte ruim para os moradores. Portanto, eles nunca iriam viver em uma casa que tem o número 838 ou 1004, por exemplo.

A rainha de Nlogônia ordenou a construção de uma nova avenida à beira-mar e quer atribuir para as novas casas apenas números sem dígitos repetidos, para evitar desconforto entre os seus súditos. Você foi nomeado por Sua Majestade para escrever um programa que, dado dois inteiros N e M, determine a quantidade máxima possível de casas que podem assumir um número entre N e M inclusive, sem que ocorram dígitos repetidos nestes números.

Entrada
Cada teste é descrito usando uma linha. A linha contém dois inteiros N e M, conforme descrito acima (1 ≤ N ≤ M ≤ 5000).

Saída
Para cada caso de teste imprima um valor inteiro que representa a quantidade máxima possível de números de casa entre N e M inclusive, sem dígitos repetidos.
'''

while True:
    qt_casas = 0
    try:
        def test_num(valor):
            global qt_casas
            count = 0
            valor = list(str(valor))
            for i in valor:
                if valor.count(i) == 1:
                    count += 1
            if count == len(valor):
                qt_casas += 1

        intervalo = str(input()).split()
        valores = list(range(int(intervalo[0]), int(intervalo[1])+1))
        for valor in valores:
            test_num(valor)
        print(qt_casas)
    except EOFError:
        break
    