'''
O seu professor gostaria de fazer um programa com as seguintes características:

    1.Leia os dados de um CPF no formato XXX.YYY.ZZZ-DD;
    2.Imprima os quatro números, sendo um valor por linha.

Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem o seguinte formato XXX.YYY.ZZZ-DD, onde XXX, YYY, ZZZ, DD são números inteiros. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas com um número inteiro em cada uma delas, conforme foi entrado. Conforme mostra o exemplo de saída a seguir.
'''

cpf = str(input()).split(sep='.')
final = ''.join(cpf[-1]).split(sep='-')
del cpf[-1]
for c in cpf:
    print(c)
for f in final:
    print(f)
