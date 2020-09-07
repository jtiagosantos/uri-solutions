'''
Seu irmão mais novo aprendeu a escrever apenas um, dois e três, em Inglês. Ele escreveu muitas dessas palavras em um papel e a 
sua tarefa é reconhecê-las. Nota-se que o seu irmão mais novo é apenas uma criança, então ele pode fazer pequenos erros: para 
cada palavra, pode haver, no máximo, uma letra errada. O comprimento de palavra é sempre correto. É garantido que cada palavra 
que ele escreveu é em letras minúsculas, e cada palavra que ele escreveu tem uma interpretação única.

Entrada
A primeira linha contém o número de palavras que o seu irmão mais novo escreveu. Cada uma das linhas seguintes contém uma única 
palavra com todas as letras em minúsculo. As palavras satisfazem as restrições acima: no máximo uma letra poderia estar errada, 
mas o comprimento da palavra está sempre correto. Haverá, no máximo, 1000 palavras de entrada.

Saída
Para cada caso de teste, imprima o valor numérico da palavra.
'''

num_teste = int(input())
for _  in range(num_teste):
    palavra = input()
    
    condicoes_one = [
        'ne' in palavra,
        'on' in palavra,
        'o' in palavra[0] and 'e' in palavra[2]
        ]
    
    condicoes_two = [
        'wo' in palavra,
        'tw' in palavra,
        't' in palavra[0] and 'o' in palavra[2]
        ]
    
    condicoes_three = [
        'hree' in palavra,
        'thre' in palavra,
        're' in palavra[1:-1],
        'hr' in palavra[1:-1],
        'h' in palavra[1:-1][0] and 'e' in palavra[1:-1][2]
    ]

    if any(condicoes_one):
        print(1)
    if any(condicoes_two):
        print(2)
    if any(condicoes_three):
        print(3)