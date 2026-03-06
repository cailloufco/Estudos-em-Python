# Faça um programa que leia um número qualquer e mostre seu fatorial

numero_escolhido = int(input('Digite um numero: '))
fatorial = 1

#fatorial usando WHILE:
'''while not(numero_escolhido == 1):
    if fatorial == 0:
        fatorial = numero_escolhido * (numero_escolhido - 1)
        numero_escolhido -= 1
    else:
        fatorial = fatorial * (numero_escolhido - 1)
        numero_escolhido -= 1
print(fatorial)'''


#fatorial usando FOR:
'''for i in range( 1 , numero_escolhido + 1 ):
    fatorial *= i
print(fatorial)'''