pesoPeixes = float(input('Quantos quilos de peixe?: '))
if pesoPeixes > 50:
    print(f'Você excedeu o peso regulamentado: {pesoPeixes - 50};\nE pagará {(pesoPeixes-50)*4:.2f} ')
else:
    print('Você está livre de multas')
