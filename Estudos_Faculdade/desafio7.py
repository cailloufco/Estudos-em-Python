#desenvolva um algorito em python que leia a altura e o peso calcule o IMC e informe para o usuario se ele ta obeso ou não.          IMC = peso (kg) / (altura em metros)²

peso_kg = 120
altura_metros = 1.70

imc = peso_kg / altura_metros**2

'''
Abaixo de 18,5: Baixo peso
18,5 a 24,9: Peso normal
25,0 a 29,9: Sobrepeso
30,0 a 34,9: Obesidade grau I
35,0 a 39,9: Obesidade grau II
40 ou mais: Obesidade grau III
'''

if imc <= 25:
    print(f'Você está normal! Seu IMC é: {imc:.1f}!')

if imc > 25:
    print(f'Você está sobrepeso! Seu IMC é: {imc:.1f}!')

if imc > 30:
    print(f'Você está obeso! Seu IMC é: {imc:.1f}!')