'''
Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

Entrada
A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural N1(1 < N1 < 10^10), a segunda linha é composta por um valor N2( N1 < N2 < 10^32).

Saída
Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.
'''

count = 1
while True:
    try:
        N1 = str(input())
        N2 = str(input())
        qt_sub = N2.count(N1)
        pos = N2.rfind(N1)+1
        print('Caso #{}:'.format(count))
        if qt_sub >= 1:
            print('Qtd.Subsequencias: {}'.format(qt_sub))
            print('Pos: {}'.format(pos))
            print()
        else:
            print('Nao existe subsequencia')
            print()
        count += 1
    except EOFError:
        break