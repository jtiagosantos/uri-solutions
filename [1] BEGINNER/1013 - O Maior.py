'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png" alt="Greatest Formula">


Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

valores = str(input()).split()
A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
maiorAB = int((A + B + abs(A - B))/2)
if maiorAB > C:
    print('{} eh o maior'.format(maiorAB))
else:
    print('{} eh o maior'.format(C))