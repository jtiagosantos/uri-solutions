'''
Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita Horeleninha (BH)! Antes de viajar para BH, você e seus N-1 amigos decidiram combinar algum dia para ir a uma pizzaria, para relaxar e descontrair (e, naturalmente, comer!).

Neste momento está sendo escolhida a data do evento. Para que todas as pessoas possam participar, foi decidido que o encontro na pizzaria ocorrerá em um data tal que todas as N pessoas podem comparecer à pizzaria nesta data. Portanto, nem toda data pode ser escolhida, pois algumas pessoas podem ter outros compromissos já marcados em alguns dias.

Dada a lista de datas consideradas para o evento e a informações de quais pessoas podem comparecer em quais datas, determine se o evento poderá ocorrer e, em caso positivo, sua data. Caso mais de uma data seja possível, o evento deve ocorrer o mais cedo possível.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém os inteiros N e D (1 ≤ N, D ≤ 50), o número de pessoas e o número de datas consideradas, respectivamente. As pessoas são numeradas de 1 a N. As próximas D linhas descrevem uma data considerada. Cada linha começa com a data na forma dia∕mes∕ano. A linha é seguida de N inteiros p1,p2,...,pN. O inteiro pi é 1 se a pessoa i pode comparecer na data considerada, ou 0 caso contrário. É garantido que as datas são sempre válidas, e não há zeros à esquerda. Além disso, as datas são dadas em ordem, do dia mais cedo para o dia mais tarde.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma linha contendo a data que o evento deve ocorrer, na forma dia∕mes∕ano, de maneira idêntica à da entrada. Caso não seja possível realizar o evento, imprima “Pizza antes de FdI” (sem aspas).
'''

while True:
    try:
        entrada_1 = str(input()).split()
        num_p = int(entrada_1[0])
        num_datas = int(entrada_1[1])
        data_perfeita = []
        for i in range(num_datas):
            cont = 0
            entrada_2 = str(input()).split()
            valores = entrada_2[1:]
            for i in valores:
                if i == '1':
                    cont += 1
            if cont == len(valores):
                data_perfeita.append(entrada_2[0])
        if data_perfeita != []:
            print(''.join(data_perfeita[0]))
        else:
            print('Pizza antes de FdI')
    except EOFError:
        break