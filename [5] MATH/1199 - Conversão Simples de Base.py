'''
https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1199.gif

Neste problema você é solicitado a escrever um simples programa de conversão de base. A entrada será um valor hexadecimal ou decimal. Você deverá converter cada valor da entrada. Se o valor for hexadecimal, você deve convertê-lo para decimal e vice-versa. O valor hexadecimal inicia sempre com “0x” ou também, é aquele valor cuja segunda casa contém a letra 'x'.

Entrada
A entrada contém vários casos de teste. Cada linha de entrada, com exceção da última, contém um número não-negativo, decimal ou hexa. O valor decimal será menor ou igual a 231. A última linha contém um número negativo que não deve ser processado, indicando o encerramento do programa.

Saída
Para cada linha de entrada (exceto a última) deve ser produzido uma linha de saída. Todo número hexadecimal deve ser precedido na saída por '0x' (zero xis).
'''

while True:
    num = str(input())
    if not '0x' in num and int(num) < 0:
        break
    if num[0] == '0' and num[1] == 'x':
        s = int(num, 16)
        print(int(s))
    else:
        s = int(num)
        s = str(hex(s))
        s = s[2:].upper()
        print('0x'+s)
