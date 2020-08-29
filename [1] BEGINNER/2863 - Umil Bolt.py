'''
Umil Bolt é um excelente corredor. Sua especialidade é a prova dos 100 metros rasos. Todos os dias, ele faz uma bateria
de tentativas de correr esta prova em um tempo cada vez menor. Pode se perceber que, dependendo da quantidade de tentativas,
o seu desempenho melhora ou piora. Sobre isso, ele pede a sua ajuda para calcular a tentativa mais rápida de cada bateria diária.

Entrada
A entrada é composta por vários casos de teste. A primeira linha de cada caso de teste contém um número inteiro 
T (2 <= T <= 99) relativo ao número de tentativas de um dia. As T linhas seguintes contêm um número real Ti (9 <= Ti <= 11)
relativo ao tempo, em segundos, da i-ésima tentativa da bateria. A entrada termina com fim de arquivo.

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número real contendo o tempo da tentativa mais 
rápida de cada bateria.
'''

def best_time(times):
    return min(times)
    
    
while True:
    times = []
    try:
        T = int(input())
        for _ in range(T):
            times.append(float(input()))
        time = best_time(times)
        print(time)
    except EOFError:
        break