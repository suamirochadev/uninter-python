# 3 Questão do Caderno de Atividade Prática da Uninter
# Aluna Uninter RU4194059
print("Bem vindo à feijoada da Suami Evelin Rocha de Medeiros")

# VOLUME FEIJOADA


def volumeFeijoada():
    while True:
        volumeML = float(
            input('Informe a quantidade de mL de feijoada você deseja?'))
        if (300 <= volumeML <= 5000):
            return volumeML * 0.08
        else:
            print(
                'Não servimos quantidades menores que 300ml. Por favor, tente novamente')

# OPÇÃO FEIJOADA


def opcaoFeijoada():  # Recebe os valores do Return, que são as opções de feijoada
    while True:
        print('Menu opção Feijoada')
        opcoes = input('Entre com a opção de feijoada \nb- Básica (Feijão + paiol + costelinha) \np- Premium (Feijão + paiol + costelinha + parts de porco) \ns- Suprema (Feijão + paiol + costelinha + partes do porco + charque + bacon) \n>>>')
        if (opcoes.lower() == 'b'):
            return 1        # Retorna os valores para def opcao()
        elif (opcoes.lower() == 'p'):
            return 1.25     # Retorna os valores para def opcao()
        elif (opcoes.lower() == 's'):
            return 1.50     # Retorna os valores para def opcao()
        else:
            print('Você não digitou uma opção válida')
            continue    # Caso o usuário digite uma opçao de feijoada que não existe, ele voltará para o começo do while

# ACOMPANHAMENTO FEIJOADA


def acompanhamentoFeijoada():
    totais = 0  # AQUI VAI FICAR O ACUMULADOR DO ACOMPANHAMENTO PQ SE NÃO O CÓDIGO NÃO VAI FICAR SE REPETINDO
    # ELES FICAM DENTRO DO INPUT DO ACOMPA EXEMPLO ABAIXO: O /n é para quebrar linhas. PARA ENTENDER MELHOR RODA O CODIGO ABAIXO SOZINHO
# acompa = int(input('Deseja mais algum acompanhamento: \n0- não desejo mais acompanhamentos (encerrar pedido) \n1- 200g de arroz \n2- 150g de farofa especial \n3- 100g de couve cozida \n4- 1 laranja descascada \n>>'))
    while True:
        try:
            acompanhamento = int(input(
                'Deseja algum acompanhamento: \n0- não desejo mais acompanhamentos (encerrar pedido) \n1- 200g de arroz \n2- 150g de farofa especial \n3- 100g de couve cozida \n4- 1 laranja descascada >>'))
            if (acompanhamento == 0):
                return totais  # Quando selecionado ele sai do laço e vai para o Main
            elif (acompanhamento == 1):
                totais = totais + 5  # ESSE totais ELE ENVIA PARA O ACUMULADOR totais LÁ EM CIMA
                continue  # ESSE CONTINUE É PARA O def accompanhamentoFeijoada() FICAR SE REPETINDO ATÉ O USUARIO NÃO QUERER MAIS AI ELE ESCOLHE A OPÇÃO 0 E SAI DO LAÇO
            elif (acompanhamento == 2):
                totais = totais + 6
                continue
            elif (acompanhamento == 3):
                totais = totais + 7
                continue
            elif (acompanhamento == 4):
                totais = totais + 3
                continue
            else:
                print('Digite uma opção válida')
        except ValueError:
            continue


# MAIN FICA AQUI E FORA DOS LAÇOS
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
# O VOLUME E A OPÇÃO ESTA EM () POIS ELES TEM QUE MULTIPLICAR PRIMEIRO PRA DEPOIS SOMAR! O () SERVE PARA VC ESCOLHER O QUE QUER PRIMEIRO
total = (volume * opcao) + acompanhamento
print('O valor a ser pago é (R$): {:.2f} (volume = {:.2f} * opcao = {:.2f} + acompanhamento = {:.2f}) ' .format(
    total, volume, opcao, acompanhamento))
# O :.2f significa que eu quero que ele mostre as casas decimais, pois a questão é em dinheiro R$ 00,00
