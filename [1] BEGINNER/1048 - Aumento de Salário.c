/*
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salary	  Readjustment Rate
0 - 400.00				15%
400.01 - 800.00			12%
800.01 - 1200.00		10%
1200.01 - 2000.00		 7%
Above 2000.00			 4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
*/

#include <stdio.h>
 
int main() {
    double s, r; int p;
    
    scanf("%lf", &s);
    
    if(s>=0 && s<=400){
        r = s * 0.15; s = s + r; p = 15;
    }else if(s>400 && s<=800){
        r = s * 0.12; s = s + r; p = 12;
    }else if(s>800 && s<=1200){
        r = s * 0.10; s = s + r; p = 10;
    }else if(s>1200 && s<=2000){
        r = s * 0.07; s = s + r; p = 7;
    }else{
        r = s * 0.04; s = s + r; p = 4;
    }
    printf("Novo salario: %.2lf\n", s);
    printf("Reajuste ganho: %.2lf\n", r);
    printf("Em percentual: %d %%\n", p);
 
    return 0;
}