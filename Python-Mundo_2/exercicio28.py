# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final , mostre:
'''
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
'''
pessoas_mais_de_18 = 0
mulher_menos_de_20 = 0
homens = 0

while True:
    var = int(input('Digite a idade da pessoa a ser cadastrada: '))
    sexo = input('Digite o sexo da pessoa ser cadastrada [ M ] ou [ F ]').upper()
    if sexo == 'M':
        homens += 1
    else:
        if sexo == 'F' and var < 20:
                mulher_menos_de_20 +=1
        if var > 18:
            pessoas_mais_de_18 += 1
    
    continuar = input('Você deseja continuar? S / N').upper()
    if continuar == 'N':
        break
print(f'PESSOAS COM MAIS DE 18 ANOS : {pessoas_mais_de_18}\nQUANTOS HOMENS FORAM CADASTRADOS : {homens}\nQUANTAS MULHERES TEM MENOS DE 20 ANOS : {mulher_menos_de_20}')
    
    