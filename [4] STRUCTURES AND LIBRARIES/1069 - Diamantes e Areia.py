'''
João está trabalhando em uma mina, tentando retirar o máximo que consegue de diamantes "<>". Ele deve excluir todas 
as particulas de areia "." do processo e a cada retirada de diamante, novos diamantes poderão se formar. Se ele tem 
como uma entrada .<...<<..>>....>....>>>., três diamantes são formados. O primeiro é retirado de <..>, resultando  
.<...<>....>....>>>. Em seguida o segundo diamante é retirado, restando .<.......>....>>>. O terceiro diamante é 
então retirado, restando no final .....>>>., sem possibilidade de extração de novo diamante.

Entrada
Deve ser lido um valor inteiro N que representa a quantidade de casos de teste. Cada linha a seguir é um caso de 
teste que contém até 1000 caracteres, incluindo "<,>, ."

Saída
Você deve imprimir a quantidade de diamantes possíveis de serem extraídos em cada caso de entrada.
'''

def count_diamante(array):
    count = 0; i = 0 
    while True:
        if array.count('<') == len(array) or array.count('>') == len(array) or array == [] or i == len(array) - 1:
            break
        if array[i] == '<' and array[i+1] == '>':
            del array[i]
            del array[i]
            count += 1
            i = -1
        i += 1
    
    return count


N = int(input())
for _ in range(N):
    diamantes = list(str(input()))
    diamantes = [i for i in diamantes if i in '<>']
    num_diamante = count_diamante(diamantes)
    print(num_diamante)