'''
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.
'''

num_grenal = emp = vit_inter = vit_gremio = 0
while True:
    valores = str(input()).split()
    gol_inter = int(valores[0])
    gol_gremio = int(valores[1])
    num_grenal += 1
    if gol_inter > gol_gremio:
        vit_inter += 1
    elif gol_gremio > gol_inter:
        vit_gremio += 1
    elif gol_gremio == gol_inter:
        emp += 1
    print('Novo grenal (1-sim 2-nao)')
    perg = int(input())
    if perg == 2:
        break
print('{} grenais'.format(num_grenal))
print('Inter:{}'.format(vit_inter))
print('Gremio:{}'.format(vit_gremio))
print('Empates:{}'.format(emp))
if vit_inter > vit_gremio:
    print('Inter venceu mais')
elif vit_gremio > vit_inter:
    print('Gremio venceu mais')
elif vit_gremio == vit_inter:
    print('Nao houve vencedor')