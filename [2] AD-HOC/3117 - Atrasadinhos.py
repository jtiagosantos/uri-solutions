'''
Um professor ministrava certos treinamentos em uma universidade e estava descontente com o número de pessoas que chegavam atrasadas. 
Ele é muito rigoroso e detesta ser interrompido por conta de alunos atrasados. Como forma de reduzir a sua frustração, ele definiu a seguinte regra:

Para cada turma será definido um número mínimo de pessoas que devem estar na sala no horário marcado. Se esse número não for alcançado, o treinamento será cancelado.
Dado o número total de pessoas da turma, um número mínimo de pessoas que devem estar na sala e o tempo de chegada de cada um, determine se o treinamento irá acontecer 
ou não. Considere que, se o tempo de chegada de um aluno Ai > 0, o mesmo encontra-se atrasado.
 

Entrada
A primeira linha dos casos de teste consiste de dois inteiros N (1 <= N <= 106) e K (0 <= K <= 106), representando a quantidade de alunos e a quantidade mínima de pessoas, 
respectivamente. A linha seguinte é dada por N inteiros A1, A2, ..., An (-104 <= An <= 104), indicando o horário qua cada aluno chegará no treinamento.

Saída
Seu programa deve produzir uma única linha, contendo a palavra YES caso o treinamento ocorra ou NO, caso contrário.
'''

entrada = input().split()
minimo_alunos = int(entrada[1])
horarios = input().split()
horarios = [i for i in horarios if int(i) <= 0]

if len(horarios) >= minimo_alunos:
    print('YES')
else:
    print('NO')