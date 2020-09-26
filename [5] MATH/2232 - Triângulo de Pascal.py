'''
O triângulo de Pascal (alguns países, nomeadamente em França, é conhecido como Triângulo de Tartaglia) é um triângulo numérico 
infinito formado por números binomiais (https://www.urionlinejudge.com.br/gallery/images/contests/UOJ_2232_b.png), onde n 
representa o número da linha e k representa o número da coluna, iniciando a contagem a partir do zero. O triângulo foi descoberto 
pelo matemático chinês Yang Hui, e 500 anos depois várias de suas propriedades foram estudadas pelo francês Blaise Pascal. 
Cada número do triângulo de Pascal é igual à soma do número imediatamente acima e do antecessor do número de cima.

https://www.urionlinejudge.com.br/gallery/images/contests/UOJ_2232_a.png

David, o fera do seu time de programação competitiva, descobriu que a soma da i-ésima linha de um triângulo de pascal é 2i. 
Ele quer agora descobrir a soma do triângulo inteiro, de N linhas. Mas como ele achou que este problema era muito trivial para 
merecer a atenção dele, ele decidiu tentar resolver um problema sobre grafos bipartidos (um tópico muito mais difícil) e assim, 
sobrou para você encontrar a solução deste problema.

Entrada
A primeira linha da entrada contém um inteiro T, o número de casos de teste. As próximas T linhas contêm um inteiro N (1 ≤ N ≤ 31), 
o número de linhas do Triângulo de Pascal.

Saída
Para cada caso de teste, a saída deve conter uma linha com um inteiro S, a soma do triângulo de pascal de N linhas.
'''

t = int(input())
for _ in range(t):
    n = int(input())
    s = sum([2**i for i in range(0, n)])
    print(s)