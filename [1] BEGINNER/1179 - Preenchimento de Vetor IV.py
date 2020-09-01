'''
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. 
Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você 
deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, 
deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. 
Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.
'''

pares = []
impares = []

for _ in range(15):
    num = int(input())
    pares.append(num) if num % 2 == 0 else impares.append(num)
    if len(pares) == 5:
        for k,v in enumerate(pares):
            print('par[{}] = {}'.format(k,v))
        pares = []
    if len(impares) == 5:
        for k,v in enumerate(impares):
            print('impar[{}] = {}'.format(k,v))
        impares = []
        
for k,v in enumerate(impares):
    print('impar[{}] = {}'.format(k,v))
    
for k,v in enumerate(pares):
    print('par[{}] = {}'.format(k,v))
        
