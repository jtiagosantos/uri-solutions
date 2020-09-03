'''
Após uma aula muito boa de história - sucedendo uma aula muito ruim de matemática - alguns alunos de uma determinada escola 
estão com dúvidas em um simples problema. A professora pediu que eles informassem o valor numérico (por simplicidade deve 
ser em decimal e em algarismos arábicos) do século de um determinado ano, mas como poucos alunos estavam acertando ela decidiu 
pedir sua ajuda para criar um programa que fizesse exatamente isso a fins educativos.

Para quem não se lembra desta aula de história, o século 1, por exemplo, compreende os anos entre 1 e 100, o século 2 os 
anos entre 101 e 200, o século 3 os anos entre 201 e 300 e assim por diante.  

Entrada
A entrada consiste em vários casos de teste e é terminada pelo final de arquivo (EOF). Cada linha é um novo caso de teste e 
contém um único inteiro N (1 ≤ N ≤ 109), que corresponde ao valor de algum ano que deve ser processado.

Saída
Para cada caso de teste, imprima uma única linha contendo o valor do século do ano correspondente.
'''

def seculo(ano):
    if ano < 100:
        return 1
    ano = list(str(ano))
    anocopy = ano.copy()
    final = anocopy[-2:]
    del ano[-2:]
    ano = int(''.join(ano))
    if final[0] == final[1] == '0':
        return ano
    return ano + 1


while True:
    try:
        ano = int(input())
        sec = seculo(ano)
        print(sec)
    except EOFError:
        break