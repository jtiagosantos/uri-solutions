'''
A fórmula de cálculo de uma derivada de uma função na forma xn é definida por:

f(x) = xn  →  f(x)’ = n.xn-1

Veja um exemplo:

f(x) = 4x3 + 3x2  →  f(x)’ = 12x2 + 6x

Escreva um programa que, dado um polinômio simples, calcule a sua derivada.

Entrada
Haverá diversos casos de teste. Cada caso de teste é formado por um número inteiro T, que representa a quantidade de termos que o polinômio possui. Na linha seguinte, há o polinômio propriamente dito, formado por T (1 ≤ T ≤ 100) termos, todos separados por um espaço, um sinal de soma e outro espaço, e cada um contendo um inteiro C (2 ≤ C ≤ 100), a letra x e um inteiro E (2 ≤ E ≤ 100), sendo C o coeficiente e E o expoente do termo. A entrada termina com fim de arquivo.

Saída
Para cada caso de teste, imprima o polinômio com a derivada aplicada.
'''

def derivada(pol):
    global resposta
    polinomio = pol.split(sep='x')
    parte_1 = int(polinomio[0]) * int(polinomio[1])
    parte_2 = int(polinomio[1])-1
    if parte_2 == 1:
        parte_2 = ''
    polinomio = str('{}x{}'.format(parte_1, parte_2))
    resposta.append(polinomio)

    
while True:
    try:
        qt_termos = int(input())
        pol = str(input()).split()
        for p in pol:
            if p == ' ' or p == '+':
                pol.remove(p)
        count = 0
        resposta = []
        for _ in range(qt_termos):
            derivada(pol[count])
            count += 1
        print(' + '.join(resposta))
    except EOFError:
        break