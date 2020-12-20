'''
Todo ano, Papai Noel faz o recrutamento de elfos e gnomos para a sua equipe de preparação natalina. O setor de sua produção que mais tem alterações ao longo do ano é o da fabricação dos presentes, pois ele contrata elfos temporários, que trabalham uma determinada quantidade de horas H com ele. Além disso, cada elfo é contratado para um dos 4 diferentes grupos de trabalho, onde cada um dos grupos possui uma quantidade de horas para produzir os presentes do tipo do grupo:

    * Grupo dos bonecos: 8 horas;
    * Grupo dos arquitetos: 4 horas;
    * Grupo dos musicos: 6 horas;
    * Grupo dos desenhistas: 12 horas.
    
Note que os trabalhadores do grupo dos bonecos só produzem bonecos, o dos arquitetos, casas, e assim sucessivamente. Mas cada tipo de presente conta como um presente completo no final do dia.

O Papai Noel possui uma lista dos nomes dos elfos escolhidos esse ano, com a quantidade de horas e em que grupo que eles podem trabalhar. Sabendo da sua habilidade com programação, o Noel quer uma forcinha sua para dizer para ele quantos presentes ele vai conseguir ter pronto, por dia, de acordo com a quantidade de elfos que ele contratou.

Entrada
O primeiro valor da entrada é um valor inteiro N (1 ≤ N ≤ 1000), indicando a quantidade de elfos que o Papai Noel contratou. As N linhas seguintes possuem três valores E, G e H (1 ≤ H ≤ 24), indicando respectivamente o nome do elfo, em qual grupo ele vai trabalhar (em letras minúsculas) e quantas horas por dia ele irá ajudar (em valor inteiro).

Saída
A saída deverá ser um inteiro P, a quantidade total de presentes produzida por dia pela fábrica do Papai Noel.
'''

h_bonecos = h_arquitetos = h_musicos = h_desenhistas = qt_brinquedo = 0

n = int(input())

for _ in range(n):
    entrada = input().split()
    if entrada[1] == 'bonecos':
        h_bonecos += int(entrada[2])
    elif entrada[1] ==  'arquitetos':
        h_arquitetos += int(entrada[2])
    elif entrada[1] == 'musicos':
        h_musicos += int(entrada[2])
    elif entrada[1] == 'desenhistas':
        h_desenhistas += int(entrada[2])

while h_bonecos >= 8:
    h_bonecos -= 8
    qt_brinquedo += 1

while h_arquitetos >= 4:
    h_arquitetos -= 4
    qt_brinquedo += 1

while h_musicos >= 6:
    h_musicos -= 6
    qt_brinquedo += 1

while h_desenhistas >= 12:
    h_desenhistas -= 12
    qt_brinquedo += 1

print(qt_brinquedo)