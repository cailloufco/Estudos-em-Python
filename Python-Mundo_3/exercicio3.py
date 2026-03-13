# Crie um programa que vai gerar cindo números aleatórios e colocar em uma tupla.
# Depois disso , mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint
numeros_aleatorios = (randint(0,50) ,randint(0,50) ,randint(0,50) ,randint(0,50) ,randint(0,50) )

maior_numero = None
menor_numero = None
#for numero in numeros_aleatorios:
    # if maior_numero == None:
    #     maior_numero = numero
    #     menor_numero = numero
    # else:
    #     if maior_numero < numero:
    #         maior_numero = numero
    #     if numero < menor_numero:
    #         menor_numero = numero
print('-='*50)
print(f'O maior número gerado foi {max(numeros_aleatorios)} e o menor valor gerado foi {min(numeros_aleatorios)}\nA lista gerado a seguinte: ')
for i in numeros_aleatorios:
    print(i , end=' ')
print()
print('-='*50)