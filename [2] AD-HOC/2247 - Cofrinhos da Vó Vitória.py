'''
Vó Vitória mantém, desde o nascimento dos netos Joãozinho e Zezinho, um ritual que faz a alegria dos meninos. Ela guarda todas as moedas recebidas como troco em dois pequenos cofrinhos, um para cada neto. Quando um dos cofrinhos fica cheio, ela chama os dois netos para um alegre almoço, ao final do qual entrega aos garotos as moedas guardadas nos cofrinhos de cada um.
Ela sempre foi muito zelosa quanto à distribuição igualitária do troco arrecadado. Quando, por força do valor das moedas, ela não consegue depositar a mesma quantia nos dois cofrinhos, ela memoriza a diferença de forma a compensá-la no próximo depósito.
Vó Vitória está ficando velha e tem medo que deslizes de memória a façam cometer injustiças com os netos, deixando de compensar as diferenças entre os cofrinhos. Sua tarefa é ajudar Vó Vitória, escrevendo um programa de computador que indique as diferenças entre os depósitos, de forma que ela não tenha que preocupar-se em memorizá-las.

Entrada
A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de teste contém um número inteiro N (0 ≤ N ≤ 100), que indica o número de depósitos nos cofrinhos. As N linhas seguintes descrevem cada uma um depósito nos cofrinhos; o depósito é indicado por dois valores inteiros J e Z (0 ≤ J,Z ≤ 100), separados por um espaço em branco, representando respectivamente
os valores, em centavos, depositados nos cofres de Joãozinho e Zezinho. O final da entrada é indicado por N = 0.

Saída
Para cada conjunto de teste da entrada seu programa deve produzir um conjunto de linhas na saída. A primeira linha deve conter um identificador do conjunto de teste, no formato “Teste n”, onde n é numerado seqüencialmente a partir de 1. A seguir seu programa deve escrever uma linha para cada depósito do conjunto de testes. Cada linha deve conter um inteiro que representa a diferença 
(em centavos) entre o valor depositado nos cofrinhos do Joãozinho e do Zezinho. Deixe uma linha em branco ao final de cada conjunto de teste. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.
'''

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    dif = dif_tt = 0
    saidas = []
    for _ in range(n):
        valores = list(map(int, input().split()))
        j = valores[0]
        z = valores[1]
        dif = j - z
        dif_tt += dif
        saidas.append(dif_tt)
    print(f'Teste {count}')
    for i in saidas:
        print(i)
    count += 1
    print('')