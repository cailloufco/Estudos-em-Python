#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar , desconsidere-o.
contador = []
for i in range(1,7):
    i = int(input('Digite seis numeros inteiro: '))
    contador.append(i)
soma = 0
for par in contador:
    if par % 2 == 0:
        print(par)
        soma += par
print(f'a soma dos numeros pares é: {soma}')