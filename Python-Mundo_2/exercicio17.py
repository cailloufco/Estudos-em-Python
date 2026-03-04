#Desenvolva um programa que leia o nome , idade e sexo de 4 pessoas. No final do programa , mostre:
'''
- A média de idade do grupo.
- Qual é o nome do homem mais velho
-Quantas mulheres tem menos de 20 anos.
'''
soma_idade = 0
maior_idade = 0
nome_maior_idade = None
contador_mulheres_idade = 0
for i in range (1,5):
    print(f'------- {i}° PESSOA -------')
    nome = input('Digite seu nome:')
    idade = int(input('Digite sua idade:'))
    sexo = input('Digite seu sexo (M / F)').upper()
    soma_idade += idade
    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_maior_idade = nome
    if sexo == 'F':
        if idade < 20:
            contador_mulheres_idade += 1
print('----------------------')
print(f'O homem com maior idade é {nome_maior_idade} , com {maior_idade} anos\nA idade média é de {soma_idade/4:.1f} anos\nE há {contador_mulheres_idade} mulheres com menos de 20 anos de idade')
