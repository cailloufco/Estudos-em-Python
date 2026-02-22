#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
'''
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''
try:
    primeiraNota = float(input('Qual foi sua primeira nota?'))
    segundaNota = float(input('Qual foi sua segunda nota?'))
except:
    print('Digite uma nota!')
    exit()
#validação , nota não pode ser maior que 10 e nem menor que 0;
if not(0 <= primeiraNota <=10) or not(0 <= segundaNota <= 10):
    print('As notas não podem ser menores que ZERO e nem superiores a DEZ') 
    exit()
mediaDoAluno = (primeiraNota + segundaNota) / 2

if mediaDoAluno >= 7:
    print(f'Aluno aprovado com a media {mediaDoAluno:.1f}')
elif mediaDoAluno < 5:
    print(f'Aluno reprovado com a media {mediaDoAluno:.1f}')
else:
    print(f'Aluno em recuperação com a media {mediaDoAluno:.1f}')
