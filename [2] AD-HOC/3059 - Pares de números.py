'''
Temos um vetor de N inteiros distintos e dois inteiros I e F. Precisamos computar quantos pares desses inteiros do vetor somam pelo menos I e no máximo F. Por exemplo, se o vetor for [45, 12, 11, 7, 83, 29, 5] e I = 19 e F = 52, temos exatamente 8 pares cuja soma está entre 19 e 52: {5, 29}, {5, 45}, {7, 12}, {7, 29}, {7, 45}, {11, 12}, {11, 29} e {12, 29}.

Entrada
A primeira linha da entrada contém três inteiros N, I e F, indicando respectivamente o tamanho do vetor e o valor mínimo da soma e o valor máximo da soma.

Saída
Seu programa deve imprimir uma única linha contendo um inteiro indicando quantos pares de inteiros no vetor somam pelo menos I e no máximo F.

Restrições
• 2 ≤ N ≤ 1000
• −2000 ≤ I, F ≤ 2000
• O valor de cada inteiro no vetor está entre −1000 e 1000
• Os inteiros no vetor são distintos
'''

entrada = str(input()).split()
tam_vetor = int(entrada[0])
valor_min = int(entrada[1])
valor_max = int(entrada[2])
vetor = str(input()).split()
for k,v in enumerate(vetor):
    vetor[k] = int(v)
count = 0
for a in vetor:
    for b in vetor:
        if a != b and valor_min <= a + b <= valor_max:
            count += 1
print(int(count/2))