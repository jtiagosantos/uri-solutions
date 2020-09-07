'''
Pedra-papel-tesoura-lagarto-Spock é uma expansão do clássico método de seleção em jogo de pedra-papel-tesoura. Atua sob o mesmo 
princípio básico, mas inclui outras duas armas adicionais: o lagarto (formado pela mão igual a uma boca de fantoche) e Spock 
(formada pela saudação dos vulcanos em Star Trek). Isso reduz as chances de uma rodada terminar em um empate. O jogo foi 
inventado por Sam Kass e Karen Bryla, como "Rock Paper Scissors Lizard Spock". As regras de vantagem são as seguintes:

    * Tesoura corta papel
    * Papel cobre pedra
    * Pedra derruba lagarto
    * Lagarto adormece Spock
    * Spock derrete tesoura
    * Tesoura prende lagarto
    * Lagarto come papel
    * Papel refuta Spock
    * Spock vaporiza pedra
    * Pedra quebra tesoura

Um dia, dois amigos, Rajesh e Sheldon, decidiram apostar quem pagaria um almoço para o outro, com esta brincadeira. Sua missão 
será fazer um algoritmo que, baseado no que eles escolherem, informe quem irá ganhar ou se dará empate.

Entrada
Haverá diversos casos de teste. O primeiro número a ser lido será um inteiro C, representando a quantidade de casos de teste. 
Cada caso de teste tem duas palavras, representando a escolha de Rajesh e de Sheldon, respectivamente.

Saída
Para cada caso de teste, imprima quem venceu, ou se houve empate.
'''

C = int(input())
for _ in range(C):
    entrada = input().split()
    raj = entrada[0]
    sheldon = entrada[1]

    condicoes_raj = [
        raj == 'tesoura' and sheldon == 'papel',
        raj == 'papel' and sheldon == 'pedra',
        raj == 'pedra' and sheldon == 'lagarto',
        raj == 'lagarto' and sheldon == 'spock',
        raj == 'spock' and sheldon == 'tesoura',
        raj == 'tesoura' and sheldon == 'lagarto',
        raj == 'lagarto' and sheldon == 'papel',
        raj == 'papel' and sheldon == 'spock',
        raj == 'spock' and sheldon == 'pedra',
        raj == 'pedra' and sheldon == 'tesoura',
    ]

    condicoes_sheldon = [
        sheldon == 'tesoura' and raj == 'papel',
        sheldon == 'papel' and raj == 'pedra',
        sheldon == 'pedra' and raj == 'lagarto',
        sheldon == 'lagarto' and raj == 'spock',
        sheldon == 'spock' and raj == 'tesoura',
        sheldon == 'tesoura' and raj == 'lagarto',
        sheldon == 'lagarto' and raj == 'papel',
        sheldon == 'papel' and raj == 'spock',
        sheldon == 'spock' and raj == 'pedra',
        sheldon == 'pedra' and raj == 'tesoura',
    ]

    if any(condicoes_raj):
        print('rajesh')
    elif any(condicoes_sheldon):
        print('sheldon')
    else:
        print('empate')