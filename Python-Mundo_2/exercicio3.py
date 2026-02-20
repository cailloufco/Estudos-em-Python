#Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela:
'''
-O primeiro valor é maior
-O segundo valor é maior
-Os valores são iguais
'''
from time import sleep

try:
    numeroDoUsuario1 = int(input('Digite um numero: '))
    numeroDoUsuario2 = int(input('Digite outro numero: '))
except ValueError:
    print('\nDIGITE NUMEROS INTEIROS')
    sleep(1)
print('-'*12)
if numeroDoUsuario1 > numeroDoUsuario2:
    print(f'O primeiro valor é maior: {numeroDoUsuario1}')
elif numeroDoUsuario1 < numeroDoUsuario2:
    print(f'O segundo valor é maior: {numeroDoUsuario2}')
else:
    print('Os valores são iguais')