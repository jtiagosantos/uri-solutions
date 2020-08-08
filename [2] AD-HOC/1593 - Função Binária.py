'''
Definimos a paridade de um inteiro como a soma dos seus bits em sua representação binária computada módulo dois. Como exemplo, o número 2110 = 101012 possui três 1’s na sua representação binária e portanto ele teria paridade ímpar.

Neste problema, você deverá calcular o número de bits 1 em um inteiro I dado, ou seja, calcular a quantidade de 1’s na representação binária dele.
Entrada
Na primeira linha terá um inteiro T (T <= 100) indicando o número de casos de teste.

Para cada caso, haverá apenas uma linha com o número I (1 ≤ I < 1018* ou 1 ≤ I < 101000**).O número da entrada não começará com um ou mais zeros.
*ocorrerá em 90% dos casos;
**ocorrerá nos casos restantes.

Saída
Imprima o número de 1’s na representação binária para cada caso em uma única linha.
'''

T = int(input())
for t in range(T):
    num = list(bin(int(input())))
    print(num.count('1'))