'''
O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Crie vinte e seis variáveis inteira;
Atribua a primeira variável o valor 97;
Atribua as outras demais variável o valor da primeira somado de uma unidade;
Mostre na tela os valores numéricos da primeira variável, um espaço em braco, o carácter 'e', outro espaço em branco e o seu valor alfanumérico (caracteres);
Repita o procedimento para todas as outras variáveis.
Entrada
Não há.

Saída
O resultado de seu programa deve ser o mesmo do exemplo de saída.
'''

variaveis = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z'
    ]

num = 97
for i in range(len(variaveis)):
    print('{} e {}'.format(num, variaveis[i]))
    num +=1 
