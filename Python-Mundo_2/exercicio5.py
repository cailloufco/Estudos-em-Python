#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria , de acordo com a idade:
'''
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''

from time import sleep

#Pegando ano atual
from datetime import date
anoAtual= date.today().year

print('\nConfederação Nacional de Natação\nInscrição em categoria de acordo com a idade')

try:
    anoDeNascimento = int(input('Digite o ano em que você nasceu: '))
    idadeDoAtleta = anoAtual - anoDeNascimento
    if idadeDoAtleta < 9 or idadeDoAtleta > 100:
        print('Você não possui idade para participar de nenhuma categoria', sleep(1.5))
        exit()
except:
    print('Insira uma data válida')