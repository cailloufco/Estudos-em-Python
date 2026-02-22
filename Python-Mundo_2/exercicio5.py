#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria , de acordo com a idade:
'''
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
from time import sleep
from datetime import date
anoAtual= date.today().year

print('\nConfederação Nacional de Natação\nInscrição em categoria de acordo com a idade')

try:
    anoDeNascimento = int(input('Digite o ano em que você nasceu: '))
    idadeDoAtleta = anoAtual - anoDeNascimento
    if idadeDoAtleta < 5 or idadeDoAtleta > 100:
        print(f'Você não possui idade para participar de nenhuma categoria , idade {idadeDoAtleta} anos')
        sleep(1.5)
        exit()
except:
    print('Insira uma data válida')
    exit()

if idadeDoAtleta > 20:
    print(f'Você está na categoria MASTER , idade {idadeDoAtleta}')
elif idadeDoAtleta > 19:
    print(f'Você está na categoria SENIOR , idade {idadeDoAtleta}')
elif idadeDoAtleta > 14:
    print(f'Você está na categoria JUNIOR , idade {idadeDoAtleta}')
elif idadeDoAtleta > 9:
    print(f'Você está na categoria INFANTIL , idade {idadeDoAtleta}')
else:
    print(f'Você está na categoria MIRIM , idade {idadeDoAtleta}')