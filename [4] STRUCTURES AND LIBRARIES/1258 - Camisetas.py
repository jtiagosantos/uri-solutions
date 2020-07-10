'''
O professor Rolien organizou junto às suas turmas de Ciência da Computação a confecção de uma camiseta polo que fosse ao mesmo tempo bonita e barata. Após algumas conversas, ficou decidido com os alunos que seriam feitas somente camisetas da cor preta, o que facilitaria a confecção. Os alunos poderiam escolher entre o logo do curso e os detalhes em branco ou vermelho. Assim sendo, Rolien precisa de sua ajuda para organizar as listas de quem quer a camiseta em cada uma das turmas, relacionando estas camisetas pela cor do logo do curso, tamanho (P, M ou G) e por último pelo nome.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1258.png

Entrada
A entrada contém vários casos de teste. Cada caso de teste inicia com um valor N, (1 ≤ N ≤ 60) inteiro e positivo, que indica a quantidade de camisetas a serem feitas para aquela turma. As próximas N*2 linhas contém informações de cada uma das camisetas (serão duas linhas de informação para cada camiseta). A primeira linha irá conter o nome do estudante e a segunda linha irá conter a cor do logo da camiseta ("branco" ou "vermelho") seguido por um espaço e pelo tamanho da camiseta "P" "M" ou "G". A entrada termina quando o valor de N for igual a zero (0) e esta valor não deverá ser processado.

Saída
Para cada caso de entrada deverão ser impressas as informações ordenadas pela cor dos detalhes em ordem ascendente, seguido pelos tamanhos em ordem descendente e por último por ordem ascendente de nome, conforme o exemplo abaixo.

Obs.: Deverá ser impressa uma linha em branco entre dois casos de teste.
'''

count = 0
while True:
    N = int(input())
    if N == 0:
        break
    dados_vermelho = []
    dados_branco = []
    estudante = []
    for i in range(N):
        nome = str(input())
        cor_tam = str(input()).split()
        cor = cor_tam[0]
        tam = cor_tam[1]
        estudante.append(cor)
        estudante.append(tam)
        estudante.append(nome)
        if cor == 'vermelho':
            dados_vermelho.append(estudante)
        if cor == 'branco':
            dados_branco.append(estudante)
        estudante = []
        
    dados_branco.sort()
    dados_vermelho.sort()

    if count >= 1:
        print()

    for x in dados_branco:
        if 'P' in x:
            print('{} {} {}'.format(x[0], x[1], x[2]))
    for y in dados_branco:
        if 'M' in y:
            print('{} {} {}'.format(y[0], y[1], y[2]))
    for z in dados_branco:
        if 'G' in z:
            print('{} {} {}'.format(z[0], z[1], z[2]))

    for a in dados_vermelho:
        if 'P' in a:
            print('{} {} {}'.format(a[0], a[1], a[2]))
    for b in dados_vermelho:
        if 'M' in b:
            print('{} {} {}'.format(b[0], b[1], b[2]))
    for c in dados_vermelho:
        if 'G' in c:
            print('{} {} {}'.format(c[0], c[1], c[2]))
    count += 1
