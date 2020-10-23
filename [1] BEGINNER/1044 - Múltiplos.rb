=begin
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
=end

valores = gets.chomp.split.map{|valor| valor.to_i}
if valores[0] % valores[1] == 0 or valores[1] % valores[0] == 0
    puts "Sao Multiplos"
else
    puts "Nao sao Multiplos"
end