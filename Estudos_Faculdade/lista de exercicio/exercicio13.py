'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido.
'''
numero_dia_da_semana = int(input('Digite um numero correspondente da senaba (1 - Domingo 2- Segunda , etc....) : '))
match numero_dia_da_semana:
    case 1:
        numero_dia_da_semana = 'Domingo'
    case 2:
        numero_dia_da_semana = 'Segunda'
    case 3:
        numero_dia_da_semana = 'Terça'
    case 4:
        numero_dia_da_semana = 'Quarta'
    case 5:
        numero_dia_da_semana = 'Quinta'
    case 6:
        numero_dia_da_semana = 'Sexta'
    case 7:
        numero_dia_da_semana = 'Sabado'
    case _:
        numero_dia_da_semana = 'Inválido'
print(numero_dia_da_semana)
