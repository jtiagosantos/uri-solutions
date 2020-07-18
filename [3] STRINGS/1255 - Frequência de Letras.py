'''
Neste problema estamos interessados na frequência das letras em uma dada linha de texto.

Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência do texto, ignorando o “case sensitive”, ou seja maiúsculas ou minúsculas (sendo mais claro, “letras” referem-se precisamente às 26 letras do alfabeto).

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1255.png

Entrada
A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de uma única linha de texto. A linha pode conter caracteres “não letras”, mas é garantido que tenha ao menos uma letra e que tenha no máximo 200 caracteres no total.

Saída
Para cada caso de teste, imprima uma linha contendo a(s) letra(s) que mais ocorreu(ocorreram) no texto em minúsculas (se houver empate, imprima as letras em ordem alfabética).
'''

caracteres = 'abcdefghijklmnopqrstuvwxyz'

N = int(input())
for c in range(N):
    texto = str(input()).lower()
    qt_letras = []
    letras_lidas = []
    resultado = []
    for t in texto:
        if t in caracteres:
            if not t in letras_lidas:
                letras_lidas.append(t)
                qt_letras.append(texto.count(t))
    for i in texto:
        if texto.count(i) == max(qt_letras):
            if not i in resultado:
                resultado.append(i)
    resultado = sorted(resultado)
    print(''.join(resultado).strip())