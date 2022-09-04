# Uninter_Atividade_Pratica_1
Caderno de Atividade prática avaliativa referente ao primeiro semestre do curso de Análise e Desenvolvimento de Sistemas.

#Primeira Questão
>
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade conforme a tabela abaixo:
Quantidades	Desconto:
Até 4	0% na unidade
Entre 5 e 19	3% na unidade
Entre 20 e 99	6% na unidade
Maior ou igual a 100	10% na unidade

>

Elabore um programa em Python que:
1.	Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
2.	Entre com a quantidade desse produto;
3.	O programa deve retornar o valor total sem desconto;
4.	O programa deve retornar o valor total após o desconto;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
6.	Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 10 und

#############################################################################################################################
#Segunda Questão
>
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma pizzaria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Pizzaria possui seguinte tabela de sabores de pizzas listados com sua descrição, códigos e valores:
Código	Descrição	Pizza Média - M	Pizza Grande – G (30% mais cara)
21	Napolitana	R$ 20,00	R$ 26,00
22	Margherita	R$ 20,00	R$ 26,00
23	Calabresa	R$ 25,00	R$ 32,50
24	Toscana	R$ 30,00	R$ 39,00
25	Portuguesa	R$ 30,00	R$ 39,00

>

Elabore um programa em Python que:
1.	Entre com o tamanho da pizza
2.	Entre com o código do produto desejado;
3.	Pergunte se o cliente quer pedir mais alguma coisa (se sim repetir a partir do item 1.  Caso contrário ir para próximo passo); 
4.	Encerre a conta do cliente com o valor total;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);
6.	Se a pessoa digitar um TAMANHO de pizza e/ou   NÚMERO diferente dos da tabela printar na tela: ‘opção inválida’ e voltar para o menu (EXIGÊNCIA 2 de 3);
7.	Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
o	(DICA: utilizar o continue dentro else que verifica a opção inválida)
o	(DICA: utilizar o break dentro if que verifica a opção sair)
8.	Colocar um exemplo de SAIDA DE CONSOLE com duas pizzas
9.	Colocar um exemplo de SAIDA DE CONSOLE com erro ao digitar código

#############################################################################################################################
#Terceira Questão
>
Enunciado: Imagina-se que você e sua equipe foram contratados por um restaurante que serve feijoada para desenvolver a solução de software. Você ficou encarregado da parte de retirar pedido por parte do cliente.
O valor que a empresa cobra por feijoada é dado pela seguinte equação:
total=(volume*opção)+adional(is)
Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:

Quadro 1: Volume versus Valor
volume (ml)	valor (R$)
volume < 300	Não é aceito
300  <= volume <= 5000	volume * 0.08
volume > 5000	Não é aceito
	
Quadro 2: Opção versus multiplicador
peso(kg)	multiplicador
b - Básica (Feijão + paiol + costelinha) 	1.00
p - Premium (Feijão + paiol + costelinha + partes de porco)	1.25
s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)	1.50


Quadro 3: Acompanhamento versus Valor
rota	Valor (R$)
0- Não desejo mais acompanhamentos (encerrar pedido)	0,00
1- 200g de arroz	5,00
2- 150g de farofa especial	6,00
3- 100g de couve cozida	7,00
4- 1 laranja descascada	3,00

>

Elabore um programa em Python que:
1.	Pergunte o volume (em ml).Se digitar um valor não numérico e/ou volume for menor/maior que o limite aceito repetir a pergunta;
2.	Pergunte a opção da feijoada. Se digitar uma opção não válida deve repetir a pergunta
3.	Pergunte o acompanhamento. Deve-se perguntar se o usuário quer mais um acompanhamento até digitar a opção 0
4.	Encerre o total a ser pago com base na equação desse enunciado;
5.	Deve-se codificar uma função volumeFeijoada (EXIGÊNCIA 1 de 3);
o	Deve-se perguntar dentro da função o volume da porção (em ml);
o	Deve-se ter um if/else ou if/elif ou if/else/elif para verificar se o usuário não digitou um volume fora da faixa com que o restaurante trabalha;
o	Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
o	Deve-se retornar o valor em (RS) conforme a Quadro 1
6.	Deve-se codificar uma função opcaoFeijoada (EXIGÊNCIA 2 de 3);
o	Deve-se perguntar dentro da função a opção desejada;
o	Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
o	Deve-se retornar o multiplicador conforme o Quadro 2
7.	Deve-se codificar uma função acompanhamentoFeijoada (EXIGÊNCIA 3 de 3);
o	Deve-se perguntar dentro se deseja ou não mais algum acompanhamento
o	Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
o	Deve-se retornar o multiplicador conforme o Quadro 3
8.	Colocar um exemplo de SAIDA DE CONSOLE um pedido com volume, opção e 2 acompanhamentos válidos
9.	Colocar um exemplo de SAIDA DE CONSOLE com o tratamento de erro quando digitado um valor não numérico é digitado e uma opção não permitida no menu opção de feijoada

#############################################################################################################################
#Quarta Questão
>
Enunciado: Imagina-se que você está desenvolvendo um software de controle de estoque para uma mercearia. Este software deve ter o seguinte menu e opções:
1.	Cadastrar Produto
2.	Consultar Produto(s)
1)	Consultar Todas as Produto
2)	Consultar Produto por Código
3)	Consultar Produto(s) por Fabricante
4)	Retornar 
3.	Remover Produto
4.	Sair

>

Elabore um programa em Python que:
1.	Deve-se codificar uma função cadastrarProduto (código) (EXIGÊNCIA 1);
o	Essa função recebe como parâmetro um código exclusivo para cada produto cadastrado (DICA: utilize um contador como parâmetro) 
o	Dentro da função perguntar o nome do produto;
o	Dentro da função perguntar o fabricante do produto;
o	Dentro da função perguntar o valor do produto
o	Cada produto cadastrado deve ter os seus dados armazenados num DICIONÁRIO (DICA: Conferir material escrito da p. 22 até p24  da AULA 06)
2.	Deve-se codificar uma função consultarProduto(EXIGÊNCIA 2);
o	Dentro da função ter um menu com as seguintes opções:
	Consultar Todos os Produtos
	Consultar Produtos por Código
	Consultar Produtos por Fabricante
	Retornar
3.	Deve-se codificar uma função chamada removerProduto (EXIGÊNCIA 3);
o	Dentro da função perguntar qual o código do produto que se deseja remover do cadastro (da lista de dicionário)
4.	Colocar um exemplo de SAIDA DO CONSOLE com o cadastro de 3 (ou mais) produto. Sendo que 2 delas do mesmo fabricante – ver figura 1
5.	Colocar um exemplo de SAIDA DO CONSOLE com a consulta a todos os produtos cadastrados – ver figura 2
6.	Colocar um exemplo de SAIDA DO CONSOLE com uma consulta por código – ver figura 3
7.	Colocar um exemplo de SAIDA DO CONSOLE com uma consulta por fabricante – ver figura 4
8.	Colocar um exemplo de SAIDA DO CONSOLE ao remover um produto cadastrado e mostrando depois todos os produtos – ver figura 5
