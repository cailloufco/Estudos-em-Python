tamanhoDaAreaPintada = float(input('Qual tamanho da area pintada em METROS QUADRADOS?: '))

valorDaParede = tamanhoDaAreaPintada/3*80
totalDeLatas = (tamanhoDaAreaPintada/3 - 1)//18+1

print(f'Valor a ser pago pela area de {tamanhoDaAreaPintada} metros quadrados é de: {valorDaParede} Reais\nO total de latas gastas é de: {totalDeLatas:.2f}')