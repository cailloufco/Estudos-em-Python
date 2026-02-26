#Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 até 500
soma= 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            print(i)
            soma += i
print(f'a soma entre todos os numeros impares multiplos de três é: {soma}')