# Exemplo - 06
# Aluno: Hnerique Godoi Ribeiro
# Objetivo:Ler o preço, quantidade e valor do produto que o cliente comprou e mostrar  na mensagem.

preço = float(input("Digite o preço do prudoto: "))
quantidade = int(input("Digite a quantidade de produtos que comprou: "))
valor_pago = float(input("Digite o valor que o cliente pagou: "))

total_compra = preço * quantidade
total_compra = valor_pago - total_compra  

print("A compra deu: ",total_compra,)
