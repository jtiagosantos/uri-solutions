/*
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
*/

#include <stdio.h>
 
int main() {
    int valor, cpvalor, cem, cinq, vinte, dez, cinco, dois, um;
    cem = cinq = vinte = dez = cinco = dois = um = 0;
    
    scanf("%d", &valor);
    cpvalor = valor;
    
    while(valor >= 100){
        valor -= 100; cem++;
    }
    while(valor >= 50){
        valor -= 50; cinq++;
    }
    while(valor >= 20){
        valor -= 20; vinte++;
    }
    while(valor >= 10){
        valor -= 10; dez++;
    }
    while(valor >= 5){
        valor -= 5; cinco++;
    }
    while(valor >= 2){
        valor -= 2; dois++;
    }
    um = valor;
    
    printf("%d\n", cpvalor);
    printf("%d nota(s) de R$ 100,00\n", cem);
    printf("%d nota(s) de R$ 50,00\n", cinq);
    printf("%d nota(s) de R$ 20,00\n", vinte);
    printf("%d nota(s) de R$ 10,00\n", dez);
    printf("%d nota(s) de R$ 5,00\n", cinco);
    printf("%d nota(s) de R$ 2,00\n", dois);
    printf("%d nota(s) de R$ 1,00\n", um);
    
    return 0;
}