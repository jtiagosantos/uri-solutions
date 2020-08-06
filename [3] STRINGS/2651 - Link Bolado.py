'''
Link é um herói famoso e por isso recebe diversas cartas de seus fãs. Porém mesmo sendo famoso, todos continuam o chamando de Zelda.

Por causa disso Link está muito bolado, tão bolado que sempre que recebe uma carta ele confere como o seu fã se referiu a ele na carta, e caso ele perceba o trecho "zelda" no nome ele fica bolado e joga a carta fora.

Sua tarefa é determinar se Link ficará bolado com a forma que seu fã o chamou na carta ou não.

Entrada
Contém uma string S (1 ≤ |S| ≤ 105) que representa como o fã de Link se referiu a ele na carta. A string é composta apenas por letras maiúsculas e minúsculas.

Saída
Seu programa deve exibir "Link Bolado" caso o nome contenha o trecho "zelda" ou "Link Tranquilo" caso contrário.
'''

nome_odiado = 'zelda'
string = str(input()).lower()
if nome_odiado in string:
    print('Link Bolado')
else:
    print('Link Tranquilo')