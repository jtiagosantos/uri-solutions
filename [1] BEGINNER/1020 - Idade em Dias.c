/*
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
*/

#include <stdio.h>
 
int main() {
    int idade, ano, mes, dia; ano=mes=dia=0;
    
    scanf("%d", &idade);
    while(idade >= 365){
        idade -= 365; ano++;
    }
    while(idade >= 30){
        idade -= 30; mes++;
    }
    dia = idade;
    
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", ano, mes, dia);
 
    return 0;
}