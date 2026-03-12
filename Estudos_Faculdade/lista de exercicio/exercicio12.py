'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

quantoGanhaPHora = float(input('Quanto você ganha por hora?: '))
quantasHorasPorMes = float(input('Quantas horas você trabalha por mês?: '))

salarioBruto = quantoGanhaPHora * quantasHorasPorMes

impostoDeRenda = 0.11 
inss = 0.08 
sindicato = 0.05 

descontoIR = salarioBruto * impostoDeRenda
descontoINSS = salarioBruto * inss
descontoSindicato = salarioBruto * sindicato

totalDescontos = descontoIR + descontoINSS + descontoSindicato

salarioLiquido = salarioBruto - totalDescontos
print(f'''
+ Salário Bruto     : R$ {salarioBruto:.2f}
- IR (11%)          : R$ {descontoIR:.2f}
- INSS (8%)         : R$ {descontoINSS:.2f}
- Sindicato (5%)    : R$ {descontoSindicato:.2f}
= Salário Líquido   : R$ {salarioLiquido:.2f}
''')