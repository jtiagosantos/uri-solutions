'''
Dada uma letra do alfabeto, informe qual a sua posição.

Entrada
Um único caracter L, uma letra maiúscula ('A'-'Z') do alfabeto.

Saída
Um único inteiro, que representa a posição da letra no alfabeto.
'''

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z'
    ]
letra = input().upper()
print(alfabeto.index(letra) + 1)
