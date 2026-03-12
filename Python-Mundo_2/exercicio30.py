# Crie um programa que simule o funcionamento de um caixa eletrônico. No início , pergunte ao usuário qual será o valor a ser sacado (NUMERO INTEIRO) e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Considere que o vaixa possui cédulas de R$50 , R$20 , R$10 e R$1

valor_sacado = int(input('Digite o valor que será sacado: '))
while True:
    if valor_sacado > 0:
        if valor_sacado >= 50:
            print(f'NOTAS DE 50 = {valor_sacado//50}')
            valor_sacado = valor_sacado % 50
            if valor_sacado == 0:
                break
        if valor_sacado >= 20:
            print(f'NOTAS DE 20 = {valor_sacado//20}')
            valor_sacado = valor_sacado % 20
            if valor_sacado == 0:
                break
        if valor_sacado >= 10:
            print(f'NOTAS DE 10 = {valor_sacado//10}')
            if valor_sacado == 0:
                break
        if valor_sacado >= 1:
            print(f'MOEDAS DE 1 = {valor_sacado}')            
    else:
        print('Valor inválido')
    break