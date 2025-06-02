# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# --> A) qual é o total gasto na compra.
# --> B) quantos produtos custam mais de R$1000.
# --> C) qual é o nome do produto mais barato.

# capitalize() -> só o primeiro caractere fica maiusculo

produto             = ''
preco               = 0
total               = 0
produtosCaros       = 0
menorPreco          = 0
produtoMaisBarato   = ''
counter             = 0

while True:
    # --> Iniciando a consulta
    print('\n##### CONSULTOR DE PRODUTOS #####')
    produto = str(input('# Qual o nome do produto > ')).strip().lower()
    preco   = float(input('# Qual o preco? > R$'))
    n       = str(input('# Deseja continuar [S/N]? > ')).strip().lower()
    # --> Estabelecendo as estatisticas
    # 1 - Gasto total
    total   = (total+preco) 
    # 2 - Produtos que custam +1000
    if preco>=1000:
        produtosCaros = produtosCaros+1
    # 3 - Nome do produto mais barato
    if counter == 0:
        produtoMaisBarato = produto
        menorPreco        = preco
    if ((counter != 0) and (preco<menorPreco)):
        produtoMaisBarato = produto
        menorPreco        = preco
    counter = counter+1
    if (n == 'n'):
        break
print('\n------------------------RELATORIO GERAL------------------------')
print(f'[Total gasto]                                 -> R${total:.2f}')
print(f'[Total de produtos que custam mais de R$1000] -> {produtosCaros}')
print(f'[Produto mais barato]                          -> {produtoMaisBarato.capitalize()} (R${menorPreco:.2f})\n')


 