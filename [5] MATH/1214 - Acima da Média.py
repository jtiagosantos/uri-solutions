'''
Sabe-se que 90% dos calouros tem sempre a expectativa de serem acima da média no início de suas graduações. Você deve checar a realidade para ver se isso procede.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1214.jpg

Entrada
A entrada contém muitos casos de teste. A primeira linha da entrada contém um inteiro C, indicando o número de casos de teste. Seguem C casos de teste ou instâncias. Cada caso de teste inicia com um inteiro N, que é o número de pessoas de uma turma (1 ≤ N ≤ 1000). Seguem N inteiros, separados por espaços, cada um indicando a média final (um inteiro entre 0 e 100) de cada um dos estudantes desta turma.

Saída
Para cada caso de teste imprima uma linha dando o percentual de estudantes que estão acima da média da turma, com o valor arredondado e com 3 casas decimais.
'''

C = int(input())
for i in range(C):
    entrada = str(input()).split()
    for k,v in enumerate(entrada):
        entrada[k] = int(v)
    qt_alunos = entrada.pop(0)
    media = sum(entrada) / len(entrada)
    acima_media = 0
    for nota in entrada:
        if nota > media:
            acima_media += 1
    perc = (acima_media * 100) / qt_alunos
    print('{:.3f}%'.format(perc))
    