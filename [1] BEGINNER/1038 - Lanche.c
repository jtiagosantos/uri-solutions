/*
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1038_en.png" alt="Price Table">

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
*/

#include <stdio.h>
 
int main() {
    int cod, qt; double tt;
    
    scanf("%d%d", &cod, &qt);
    
    switch(cod){
        case 1:
            tt = 4 * qt;
            break;
        case 2:
            tt = 4.5 * qt;
            break;
        case 3:
            tt = 5 * qt;
            break;
        case 4:
            tt = 2 * qt;
            break;
        case 5:
            tt = 1.5 * qt;
            break;
    }
    
    printf("Total: R$ %.2lf\n", tt);
 
    return 0;
}