'''
O seu professor gostaria de fazer um programa com as seguintes características:

Leia uma frase que vai ter uma virgula no meio do texto;
Imprima a primeira parte da frase;
Imprima a segunda parte da frase.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem uma frase com no máximo 100 caracteres (pode ter espaço em branco) e uma virgula. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem duas linhas conforme os passos 2 e 3. Conforme mostra o exemplo de saída a seguir.
'''

string = str(input()).split(sep=',')
print(string[0])
print(string[1])