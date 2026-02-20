#Escreva um programa que leia um *numero inteiro* qualquer e peça para que o usuario escolha qual será a base de conversão:
'''
1- para BINARIO
2- para OCTAL
3- para HEXADECIMAL
'''
from time import sleep

while True:
    try:
        numeroQualquer = int(input('Digite um numero inteiro qualquer: '))
        break
    except ValueError:
         print('\nescolha um numero INTEIRO\n')
         sleep(2)

while True:
    try:
        print('Escolha sua base de conversão')
        print('''1- para BINARIO
2- para OCTAL
3- para HEXADECIMAL''')
        escolhaDoUsuario = int(input('Escolha: 1 , 2 ou 3 ou então digite qualquer tecla para sair'))
        print('\n')

        match escolhaDoUsuario:
            case 1:
                print('Resultado BINARIO:', bin(int(numeroQualquer))[2:], '\n')
                sleep(1)
            case 2:
                print('Resultado OCTAL:', oct(int(numeroQualquer))[2:],'\n')
                sleep(1)
            case 3:
                print('Resultado HEXADECIMAL:', hex(int(numeroQualquer))[2:], '\n')
                sleep(1)
            case _ :
                break
    except ValueError:
        break
        

    
    



