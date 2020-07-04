'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''

N = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for i in notas:
    qt_notas = int(N/i)
    print('{} nota(s) de R$ {:.2f}'.format(qt_notas, i))
    N -= qt_notas * i
print('MOEDAS:')
for i in moedas:
    qt_moedas = int(round(N,2)/i)
    print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas,i))
    N -= qt_moedas * i

