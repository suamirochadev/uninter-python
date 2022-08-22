
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

quantidade_pizza_media = 1
quantidade_pizza_grande = 1
valor_total_pizza_media = 0
valor_total_pizza_grande = 0
tamanho_pizza = None
codigo_pizza= None
nome_pizza_escolhida = None
desejo_cliente = None

while tamanho_pizza == 'M' and tamanho_pizza == 'G':
    tamanho_pizza = input('Informe o tamanho da pizza (M/G): ')
if tamanho_pizza == 'M':
        quantidade_pizza_media += 1
            
elif tamanho_pizza == 'G':
        quantidade_pizza_grande += 1
            
else:
        print('Tamanho inválido. Tente Novamente.')
        

while codigo_pizza == '21' or '22' or '23' or '24' != '25':
        if (codigo_pizza == 21 and tamanho_pizza == 'M'):
                nome_pizza_escolhida = 'Napolitana'
                valor_total_pizza_media += 20
        elif(codigo_pizza == 21) and tamanho_pizza == 'G':
                nome_pizza_escolhida = 'Napolitana'
                valor_total_pizza_grande += 26
        if (codigo_pizza == 22 and tamanho_pizza == 'M'):
                nome_pizza_escolhida = 'Margherita'
                valor_total_pizza_media += 20
        elif(codigo_pizza == 22) and tamanho_pizza == 'G':
                nome_pizza_escolhida = 'Margherita'
                valor_total_pizza_grande += 26
        if (codigo_pizza == 23 and tamanho_pizza == 'M'):
                nome_pizza_escolhida = 'Calabresa'
                valor_total_pizza_media += 25
        elif(codigo_pizza == 23) and tamanho_pizza == 'G':
                nome_pizza_escolhida = 'Calabresa'
                valor_total_pizza_grande += 32.50
        if (codigo_pizza == 24 and tamanho_pizza == 'M'):
                nome_pizza_escolhida = 'Toscana'
                valor_total_pizza_media += 30
        elif(codigo_pizza == 24) and tamanho_pizza == 'G':
                nome_pizza_escolhida = 'Toscana'
                valor_total_pizza_grande += 39
        if (codigo_pizza == 25 and tamanho_pizza == 'M'):
                nome_pizza_escolhida = 'Portuguesa'
                valor_total_pizza_media += 30
        elif(codigo_pizza == 25) and tamanho_pizza == 'G':
                nome_pizza_escolhida = 'Portuguesa'
                valor_total_pizza_grande += 39
        else:
                print('Código inválido. Tente novamente.')
                if tamanho_pizza == 'M':
                        quantidade_pizza_media -= 1
                else:
                        quantidade_pizza_grande -= 1
                print('Você pediu uma pizza {}.\n'.format(nome_pizza_escolhida))
while desejo_cliente != input(('Deseja comprar outra pizza? (S/N): ')):
    if desejo_cliente == 'S':
        continue
    else:
        desejo_cliente == 'N'
        print('Resumo da compra')
    if quantidade_pizza_media > 0:
        print('Quantidade de pizza tamanho M: {}'. format(quantidade_pizza_media))
        print('Valor total da pizza tamanho M: {:.2f}'. format(valor_total_pizza_media))
    if (quantidade_pizza_grande > 0):
        print('Quantidade de pizza tamanho M: {}'. format(quantidade_pizza_grande))
        print('Valor total da pizza tamanho M: {:.2f}'. format(valor_total_pizza_grande))
        valor_pagar = valor_total_pizza_media + valor_total_pizza_grande
        print('_______________________________________________________________________')
        print('Total a pagar: R$ {:.2f}'.format(valor_pagar))
        break