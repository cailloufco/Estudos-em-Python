'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -Masculino, Sexo Inválido'''

sexo = input('Digite F [FEMININO] ou M [Masculino]').upper()
if sexo == 'M':
    print(f'Masculinho - M')
elif sexo == 'F':
    print(f'Feminino - M')
else:
    print('sexo invalido')