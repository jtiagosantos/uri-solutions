'''
Este ano o sargento está tendo mais trabalho do que de costume para treinar os recrutas. Um deles é muito atrapalhado, e de vez em quando faz tudo errado – por exemplo, ao invés de virar à direita quando comandado, vira à esquerda, causando grande confusão no batalhão. O sargento tem fama de durão e não vai deixar o recruta em paz enquanto este não aprender a executar corretamente os comandos. No sábado à tarde, enquanto todos os outros recrutas estão de folga, ele obrigou o recruta a fazer um treinamento extra. Com o recruta marchando parado no mesmo lugar, o sargento emitiu uma série de comandos "Esquerda, Volver!" e "Direita, Volver!". A cada comando, o recruta deve girar sobre o mesmo ponto e dar um quarto de volta na direção correspondente ao comando. Por exemplo, se o recruta está inicialmente com o rosto voltado para a direção norte, após um comando de "esquerda volver!" ele deve ficar com o rosto voltado para a direção oeste. Se o recruta está inicialmente com o rosto voltado para o leste, após um comando "Direita, volver!" ele deve ter o rosto voltado para o sul. No entanto, durante o treinamento, em que o recruta tinha inicialmente o rosto voltado para o norte, o sargento emitiu uma série tão extensa de comandos, e tão rapidamente, que até ele ficou confuso, e não sabe mais para qual direção o recruta deve ter seu rosto voltado após executar todos os comandos. Você pode ajudar o sargento?
Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro N que indica o número de comandos emitidos pelo sargento (1 ≤ N ≤ 1000)). A segunda linha contém N caracteres, descrevendo a série de comandos emitidos pelo sargento. Cada comando é representado por uma letra: 'E' (para "Esquerda, volver!") e 'D' (para "direita, volver!"). O final da entrada é indicado por N = 0.

A entrada deve ser lida da entrada padrão.

Saída
Para cada caso de teste da entrada seu programa deve produzir uma única linha da saída, indicando a direção para a qual o recruta deve ter sua face voltada após executar a série de comandos, considerando que no início o recruta tem a face voltada para o norte. A linha deve conter uma letra entre 'N', 'L', 'S' e 'O', representando respectivamente as direções norte, leste, sul e oeste.

A saída deve ser escrita na saída padrão.
'''

while True:
    N = int(input())
    if N == 0:
        break
    i = count = 0
    comandos = str(input()).upper()
    count_D = comandos.count('D')
    count_E = comandos.count('E')
    resultado = str()
    direcoes_D = ['N', 'L', 'S', 'O']
    direcoes_E = ['N', 'O', 'S', 'L']
    if count_D > count_E:
        count_D = count_D - count_E
        while True:
            if count > count_D:
                break
            if i == 4:
                i = 0
            resultado = direcoes_D[i]
            count += 1
            i += 1
    elif count_E > count_D:
        i = count = 0
        count_E = count_E - count_D
        while True:
            if count > count_E:
                break
            if i == 4:
                i = 0
            resultado = direcoes_E[i]
            count += 1
            i += 1
    else:
        resultado = 'N'
    print(resultado)
    