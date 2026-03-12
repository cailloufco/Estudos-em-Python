# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

numero_escolido = int(input('Digite um valor para ver se é positivo ou negativo'))

if numero_escolido < 0:
    print('seu numero é negativo')
elif numero_escolido > 0:
    print('Seu numero é positivo')
else:
    print('Seu numero é ZERO')