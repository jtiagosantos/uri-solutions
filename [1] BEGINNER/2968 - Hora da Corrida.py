'''
Vinicius leva muito a sério seu condicionamento físico e, diariamente às 6h da manhã, chova ou faça sol, no verão e no inverno, ele corre no entorno de uma lagoa. Ao longo da pista de corrida existem N placas igualmente espaçadas. Para não desanimar do exercício, Vinicius conta o número de placas pelas quais ele já passou e verifica se ele já correu pelo menos 10%, pelo menos 20%, : : : , pelo menos 90% do percurso.

Vamos ajudar o Vinicius, calculando para ele o número de placas que ele precisa contar para ter completado pelo menos 10%, 20%, : : : , 90% da corrida, dados o número de voltas que ele pretende correr e o número total de placas ao longo da pista.

Por exemplo, suponhamos que Vinicius queira dar 3 voltas e o número de placas seja 17. Então, para garantir ter corrido pelo menos 30% do percurso, ele precisa contar 16 placas. Para garantir pelo menos 60%, ele precisa contar 31 placas.

Entrada
A entrada consiste de uma única linha que contém dois inteiros, V e N (1 ≤ V;N ≤ 104), onde V é o número pretendido de voltas e N é o número de placas na pista.

Saída
Seu programa deve produzir uma única linha com nove inteiros representando os números de placas que devem ser contadas para garantir o cumprimento, respectivamente, de 10%, 20%, : : : , 90% da meta.
'''

from math import ceil
valores = str(input()).split()
V = int(valores[0])
N = int(valores[1])
total_placas = V * N
metas = [0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90]
for i in metas[:8]:
    print(ceil(total_placas*i), end = ' ')
print(ceil(total_placas*metas[8]))