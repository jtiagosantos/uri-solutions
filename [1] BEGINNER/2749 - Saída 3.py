'''
O seu professor de programação gostaria de fazer uma tela com as seguintes características:

Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 2o traço deve começar a escrever "x = 35" e o restante preencher com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 17o traço deve começar a escrever "x = 35" e o restante preencher com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, embaixo do 33o traço deve começar a escrever "x = 35" e o restante preencher no meio com espaço em branco;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)

|x = 35                               |

|                                     |

|                x = 35               |

|                                     |

|                               x = 35|

--------------------------------------- (39 traços)

Entrada
Não há.

Saída
A saída será impresso conforme a figura acima.
'''

def linha_hor():
    print('-' * 39)

def linha_vert():
    print('|{:>38}'.format('|'))

def linha_vert_1():
    print('|x = 35{:>32}'.format('|'))

def linha_vert_2():
    print('|{:>21}{:>17}'.format('x = 35', '|'))

def linha_vert_3():
    print('|{:>37}|'.format('x = 35'))

linha_hor()
linha_vert_1()
linha_vert()
linha_vert_2()
linha_vert()
linha_vert_3()
linha_hor()