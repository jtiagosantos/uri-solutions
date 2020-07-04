'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

valores = str(input()).split()
for k,v in enumerate(valores):
    valores[k] = int(v)

for i in sorted(valores):
    print(i)
print()

for i in valores:
    print(i)