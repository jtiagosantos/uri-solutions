/*
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1049_b.png" alt="Animal Species Table">

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
*/

#include <stdio.h>

int main() {
    char animal[12];

    scanf("%s", &animal);
    switch(animal[0]){
        case 'v':
            scanf("%s", &animal);
            if(animal[0]=='a'){
                scanf("%s", &animal);
                if(animal[0]=='c'){
                    printf("aguia\n");
                }else{
                    printf("pomba\n");
                }
            }else{
                scanf("%s", animal);
                if(animal[0]=='o'){
                    printf("homem\n");
                }else{
                    printf("vaca\n");
                }
            }
            break;
        case 'i':
            scanf("%s", &animal);
            if(animal[0]=='i'){
                scanf("%s", &animal);
                if(animal[2]=='m'){
                    printf("pulga\n");
                }else{
                    printf("lagarta\n");
                }
            }else{
                scanf("%s", &animal);
                if(animal[0]=='h'){
                    printf("sanguessuga\n");
                }else{
                    printf("minhoca\n");
                }
            }
            break;
    }

    return 0;
}