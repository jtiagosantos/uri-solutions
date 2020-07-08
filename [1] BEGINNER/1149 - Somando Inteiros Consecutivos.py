'''
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.
'''

entrada = str(input()).split()
for k, v in enumerate(entrada):
    entrada[k] = int(v)
A = entrada.pop(0)
N = [i for i in entrada if i > 0]
N = N[0]

valores = []
for i in range(N):
    soma = A
    soma = soma + i
    valores.append(soma)
print(sum(valores))
