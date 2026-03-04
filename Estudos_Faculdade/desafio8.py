#Crie um algoritmo que peça o preço de uma compra e peça o tipo de pagamento
#Se for a vista ou pix dê 12% de desconto no valor da compra
#Imprima : total da compra , valor do desconto aplicado e valor final


valor_compra = float(input('Digite o valor da sua compra: '))
forma_de_pagamento = input('Digite a forma de pagamento ( PIX , A VISTA , DEBITO ou CREDITO )').upper()

if forma_de_pagamento == 'PIX' or forma_de_pagamento == 'A VISTA':
    print(f'o valor da compra ficou {valor_compra - (valor_compra * 12/100):.2f} com desconto da forma de pagamento')
else:
    print(f'o valor da compra ficou {valor_compra:.2f} , sem descontos')
