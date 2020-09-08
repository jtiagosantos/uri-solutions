'''
No Instituto Federal do Sul de Minas, na cidade de Muzambinho, há um matemático realizando uma pesquisa maluca. 
Ele está prestes a encontrar a fórmula da juventude. Depois de vários testes ele descobriu dados que o deixaram 
maluco, um deles foi que: quanto mais você coda mais ele rejuvenesce. Por enquanto a fórmula está em desenvolvimento 
e ele te contratou para ajudá-lo na pesquisa, pois após tanto trabalho esqueceu-se de alguns princípios da matemática, 
como metade da tabuada, e pediu para você construir a tabuada com os números que ele precisa. 

Entrada
O primeiro número N é um inteiro indicando quantas vezes seu programa será testado. Em seguida mais dois inteiros X e Y que serão os números a ser multiplicados.

Saída
Seu programa deve exibir a multiplicação dos dois números, exceto quando forem iguais, nesse caso sem os "&&".
'''

N = int(input())
for _ in range(N):
    entrada = input().split(sep='x')
    X = int(entrada[0])
    Y = int(entrada[1])
    for i in range(5, 11):
        if X == Y:
            print('{} x {} = {}'.format(X, i, X*i))
        else:
            print('{} x {} = {} && {} x {} = {}'.format(X, i, X*i, Y, i, Y*i))