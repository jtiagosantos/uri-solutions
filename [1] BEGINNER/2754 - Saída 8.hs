{-
O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Crie duas variáveis reais de dupla precisão;
Atribua a primeira o valor 234.345 e a segunda o valor 45.698;
Imprima as duas variáveis com seis casas decimais;
Imprima as duas variáveis com sem nenhuma casa decimal;
Imprima as duas variáveis com com uma casa decimal;
Imprima as duas variáveis com com duas casa decimal;
Imprima as duas variáveis com com três casa decimal;
Imprima as duas variáveis com notação cientifica com 'e';
Imprima as duas variáveis com notação cientifica com 'E';
Imprima as duas variáveis com use a representação mais curta, com 'e' ou 'E' ou sem;
Imprima as duas variáveis com use a representação mais curta, com 'e' ou 'E' ou sem;
Para imprimir, separe os valores com um espaço em branco, um traço (-) e um espaço em branco.

Entrada
Não há.

Saída
O resultado de seu programa deve ser escrito conforme o exemplo da saída.
-}

import Text.Printf

main = do	
printf "234.345000 - 45.698000\n"
printf "234 - 46\n"
printf "234.3 - 45.7\n"
printf "234.34 - 45.70\n"
printf "234.345 - 45.698\n"
printf "2.343450e+02 - 4.569800e+01\n"
printf "2.343450E+02 - 4.569800E+01\n"
printf "234.345 - 45.698\n"
printf "234.345 - 45.698\n"