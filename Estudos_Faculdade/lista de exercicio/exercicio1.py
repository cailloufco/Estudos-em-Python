#Faça um Programa que peça dois números e imprima o maior deles.
numero_escolhido = int(input('Digite um numero'))
numero_escolhido2 = int(input('Digite um outro numero'))

if numero_escolhido > numero_escolhido2:
    print(numero_escolhido)
elif numero_escolhido < numero_escolhido2:
    print(numero_escolhido2)
else:
    print('Os valores são iguais')