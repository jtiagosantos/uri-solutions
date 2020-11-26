/*
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
*/

#include <stdio.h>
 
int main() {
    int t, h, m, s; h=m=s=0;
    
    scanf("%d", &t);
    s = t;
    while(s >= 60){
        s -= 60; m++;
    }
    while(m >= 60){
        m -= 60; h++;
    }
    printf("%d:%d:%d\n", h, m, s);
 
    return 0;
}