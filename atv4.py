# Questão 4 do Caderno de Atividade Prática Uninter

from importlib.metadata import entry_points


produservilist = list()
proserCodigo = int(0)

# Identificação


def identicicacao():
    suamievelinrochademedeiros_4194059 = 'Suami Evelin Rocha de Medeiros'
    print('Seja bem-vindo a Controle de Estoque o {}. '.format(suamievelinrochademedeiros_4194059))

# Remover Produto


def removerProduto():
    print('Exclusão de Produtos: ')
    while(True):
        try:
            print('Excluído por CÓDIGO.')
            entry = input(input('Informe o Código:\n> '))
            for(produto) in (produservilist):
                if(produto['proserCodigo'] == (entry)):
                    produservilist.remove(produto)
                    return
        except:
            print('Erro desconhecido.')
            continue
        print('Código não localizado.')
        return

# Consultar o produto


def consultarProduto():
    while(True):
        try:
            print('Consulta de Produtos:')
            opce = validaInt(
                'Informe a opção desejada.\n'
                '1. Consultar todos.\n'
                '2. Consultar por Código.\n'
                '3. Consultar por Fabricante.\n'
                '4. Retornar.\n> ', 1, 4
            )
            if((opce) == (int(1))):
                print('Consultando todos.')
                for(produto) in (produservilist):
                    for(key, value) in (produto.items()):
                        print('{}: {}'.format(key, value))
            elif((opce) == (int(2))):
                while True:
                    try:
                        print('Consultando por código.')
                        entry = int(input('Informe o Código::\n>'))
                        for(produto) in (produservilist):
                            if(produto['proserCodigo'] == (entry)):
                                for(key, value) in (produto.items()):
                                    print('{}: {}'.format(key, value))
                                return
                    except:
                        print('Erro desconhecido.')
                        continue
                    print('Código não localizado.')
                    return
            elif((opce) == (int(3))):
                while(True):
                    try:
                        print('Consultando por Fabricante.')
                        entry = input('Informe a Fabricante:\n> ').upper()
                        for(produto) in (produservilist):
                            if(produto['fabricanteProduto'] == (entry)):
                                for(key, value) in (produto.items()):
                                    print('{}: {}'.format(key, value))
                        return
                    except:
                        print('Erro desconhecido.')
                        continue
                else:
                    return
        except:
            print('Erro desconhecido.')
            continue
# Cadastrar Produto


def cadastrarProduto(proserCodigo):
    print('Cadastro de Produtos: ')
    print('Código do Produto: {}'.format(proserCodigo))
    nomeProduto = -input('Informe o nome do produto: ').upper()
    fabricanteProduto = input('Informe a fabricante do produto: ').upper
    valorProduto = float(input('Informe o fabricante do produto: R$'))
    produservi = dict({
        'proserCodigo': proserCodigo,
        'nomeProduto': nomeProduto,
        'fabricanteProduto': fabricanteProduto,
        'valorProduto': valorProduto
    })
    produservilist.append(produservi.copy())

# Validar número inteiro


def validaInt(q, min, max):
    x = int(input(q))
    while(((x) < (min)) or ((x) > (max))):
        x = int(input(q))
    return x

# Principal


def identificacao():
    while(True):
        try:
            op = int(validaInt(
                'Informe a opção desejada.\n'
                '1. Cadastro\n'
                '2. Filtro\n'
                '3. Exclusão\n'                proserCodigo += 1
                cadastrarProduto(proserCodigo)
            elif((op) == (int(2))):
                consultarProduto()
            elif((op) == (int(3))):
                removerProduto()
            else:
                break
        except:
            print('Erro descon# Questão 4 do Caderno de Atividade Prática Uninter


# Remover Produto


def removerProduto():
    print('Exclusão de Produtos:')
    while(True):
        try:
            print('Excluíndo por CÓDIGO.')
            entry = int(input('Informe o Código:\n> '))
            for(produto)in(produservilist):
                if(produto['proserCodigo']==(entry)):
                    produservilist.remove(produto)
                    return
        except:
            print('Erro desconhecido.')
            continue
        print('Código não localizado.')
        return

# Consultar o produto

def consultarProduto():
    while(True):
        try:
            print('Consulta de Produtos:')
            opce=validaInt(
                'Informe a opção desejada.\n'
                '1. Consultar todos.\n'
                '2. Consultar por Código.\n'
                '3. Consultar por Fabricante.\n'
                '4. Retornar.\n> ',1,4
            )
            if((opce)==(int(1))):
                print('Consultando todos.')
                for(produto)in(produservilist):
                    for(key,value)in(produto.items()):
                        print('{}: {}'.format(key, value))
            elif((opce)==(int(2))):
                while(True):
                    try:
                        print('Consultando por código.')
                        entry=int(input('Informe o Código:\n> '))
                        for(produto) in (produservilist):
                            if(produto['proserCodigo']==(entry)):
                                for(key,value)in(produto.items()):
                                    print('{}: {}'.format(key,value))
                                return
                    except:
                        print('Erro desconhecido.')
                        continue
                    print('Código não localizado.')
                    return
            elif((opce) == (int(3))):
                while(True):
                    try:
                        print('Consultando por Fabricante.')
                        entry=input('Informe a Fabricante:\n> ').upper()
                        for(produto)in(produservilist):
                            if(produto['fabricanteProduto']==(entry)):
                                for(key,value)in(produto.items()):
                                    print('{}: {}'.format(key, value))
                        return
                    except:
                        print('Erro desconhecido.')
                        continue
                else:
                    return
        except:
            print('Erro desconhecido.')
            continue

# Cadastrar Produto

def cadastrarProduto(proserCodigo):
    print('Cadastro de Produtos: ')
    print('Código do Produto: {}'.format(proserCodigo))
    nomeProduto=input('Informe o nome do produto: ').upper()
    fabricanteProduto=input('Informe a fabricante do produto: ').upper
    valorProduto=float(input('Informe o fabricante do produto: R$'))
    produservi=dict({
        'proserCodigo':proserCodigo,
        'nomeProduto':nomeProduto,
        'fabricanteProduto':fabricanteProduto,
        'valorProduto':valorProduto
    })
    produservilist.append(produservi.copy())

# Validar número inteiro

def validaInt(q, min, max):
    x=int(input(q))
    while(((x)<(min))or((x)>(max))):
        x=int(input(q))
    return x

# Principal

def identificacao():
    while(True):
        try:
            op=int(validaInt(
            'Informe a opção desejada.\n'
            '1. Cadastro\n'
            '2. Filtro\n'
            '3. Exclusão\n'
            '4. Sair\n> ',1,4
            ))
            if((op)==(int(1))):
                proserCodigo+=1
                cadastrarProduto(proserCodigo)
            elif((op)==(int(2))):
                consultarProduto()
            elif((op)==(int(3))):
                removerProduto()
            else:
                break
        except:
            print('Erro desconhecido.')
            continue
        
produservilist = list()
proserCodigo = int(0)
