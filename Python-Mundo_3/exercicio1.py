# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso
try:
    numeros_por_extenso = ('zero' , 'um' , 'dois' , 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez')
    num = int(input('Digite um número para ser exibido por extenso: '))
    if num > 10 or num < 0:
        print('Valor inválido')
        exit()
    else:
        print(f'{numeros_por_extenso[num]}')
except:
    print('Valor inválido')