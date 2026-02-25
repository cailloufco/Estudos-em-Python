# temperaturaFahrenheit = float(input('Quantos graus Fahrenheit estão fazendo?:'))
# print(f'Quanto convertido para celcius fazem:{5*(temperaturaFahrenheit-32)/9}')

# temperaturaCelcius = float(input('Quantos graus Celcius estão fazendo? :'))
# print(f'Quanto convertido para fahrenheit fazem: {temperaturaCelcius*1.8+ 32}')

numInt1 = int(input("Digite um numero INTEIRO: "))
numInt2 = int(input("Digite um numero INTEIRO: "))
numReal = float(input("Digite um numero REAL: "))

print(f'''O produto do dobro do primeiro com a metade do segundo é: {(numInt1 * 2) * (numInt2 / 2)}
A soma do triplo do primeiro com o terceiro é: {numInt1 * 3 + numReal}
O terceiro elevado ao cubo é: {numReal ** 3}''')