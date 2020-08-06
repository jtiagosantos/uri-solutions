'''
Um novo conjunto de autenticação será implementado no Instituto Federal do Sul de Minas, campus Muzambinho.

Bom, o novo serviço de autenticação é seguro, sem bugs e dores de cabeça mesmo porque estamos no final de semestre. Ele permitirá que sua senha tenha espaços, mas não números ou caracteres especiais. A atualização ocorre sempre no período de férias, para que todos os ajustes sejam feitos e no final agrade todos os usuarios. Como estagiário da central de suporte da escola, seu dever é implementar a nova autenticação. Por enquanto o novo padrão para nomes de usuários está sendo estudado.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2690.jpg

Como podemos perceber para cada conjunto de letras teremos um numero especifico. Bole um programa maroto para fazer essa conversão das letras para os números, e como você não acessará as senhas dos alunos, faça um algoritmo para que o mesmo faça o processo sozinho usando seus proprios casos de teste.

Obs : Seus casos de teste não poderão passar de 20 caracterese e a saída, 12 digitos.

Entrada
Você terá N indicando a quantidade de senhas que serão trocadas, em seguida N casos de testes.

Saída
A saída será uma lista com os novos números, criptografados das senhas que foram digitadas.
'''

tabela = {
    'G':'0', 'Q':'0', 'a':'0', 'k':'0', 'u':'0', 'I':'1', 'S':'1', 'b':'1', 'l':'1',
    'v':'1', 'E':'2', 'O':'2', 'Y':'2', 'c':'2', 'm':'2', 'w':'2', 'F':'3', 'P':'3',  
    'Z':'3', 'd':'3', 'n':'3', 'x':'3', 'J':'4', 'T':'4', 'e':'4', 'o':'4', 'y':'4',
    'D':'5', 'N':'5', 'X':'5', 'f':'5', 'p':'5', 'z':'5', 'A':'6', 'K':'6', 'U':'6', 
    'g':'6', 'q':'6', 'C':'7', 'M':'7', 'W':'7', 'h':'7', 'r':'7', 'B':'8', 'L':'8', 
    'V':'8', 'i':'8', 's':'8', 'H':'9', 'R':'9', 'j':'9', 't':'9'
}

N = int(input())
for i in range(N):
    criptografia = ''
    senha = list(''.join(str(input())))
    for s in senha:
        if s in tabela.keys():
            criptografia += tabela[s]
    criptografia = list(criptografia)
    criptografia = criptografia[:12]
    print(''.join(criptografia))