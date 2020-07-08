'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
'''

valores = []
numerador = denominador = 1
cont = 1
for i in range(20):
    cont *= 2
while denominador != cont:
    S = numerador / denominador
    valores.append(S)
    numerador += 2
    denominador *= 2
print('{:.2f}'.format(sum(valores)))
