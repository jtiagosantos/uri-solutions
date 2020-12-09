/*
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
*/

#include <stdio.h>
 
int main() {
    int hi, hf, dur;
    
    scanf("%d%d", &hi, &hf);
    
    if(hi == hf){
        dur = 24;
    }else if(hi > hf){
        dur = (24-hi) + hf;
    }else{
        dur = hf - hi;
    }
    
    printf("O JOGO DUROU %d HORA(S)\n", dur);
 
    return 0;
}