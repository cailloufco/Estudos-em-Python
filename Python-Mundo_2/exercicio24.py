# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequència de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

termos_exibidos = int(input('Digite quantos números da Sequência de Fibonacci você que ver: '))
contador = 0

termo_anterior = 0
termo_fibonacci = 0
while contador < termos_exibidos:
    print(f'{termo_fibonacci}' , end= ' → ')
    if termo_fibonacci == 0:
        termo_fibonacci += 1
        contador += 1
    else:
        termo_fibonacci = termo_fibonacci + termo_anterior
        termo_anterior = termo_fibonacci - termo_anterior
        contador += 1
