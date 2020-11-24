/*
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png" alt="Greatest Formula">


Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
*/

#include <stdio.h>
#include <math.h>
 
int main() {
    int a, b, c, maiorAB;
    
    scanf("%d %d %d", &a, &b, &c);
    maiorAB = (a+b+abs(a-b)) / 2;
    
    if(maiorAB > c){
        printf("%d", maiorAB);
    }else{
        printf("%d", c);
    }
    printf(" eh o maior\n");
 
    return 0;
}