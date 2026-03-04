# Crie um algoritmo que peça sua idade , quantidade de saldo e cartão VIP
# Se a idade for maior que 23 e o saldo for maior que 1000 ou possui cartão VIP
# Imprima: Bem-vindo , aceita um café?
# Se não , imprima : Caia fora malandrão

idade = int(input('Digite sua idade: '))
saldo_bancario = float(input('Você possui quanto no banco?: '))
cartao_vip = input('Você possui cartão VIP? S - ( SIM ) , N - ( NÃO )').upper()

if (idade > 23 and saldo_bancario >= 1000) or cartao_vip == 'S':
    print('Bem-vindo , aceita um café?')
else:
    print('Caia fora malandrão')