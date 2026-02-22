#Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('Jokenpô')
sleep(2)
try:
    escolhaDoUsuario = int(input('''Escolha com base nos numeros!
1- Pedra
2- Tesoura
3- Papel
'''))
except:
    print('Faça uma escolha válida de 1 à 3!')
    exit()
if escolhaDoUsuario > 3:
    print('Faça uma escolha válida de 1 à 3!')
    exit()

escolhaDoPython = randint(1, 3)

match escolhaDoUsuario:
    case 1:
        escolhaDoUsuario = 'Pedra'
    case 2:
        escolhaDoUsuario = 'Tesoura'
    case 3:
        escolhaDoUsuario = 'Papel'

match escolhaDoPython:
    case 1:
        escolhaDoPython = 'Pedra'
    case 2:
        escolhaDoPython = 'Tesoura'
    case 3:
        escolhaDoPython = 'Papel'

print(f'''\nVocê = {escolhaDoUsuario}
Python = {escolhaDoPython}\n''')
sleep(1.5)
if (escolhaDoUsuario == 'Pedra' and escolhaDoPython == 'Tesoura') or (escolhaDoUsuario == 'Papel' and escolhaDoPython == 'Pedra') or (escolhaDoUsuario == 'Tesoura' and escolhaDoPython == 'Papel'):
    print('Você venceu!!!')
elif escolhaDoPython == escolhaDoPython:
    print('Empate!!!')
else:
    print('Você perdeu...')
