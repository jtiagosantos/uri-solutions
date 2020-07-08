'''
O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC. Só que teve um problema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge você para fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do produto e seu respectivo valor.

1001 | R$ 1.50

1002 | R$ 2.50

1003 | R$ 3.50

1004 | R$ 4.50

1005 | R$ 5.50

Entrada
A primeira entrada informada é a quantidade de produtos comprados (1 <= p <= 5). Para cada produto segue a quantidade (1 <= q <= 500) que o consumidor comprou.

Obs.: não poderão ser informados números de produtos repetidos.

Saída
Você deve imprimir o valor da compra com duas casas decimais.
'''

qt_produtos = int(input())
total = 0
for i in range(qt_produtos):
    preco = x = 0
    entradas = str(input()).split()
    cod = int(entradas[0])
    qt = int(entradas[1])
    if cod == 1001:
        preco = 1.50
    if cod == 1002:
        preco = 2.50
    if cod == 1003:
        preco = 3.50
    if cod == 1004:
        preco = 4.50
    if cod == 1005:
        preco = 5.50
        
    x = preco * qt
    
    total += x
    
print('{:.2f}'.format(total))
