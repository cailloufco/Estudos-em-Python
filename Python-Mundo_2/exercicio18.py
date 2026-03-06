# Faça um programa que leia o sexo de uma pessoa , mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado , peça a digitação novamente até ter um valor correto.

sexo = None
while not(sexo == 'M' or sexo == 'F'):
    sexo = input('Digite seu SEXO ( M ou F ): ').upper()
    if sexo != 'M' and sexo != 'F':
        print('INVÁLIDO , TENTE NOVAMENTE.')
    else:
        print('Valor correto')