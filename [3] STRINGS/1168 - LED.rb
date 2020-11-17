=begin
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.


https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1168.png

Entrada
A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor que João quer montar com os leds.

Saída
Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".
=end

dict = {
	'0' => 6,
	'1' => 2,
	'2' => 5,
	'3' => 5,
	'4' => 4,
	'5' => 5,
	'6' => 6,
	'7' => 3,
	'8' => 7,
	'9' => 6
}

n = gets.chomp.to_i
n.times do
	num = gets.chomp.scan(/./)
	count = 0
	for i in num
		count += dict[i]
	end
	puts "#{count} leds"
end