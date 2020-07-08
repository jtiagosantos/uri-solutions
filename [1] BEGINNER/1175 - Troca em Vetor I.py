'''
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.
'''

vetor_N = []
for i in range(20):
    num = int(input())
    vetor_N.append(num)
cont = -1
for i,Y in enumerate(vetor_N):
    print('N[{}] = {}'.format(i,vetor_N[cont]))
    cont -= 1