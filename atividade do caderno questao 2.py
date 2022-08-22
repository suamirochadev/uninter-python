quantidade_pizza_media = 0
quantidade_pizza_grande = 0
valor_total_pizza_media = 0
valor_total_pizza_grande = 0
tamanho_pizza = None
codigo_pizza = None
nome_pizza_escolhida = None
desejo_cliente = None

while True:
    print("Bem Vindo a pizzaria da Su")
    print("____________________________________")
    print("|Código| Descrição |Pizza M|Pizza G |")
    print("|------|-----------|-------|--------|")
    print("|  21  |Napolitana | R$20  | R$26   |")
    print("|  22  |Margherita | R$20  | R$26   |")
    print("|  23  |Calabresa  | R$25  | R$32.50|")
    print("|  24  |Toscana    | R$30  | R$39   |")
    print("|  25  |Portuguesa | R$30  | R$39   |")
    print("|___________________________________|")

    while tamanho_pizza not in ["M", "G"]:
        tamanho_pizza = input(
            "Informe o tamanho da pizza (M/G): ").upper().strip()
        if tamanho_pizza == "M":
            quantidade_pizza_media += 1
        elif tamanho_pizza == "G":
            quantidade_pizza_grande += 1
        else:
            print("Tamanho inválido. Tente Novamente.")

    while codigo_pizza not in [21, 22, 23, 24, 25]:
        codigo_pizza = int(input("Digite o código da pizza: "))
        if codigo_pizza == 21:
            nome_pizza_escolhida = "Napolitana"
            if tamanho_pizza == "M":
                valor_total_pizza_media += 20
            else:
                valor_total_pizza_grande += 26
        elif codigo_pizza == 22:
            nome_pizza_escolhida = "Margherita"
            if tamanho_pizza == "M":
                valor_total_pizza_media += 20
            else:
                valor_total_pizza_grande += 26
        elif codigo_pizza == 23:
            nome_pizza_escolhida = "Calabresa"
            if tamanho_pizza == "M":
                valor_total_pizza_media += 25
            else:
                valor_total_pizza_grande += 32.50
        elif codigo_pizza == 24:
            nome_pizza_escolhida = "Toscana"
            if tamanho_pizza == "M":
                valor_total_pizza_media += 30
            else:
                valor_total_pizza_grande += 39
        elif codigo_pizza == 25:
            nome_pizza_escolhida = "Portuguesa"
            if tamanho_pizza == "M":
                valor_total_pizza_media += 30
            else:
                valor_total_pizza_grande += 39

        else:
            print("Código inválido. Tente novamente.")
            continue

        print("Você pediu uma pizza {}.\n".format(nome_pizza_escolhida))

    desejo_cliente = input(
        "Deseja comprar outra pizza? (S/N): ").upper().strip()
    if desejo_cliente == "N":
        break
    tamanho_pizza = None
    codigo_pizza = None


print("Resumo da compra")
if quantidade_pizza_media > 0:
    print("Quantidade de pizza tamanho M: {}".format(quantidade_pizza_media))
    print("Valor total da pizza tamanho M: {:.2f}".format(
        valor_total_pizza_media))
if quantidade_pizza_grande > 0:
    print("Quantidade de pizza tamanho G: {}".format(quantidade_pizza_grande))
    print("Valor total da pizza tamanho G: {:.2f}".format(
        valor_total_pizza_grande))
    valor_pagar = valor_total_pizza_media + valor_total_pizza_grande
    print("_______________________________________________________________________")
    print("Total a pagar: R$ {:.2f}".format(valor_pagar))
