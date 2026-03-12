'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
salario_do_usuario = float(input('Digite seu salário o reajuste!: '))
if salario_do_usuario >= 1500:
    print(f'Salario antes do reajuste = {salario_do_usuario}\nPercentual de aumento = 5%\nO valor aumentado é {salario_do_usuario*5/100:.2f}\nNovo salário após o aumento = {salario_do_usuario+(salario_do_usuario*5/100)}')
elif salario_do_usuario >=700:
    print(f'Salario antes do reajuste = {salario_do_usuario}\nPercentual de aumento = 10%\nO valor aumentado é {salario_do_usuario*10/100:.2f}\nNovo salário após o aumento = {salario_do_usuario+(salario_do_usuario*10/100)}')
elif salario_do_usuario >=280:
    print(f'Salario antes do reajuste = {salario_do_usuario}\nPercentual de aumento = 15%\nO valor aumentado é {salario_do_usuario*15/100:.2f}\nNovo salário após o aumento = {salario_do_usuario+(salario_do_usuario*15/100)}')
else:
    print(f'Salario antes do reajuste = {salario_do_usuario}\nPercentual de aumento = 20%\nO valor aumentado é {salario_do_usuario*20/100:.2f}\nNovo salário após o aumento = {salario_do_usuario+(salario_do_usuario*20/100)}')