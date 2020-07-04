'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salary	  Readjustment Rate
0 - 400.00				15%
400.01 - 800.00			12%
800.01 - 1200.00		10%
1200.01 - 2000.00		 7%
Above 2000.00			 4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
'''

salario = float(input())
percentual = novo_salario = 0

if salario >= 0 and salario <= 400.00:
    percentual = 15
    novo_salario = salario + salario * 0.15
elif salario >= 400.01 and salario <= 800.00:
    percentual = 12
    novo_salario = salario + salario * 0.12
elif salario >= 800.01 and salario <= 1200.00:
    percentual = 10
    novo_salario = salario + salario * 0.10
elif salario >= 1200.01 and salario <= 2000.00:
    percentual = 7
    novo_salario = salario + salario * 0.07
elif salario > 2000.00:
    percentual = 4
    novo_salario = salario + salario * 0.04

print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(novo_salario - salario))
print('Em percentual: {}'.format(str(percentual)+' %'))