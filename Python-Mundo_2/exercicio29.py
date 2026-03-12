# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final , mostre:
'''
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
'''
produtos_mais_de_1000 = 0
mais_barato = None
total_gasto = 0
nome_do_mais_barato = None
while True:
    nome_do_produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto : '))
    total_gasto += valor

    if mais_barato == None:
        mais_barato = valor

    elif valor < mais_barato:
        mais_barato = valor
        nome_do_mais_barato = nome_do_produto
        
    if valor > 1000:
        produtos_mais_de_1000 += 1
    
    continuar = input('Você deseja continuar? S/N').upper()
    if continuar == 'N':
        break
print(f'O produto mais barato foi o {nome_do_mais_barato} custando {mais_barato} , tiveram {produtos_mais_de_1000} custando mais de 1000 e o total gasto foi {total_gasto:.2}')