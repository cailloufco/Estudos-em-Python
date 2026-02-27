#Faça um programa que leia um número inteiro e diga se ele é é ou não um número primo.
try:
    numeroDigitadoPorUsuario = int(input('Digite um numero inteiro: '))
except:
    print(f'Digite um valor válido')
primo = True
if numeroDigitadoPorUsuario == 1:
    print('Numero não é primo')
    exit()
for i in range (2 , numeroDigitadoPorUsuario):
    if numeroDigitadoPorUsuario % i == 0:
        primo = False
        break
if primo == False:
    print('Numero não é primo')
else:
    print('Numero é primo')