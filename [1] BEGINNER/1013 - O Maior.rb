=begin
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png" alt="Greatest Formula">


Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
=end

valores = gets.chomp.split.map{|valor| valor.to_i}
maior = valores.max
puts "#{maior} eh o maior"