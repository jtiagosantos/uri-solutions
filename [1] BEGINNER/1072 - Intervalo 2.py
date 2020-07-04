'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.
'''

valores = []
dentro_inter = fora_inter = 0
N = int(input())
for i in range(N):
    num = int(input())
    valores.append(num)
for i in valores:
    if i >= 10 and i <= 20:
        dentro_inter += 1
    else:
        fora_inter += 1
print('{} in'.format(dentro_inter))
print('{} out'.format(fora_inter))
