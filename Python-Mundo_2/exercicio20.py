# Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] somar
[2] multiplicar
[3] descobrir o maior
[4] digitar novos valores
[5] sair do programa
'''
from time import sleep

num_1 = float(input('Digite um valor! : '))
num_2 = float(input('Digite mais um valor! : '))
valor_opcao = 0

while not(valor_opcao == 5):
    print('''[1] Somar
[2] Multiplicar
[3] Descobrir o maior
[4] Digitar novos valores
[5] Sair do programa
''')
    try:
        valor_opcao = int(input('Escolha a opção: '))
        if valor_opcao > 5:
            print('Valor inválido! , escolha corretamente.') , sleep(2)
    except:
        print('Valor inválido! , escolha corretamente.') , sleep(2)
    match valor_opcao:
        case 1:
            print(f'{'-'*5}SOMA{'-'*5}')
            print(f'{num_1} + {num_2} = {num_1 + num_2}'), sleep(1.7)

        case 2:
            print(f'{'-'*5}MULTIPLICAÇÃO{'-'*5}')
            print(f'{num_1} X {num_2} = {num_1 * num_2}'), sleep(1.7)

        case 3:
            print(f'{'-'*5}DESCOBRIR MAIOR VALOR{'-'*5}')
            if num_1 == num_2:
                print('ambos tem o mesmo valor!')
            elif num_1 > num_2:
                print(f'o primeiro valor ({num_1}) é maior que o segundo ({num_2})'), sleep(1.7)
            else:
                print(f'o segundo valor ({num_2}) é maior que o primeiro ({num_1})'), sleep(1.7)

        case 4:
            print(f'{'-'*5}NOVOS VALORES{'-'*5}')
            try:
                num_1 = float(input('Digite um valor! : '))
                num_2 = float(input('Digite mais um valor! : '))
            except:
                print('Valor inválido! , escolha corretamente.') , sleep(2)

        case _:
            print('')
    print('-'*20)
  