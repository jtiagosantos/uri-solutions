'''
Júlio está criando um novo Smart Watch especialmente para programadores. É impressionante as vantagens que ele oferece e 
o conforto pra codar que ele tem. O relógio ainda está em desenvolvimento e ele prometeu consertar os bugs e colocar uns 
apetrechos melhores e, em troca, pediu um sistema simples para o modo Standy Bay. O problema é que o relógio por si só 
sempre tem o ângulo de inclinação do Sol/Lua(de 0 a 360). Valendo um relógio, caso deseja aceitar: dada em grau da inclinação 
do Sol/Lua, informe em qual período do dia ele se encontra.

https://www.urionlinejudge.com.br/gallery/images/problems/UOJ_2686.png

Entrada
A entrada contém um número inteiro M (0 ≤ M ≤ 360) representando o grau do Sol/Lua. Como a posição muda constantemente seu 
programa receberá diversos casos a cada segundo(EOF).

Saída
Imprima uma saudação referente ao período do dia que ele se encontra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e 
"De Madrugada!!".
'''

def saudacao(grau):
    if grau == 360:
        return 'Bom Dia!!'
    elif grau >= 0 and grau < 90:
        return 'Bom Dia!!'
    elif grau >= 90 and grau < 180:
        return 'Boa Tarde!!'
    elif grau >= 180 and grau < 270:
        return 'Boa Noite!!'
    elif grau >= 270 and grau < 360:
        return 'De Madrugada!!'


while True:
    try:
        grau = int(input())
        string = saudacao(grau)
        print(string)
    except EOFError:
        break