# Faça um Programa que leia três números e mostre o maior e o menor deles.
numeros = []
for i in range(3):
    numeros.append(int(input(f'{i} - Digite um numero: ')))
numeros.sort()
print(numeros[0])
print(numeros[2])