/*
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
*/

#include <stdio.h>
 
int main() {
    int a, b, c, d;
    
    scanf("%d %d %d %d", &a,&b, &c, &d);
    printf("DIFERENCA = %d\n", a*b-c*d);
 
    return 0;
}