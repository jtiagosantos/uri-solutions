'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''

idade = int(input())
qt_ano = qt_mes = qt_dia = 0

#Para a quantidade de anos:
while True:
    if idade < 365:
        break
    else:
        idade -= 365
        qt_ano += 1
        
#Para a quantidade de meses:
while True:
    if idade < 30:
        break
    else:
        idade -= 30
        qt_mes += 1
        
qt_dia = idade

print('{} ano(s)'.format(qt_ano))
print('{} mes(es)'.format(qt_mes))
print('{} dia(s)'.format(qt_dia))
