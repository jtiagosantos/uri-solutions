'''
O seu professor gostaria de fazer um programa com as seguintes características:

    1. Crie 3 variáveis para armazenar um único carácter;
    2. Leia um valor carácter para a primeira variável;
    3. Leia um valor carácter para a segunda variável;
    4. Leia um valor carácter para a terceira variável;
    5. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 2, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 3, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 4. Não esqueça de pular linha;
    6. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 4, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 2. Não esqueça de pular linha;
    7. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 4, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 2, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 3. Não esqueça de pular linha.

Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem uma variável A que armazena um valor carácter. Na segunda linha tem uma variável B que armazena um valor carácter. Na terceira linha tem uma variável C que armazena um valor carácter. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas da forma descrita nos itens 5, 6 e 7. Conforme mostra o exemplo de saída a seguir.
'''

A = str(input())
B = str(input())
C = str(input())

lista_1 = []
lista_2 = []
lista_3 = []

lista_1.append(A)
lista_1.append(B)
lista_1.append(C)

lista_2.append(B)
lista_2.append(C)
lista_2.append(A)

lista_3.append(C)
lista_3.append(A)
lista_3.append(B)

for a,b,c in zip(lista_1, lista_2, lista_3):
    print('A = {}, B = {}, C = {}'.format(a,b,c))