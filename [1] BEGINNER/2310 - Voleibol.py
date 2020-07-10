'''
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

Entrada
A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo nome de cada um dos jogadores. Abaixo do nome de cada jogador, seguem duas linhas com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) representam a quantidade de tentativas de saques, bloqueios e ataques e na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

Saída
A saída deve conter o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.
'''

N = int(input())
total_s = total_b = total_a = 0
sucess_s = sucess_b = sucess_a = 0
for i in range(N):
    nome = str(input())
    #Quantidade de tentativas:
    entrada_1 = str(input()).split()
    S = int(entrada_1[0])
    B = int(entrada_1[1])
    A = int(entrada_1[2])
    
    #Quantidade de tentativas com sucesso:
    entrada_2 = str(input()).split()
    S1 = int(entrada_2[0])
    B1 = int(entrada_2[1])
    A1 = int(entrada_2[2])
    
    total_s += S
    sucess_s += S1
    
    total_b += B
    sucess_b += B1
    
    total_a += A
    sucess_a += A1
    
perc_s = (100 * sucess_s) / total_s
perc_b = (100 * sucess_b) / total_b
perc_a = (100 * sucess_a) / total_a

print('Pontos de Saque: {:.2f} %.'.format(perc_s))
print('Pontos de Bloqueio: {:.2f} %.'.format(perc_b))
print('Pontos de Ataque: {:.2f} %.'.format(perc_a))

