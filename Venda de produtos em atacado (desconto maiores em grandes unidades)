from re import sub


print("Bem vindo a Loja da Suami Rocha")
valorProduto = float(input("Entre com o valor do produto: "))
qtdProduto = int(input("Entre com a quantidade"))
subtotal = valorProduto * qtdProduto
if qtdProduto < 4:
    valorFinal = subtotal
elif 5 <= qtdProduto < 19:
    valorFinal = subtotal - subtotal * 0.03  # desconto de 3%
elif 20 <= qtdProduto < 99:
    valorFinal = subtotal - subtotal * 0.06  # desconto de 6%
else:  # Se o a quantidade for acima de 100 entra nesse else então desconto de 10%
    valorFinal = subtotal - subtotal * 0.10
print("O valor sem desconto: R$ {:.2f}" . format(subtotal))
print("O valor com desconto: R$ {:.2f}"  . format(valorFinal))
