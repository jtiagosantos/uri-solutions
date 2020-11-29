/*
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
*/

#include <stdio.h>
#include <math.h>
 
int main() {
    double a, b, c, delta, raiz_delta, x1, x2;
    
    scanf("%lf%lf%lf", &a, &b, &c);
    
    if(a == 0){
        printf("Impossivel calcular\n");
    }else {
        delta = pow(b,2) - 4*a*c;
        
        if(delta < 0){
            printf("Impossivel calcular\n");
        }else {
            raiz_delta = sqrt(delta);
            x1 = (-b + raiz_delta) / (2.0*a);
            x2 = (-b - raiz_delta) / (2.0*a);
            printf("R1 = %.5lf\n", x1);
            printf("R2 = %.5lf\n", x2);
        }
    }
 
    return 0;
}