###############################################################################################
# 1 Cadastrar Produto
#_______começo cadastrar produto_______
from locale import currency
from math import fabs
from multiprocessing.sharedctypes import Value


listaProduto = []
def cadastrarP(cod):
    print("Bem-vindo ao cadastro de produtos")
    print("O código do produto a ser cadastrado é: {} " . format(cod))
    nome = input("Digite o nome do produto que deseja: ")
    fab = input("Digite o fabricante do produto desejado: ")
    dicionarioProduto = {'cod': cod,
                        'nome': nome,
                        'fab': fab}
    listaProduto.append(dicionarioProduto.copy())
#_______final cadastrar produto________
###############################################################################################
# 2 Consultar Produto
###############################################################################################
# 2.1 Consultar Todos os Produtos
# 2.2 Consultar Produto por Código
# 2.3 Consultar Produto por Fabricante
# 2.4 Retornar
###############################################################################################
#________começo consultar produto_______
def consultarP():
    print("Bem-vindo ao consultar produto")
    while True:
        try:
            opcao = int(input("Entre com a opção desejada:\n"
                                    "1 - Consultar todos os produtos:\n"
                                    "2 - Consultar produto por código:\n"
                                    "3 - Consultar produtos por fabricante:\n"
                                    "4 - Retornar:\n"
                                    ">>"))
            if opcao == 1: # Menu consultar todos os produtos
                print("Você escolheu: consultar todos os produtos.")
                for produto in listaProduto: # selecionar cada dicionário da minha lista (todos os produtos da minha lista)
                    for key,value in produto.items(): # selecionando cada conjunto chave/valor do dicionário (ex.: 'cod': 1 , 'nome': Presunto , 'fab': Sadia)
                        print("{} : {}" . format(key,value)) # Aqui é onde imprimo cada chave:valor, será impresso da maneira como está.
            elif opcao == 2: # Menu Consultar produtos por código
                print("Você escolheu: consultar produtos por código. ")
                entrada = int(input("Entre com o código do produto"))
                for produto in listaProduto:
                    if (produto['cod'] == entrada):
                        for key,value in produto.items():
                            print("{} : {}" . format(key,value))
            elif opcao == 3: # Menu consultar produtos por fabricante
                print("Você escolheu: consultar por fabricante.")
                entrada = input("Entre com o fabricante desejado: ")
                for produto in listaProduto:
                    if produto['fab'] == entrada:
                        for key,value in produto.items():
                            print("{} : {}" . format(key,value))
            elif opcao == 4: # Retornar
                return
            else:
                print("Pare de digitar números que não existem no menu.")
                continue
        except ValueError:
            print("Pare de digitar valores inexistentes.")
#________final consultar produto_______
###############################################################################################
# 3 Remover Produto
#________começo remover produto_______
def removerP():
    print("Bem-vindo ao remover produto")
    entrada = int(input("Entre com o código desejado para remover: "))
    for produto in listaProduto:
                    if (produto['cod'] == entrada):
                        listaProduto.remove(produto)
#________final remover produto_______
###############################################################################################
# 4 Sair
###############################################################################################
# Main
#________começo main_______
print("Bem-vindo ao programa de Suami Evelin Rocha de Medeiros")
registroP=0

while True:
    try:
        opcao=int(input("Digite a opcao desejada:\n"
                            "1- Cadastrar Produto:\n"
                            "2- Consultar Produto:\n"
                            "3- Remover Produto:\n"
                            "4- Sair"
                            "\n>>"))
        if opcao == 1:
            registroP = registroP + 1
            cadastrarP(registroP)
        elif opcao == 2:
            consultarP()
        elif opcao == 3:
            removerP()
        elif opcao == 4:
            print("Programa finalizado")
            break
        else:
            print("Pare de digitar números que não existem no menu.")
            continue
    except ValueError:
        print("Pare de digitar valores inexistentes.")
#________final main_______
###############################################################################################