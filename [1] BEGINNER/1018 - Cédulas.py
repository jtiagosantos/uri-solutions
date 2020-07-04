'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

N = int(input())
valor = N
qt_cem = qt_cinq = qt_vin = qt_dez = qt_cinc = qt_dois = qt_um = 0

#Para a cédula de R$100,00:
while True:
    if N < 100:
        break
    else:
        N -= 100
        qt_cem += 1

#Para a cédula de R$50,00:
while True:
    if N < 50:
        break
    else:
        N -= 50
        qt_cinq += 1

#Para a cédula de R$20,00:
while True:
    if N < 20:
        break
    else:
        N -= 20
        qt_vin += 1

#Para a cédula de R$10,00:
while True:
    if N < 10:
        break
    else:
        N -= 10
        qt_dez += 1

#Para a cédula de R$5,00:
while True:
    if N < 5:
        break
    else:
        N -= 5
        qt_cinc += 1

#Para a cédula de R$2,00:
while True:
    if N < 2:
        break
    else:
        N -= 2
        qt_dois += 1

qt_um = N

print(valor)
print('{} nota(s) de R$ 100,00'.format(qt_cem))
print('{} nota(s) de R$ 50,00'.format(qt_cinq))
print('{} nota(s) de R$ 20,00'.format(qt_vin))
print('{} nota(s) de R$ 10,00'.format(qt_dez))
print('{} nota(s) de R$ 5,00'.format(qt_cinc))
print('{} nota(s) de R$ 2,00'.format(qt_dois))
print('{} nota(s) de R$ 1,00'.format(qt_um))
