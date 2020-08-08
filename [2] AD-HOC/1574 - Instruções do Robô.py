'''
Você possui um robô na origem do eixo x. O robô receberá algumas instruções. Sua tarefa é predizer sua posição depois de executar todas as instruções.

    * LEFT: move uma unidade para a esquerda (diminui p em 1, onde p é a posição do robô antes de mover)
    * RIGHT: move uma unidade para a direita (incrementa p em 1)
    *SAME AS i: executa a mesma ação que na i-ésima instrução. É garantido que i é um inteiro positivo não maior que o número de instruções já executadas.

Entrada
A primeira linha contém o número de casos de testes T (T <= 100). Cada caso de teste inicia com um inteiro n ( 1 <= n <= 100), o número de instruções. Cada uma das n linhas seguintes contém uma instrução.

Saída
Para cada caso de teste, imprima a posição final do robô. Note que após processar cada caso de teste, o robô deve ter sua posição inicial resetada para a origem.
'''

T = int(input())
for t in range(T):
    pos_inicial = 0
    instrucoes = []
    num_ins = int(input())
    for i in range(num_ins):
        ins = str(input()).upper()
        if ins == 'RIGHT':
            pos_inicial += 1
            instrucoes.append('RIGHT')
        elif ins == 'LEFT':
            pos_inicial -= 1
            instrucoes.append('LEFT')
        elif 'SAME AS ' in ins:
            ins = ins.split()
            pos = int(ins[2])
            mover = instrucoes[pos-1]
            if mover == 'RIGHT':
                pos_inicial += 1
                instrucoes.append('RIGHT')
            elif mover == 'LEFT':
                pos_inicial -= 1
                instrucoes.append('LEFT')
    print(pos_inicial)
