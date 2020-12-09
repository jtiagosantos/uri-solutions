/*
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
*/

#include <stdio.h>

int main() {
    int a, b, c;

    scanf("%d%d%d", &a, &b, &c);

    if(a < b && b < c){
        printf("%d\n%d\n%d\n\n", a, b, c);
    }else if(a < c && c < b){
        printf("%d\n%d\n%d\n\n", a, c, b);
    }
    if(b < a && a < c){
        printf("%d\n%d\n%d\n\n", b, a, c);
    }else if(b < c && c < a){
        printf("%d\n%d\n%d\n\n", b, c, a);
    }
    if(c < b && b < a){
        printf("%d\n%d\n%d\n\n", c, b, a);
    }else if(c < a && a < b){
        printf("%d\n%d\n%d\n\n", c, a, b);
    }
    printf("%d\n%d\n%d\n", a, b, c);

    return 0;
}