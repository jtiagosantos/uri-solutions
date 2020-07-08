'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.
'''

valida = 0
notas = []
while True:
    nota = float(input())
    if nota >= 0.0 and nota <= 10.0:
        notas.append(nota)
        valida += 1
    else:
        print('nota invalida')
    if valida == 2:
        break
media = sum(notas) / len(notas)
print('media = {:.2f}'.format(media))