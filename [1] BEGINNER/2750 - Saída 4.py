'''
O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Criar 16 variáveis inteiras;
Atribuir a elas valores de 0 a 15 a cada um das variáveis anteriores;
Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 4o traço deve começar a escrever “decimal”, embaixo do 16o traço deve começar a escrever “octal”, embaixo do 26o traço deve começar a escrever “Hexadecimal” e o restante preencher com espaço em branco;
Repita o procedimento 1;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 8o traço deve imprimir o valor da primeira variável em valor decimal, embaixo do 18o traço deve imprimir o valor da primeira variável em valor octal, embaixo do 31o traço deve imprimir o valor da primeira variável em valor hexadecimal e o restante preencher com espaço em branco;
Repita o procedimento 6 para as outras 15 variáveis;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
| decimal   |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
--------------------------------------- (39 traços)
Entrada
Não há.

Saída
A saída será impressa conforme a figura acima.
'''

print('-'*39)
print('|  decimal  |  octal  |  Hexadecimal  |')
print('-'*39)
i = 0
for _ in range(8):
    print('|      {}    |    {}    |       {}       |'.format(i,i,i))
    i += 1
print('|      8    |   10    |       8       |')
print('|      9    |   11    |       9       |')
print('|     10    |   12    |       A       |')
print('|     11    |   13    |       B       |')
print('|     12    |   14    |       C       |')
print('|     13    |   15    |       D       |')
print('|     14    |   16    |       E       |')
print('|     15    |   17    |       F       |')
print('-'*39)