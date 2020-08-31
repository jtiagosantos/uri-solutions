'''
Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em conta o 
restante da expressão. Por exemplo:

a+(b*c)-2-a        está correto
(a+b*(2-c)-2+a)*2  está correto

enquanto

(a*b-(2+c)         está incorreto
2*(3-a))           está incorreto
)3+b*(2-c)(        está incorreto

Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parênteses que 
fecha sem um previo parenteses que abre e a quantidade total de parenteses que abre e fecha deve ser igual.

Entrada
Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as 
palavras correct ou incorrect de acordo com as regras acima fornecidas.
'''

def validador(array):
    arraycopy = array.copy()
    if len(array) % 2 != 0:
        return 'incorrect'
    else:
        count = 0; i = 0
        while True:
            if i == len(array) - 1 or array == []:
                break
            if array[i] == '(' and array[i+1] == ')':
                count += 1
                del array[i]
                del array[i]
                i = -1
            i += 1
        if count == len(arraycopy) / 2:
            return 'correct'
        else:
            return 'incorrect'
    

while True:
    try:
        expressao = list(str(input()))
        array = [i for i in expressao if i in '()']
        teste = validador(array)
        print(teste)

    except EOFError:
        break