'''
Frodo era um pequeno hobbit (pessoinhas pequenas e de pés peludos) que vivia tranquilamente no Condado, tomando seus vários cafés da manhã recheados de muitos alimentos suculentos que a dieta de um bom hobbit proporciona.
Certo dia, seu tio Bilbo lhe entrega seu famoso anel dourado, e Gandalf, um mago muito “bacanudo”, diz a Frodo que esse anel não era normal e que deveria ser jogado na Montanha da Perdição, para que um grande mal fosse evitado. Para essa jornada, foi formada uma comitiva, composta de anões, elfos, humanos, hobbits e magos.
Frodo deseja saber a quantidade de cada raça que irá com ele para a jornada. Dada uma lista das pessoas que se alistaram, faça um relatório para Frodo da comitiva.

Entrada
A primeira linha da entrada é composta por um inteiro N(0 < N <= 10), indicando o número de pessoas que se alistaram. Cada uma das próximas N linhas seguintes são compostas por uma cadeia de caracteres (sem espaços e de caracteres alfanuméricos apenas) e um caractere maiúsculo, indicando, respectivamente, o nome e o tipo da raça do respectivo ser. Este caractere poderá ser:
● A - Para anões;
● E - Para elfos;
● H - Para humanos;
● M - Para magos;
● X - Para hobbits (X, pois todo hobbit é uma incógnita para o mundo).
Saída
Deve ser apresentado um relatório com a comitiva do Frodo, indicando em cada linha quantos seres de cada espécie estarão na jornada, seguindo a ordem: hobbits, humanos, elfos, anões e magos.
'''

N = int(input())
tipos = []
anao = elfo = humano = mago = hobbit = 0
for i in range(N):
    entrada = str(input()).split()
    nome = entrada[0]
    tipo = entrada[1].upper()
    tipos.append(tipo)
for i in tipos:
    if i == 'A':
        anao += 1
    if i == 'E':
        elfo +=1 
    if i == 'H':
        humano +=1
    if i == 'M' :
        mago +=1
    if i == 'X':
        hobbit +=1
print('{} Hobbit(s)'.format(hobbit))
print('{} Humano(s)'.format(humano))
print('{} Elfo(s)'.format(elfo))
print('{} Anao(s)'.format(anao))
print('{} Mago(s)'.format(mago))
