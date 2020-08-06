'''
Um grupo de alunos decidiu organizar a GCC (Grande Competição de Códigos), que será, obviamente, a maior competição de códigos do mundo. Há N universidades que podem mandar seus alunos para participar na GCC, na forma de times de três alunos. Os organizadores da GCC querem saber: assumindo que cada aluno só pode estar em uma universidade e só pode ser parte de um time e que times só podem ser formados por alunos de uma mesma universidade, qual o maior possível número de alunos que podem participar da GCC.

Entrada
A primeira linha da entrada contém um inteiro N (0≤N≤105), o número de universidades que podem mandar seus alunos para participar da GCC.

A segunda linhada entrada contém N inteiros: o i-ésimo inteiro Si é o número de alunos da i-ésima universidade (0≤Si≤102).

Saída
A saída deve ser uma linha contendo um único inteiro: o maior possível número de alunos que podem participar da GCC dado as limitações mencionadas.
'''

N = int(input())
valores = str(input()).split()
for k, v in enumerate(valores):
    valores[k] = int(v)
num_alunos = []
for v in valores:
    div = v // 3
    num_alunos.append(div * 3)
print(sum(num_alunos))
