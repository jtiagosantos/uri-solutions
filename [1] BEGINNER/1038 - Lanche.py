'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1038_en.png" alt="Price Table">

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''

valores = str(input()).split()
cod = int(valores[0])
quant = int(valores[1])
if cod == 1:
    total = quant * 4.00
elif cod == 2:
    total = quant * 4.50
elif cod == 3:
    total = quant * 5.00
elif cod == 4:
    total = quant * 2.00
elif cod == 5:
    total = quant * 1.50
print('Total: R$ {:.2f}'.format(total))
