# Faça um programa que jogue PAR OU IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep

contador_vitorias = 0
escolha_do_usuario = None #PAR OU IMPAR
escolha_do_python = None #PAR OU IMPAR

numero_do_usuario = 0
numero_do_python = randint(0, 20)
resultado_numeros = None


while True:
    try:
        escolha_do_usuario = int(input('Escolha PAR ou IMPAR\n[1]PAR\n[2]IMPAR : '))
        if (escolha_do_usuario > 2) or (escolha_do_usuario < 0):
            print('Valor inválido...') , sleep(1)
            continue
        numero_do_usuario = int(input('Digite um número qualquer: '))
        if numero_do_usuario < 0:
            print('Digite um valor válido...'), sleep(1)
            continue
    except:
        print('Valor inválido...'), sleep(1)
    print('='*40)
    match escolha_do_usuario:
        case 1:
            escolha_do_usuario = 'PAR'
        case 2:
            escolha_do_usuario = 'IMPAR'
    if escolha_do_usuario == 'PAR':
        escolha_do_python = 'IMPAR'
    else:
        escolha_do_python = 'PAR'

    print(f'O PYTHON é {escolha_do_python} e escolheu o número {numero_do_python}\nVOCÊ é {escolha_do_usuario} e escolheu o número {numero_do_usuario} ')

    resultado_numeros = numero_do_python + numero_do_usuario
    if resultado_numeros % 2 == 0:
        resultado_numeros = 'PAR'
    else:
        resultado_numeros = 'IMPAR'
    print(f'QUANDO SOMADO O NUMERO É {numero_do_python+numero_do_usuario} SENDO {resultado_numeros}')
    print('='*40), sleep(2.4)


    if escolha_do_usuario == 'PAR' and (numero_do_usuario + numero_do_python)%2 == 0:
        contador_vitorias += 1
        print(f'Você venceu! Continue até perder ( VITORIAS CONSECUTIVAS : {contador_vitorias} )'), sleep(1.5)
    elif escolha_do_usuario == 'PAR' and (numero_do_usuario + numero_do_python)%2 != 0:
        print(f'Você perdeu!...\nVitorias Consecutivas = {contador_vitorias}'), sleep(1.5)
        break
    elif escolha_do_usuario == 'IMPAR' and (numero_do_usuario + numero_do_python)%2 != 0:
        contador_vitorias += 1
        print(f'Você venceu! Continue até perder ( VITORIAS CONSECUTIVAS : {contador_vitorias} )'), sleep(1.5)
    elif escolha_do_usuario == 'IMPAR' and (numero_do_usuario + numero_do_python)%2 == 0:
        print(f'Você perdeu!...\nVitorias Consecutivas = {contador_vitorias}'), sleep(1.5)
        break
    print('='*40)