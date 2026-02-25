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