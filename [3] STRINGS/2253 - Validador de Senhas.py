'''
Rolien e Naej são os desenvolvedores de um grande portal de programação. Para ajudar no novo sistema de cadastro do site, eles requisitaram a sua ajuda. Seu trabalho é fazer um código que valide as senhas que são cadastradas no portal, para isso você deve atentar aos requisitos a seguir:

A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
Além disso, a senha pode ter de 6 a 32 caracteres.
Entrada
A entrada contém vários casos de teste e termina com final de arquivo. Cada linha tem uma string S, correspondente a senha que é inserida pelo usuário no momento do cadastro.

Saída
A saída contém uma linha, que pode ser “Senha valida.”, caso a senha tenha cada item dos requisitos solicitados anteriormente, ou “Senha invalida.”, se um ou mais requisitos não forem atendidos.
'''

while True:
    try:
        maiuscula = minuscula = numero = valida = espaco = 0
        senha = str(input())
        if senha.isalnum():
            senha = list(senha)
            for s in senha:
                if s.isupper():
                    maiuscula += 1
                if s.lower():
                    minuscula += 1
                if s.isdigit():
                    numero += 1
                if s == ' ':
                    espaco += 1
            if maiuscula > 0 and minuscula > 0 and numero > 0 and 6 <= len(senha) <= 32 and espaco == 0:
                valida += 1
        if valida > 0:
            print('Senha valida.')
        else:
            print('Senha invalida.')
            
    except EOFError:
        break