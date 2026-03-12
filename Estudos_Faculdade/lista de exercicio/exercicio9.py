# Faça um Programa que leia três números e mostre-os em ordem decrescente.
numeros= []
for i in range(3):
    numeros.append(int(input(f'{i + 1}Digite um numemero: ')))
numeros.sort()
numero1 = numeros[0]
numero2 = numeros[1]
numero3 = numeros[2]
print(numero3 , numero2 , numero1)

