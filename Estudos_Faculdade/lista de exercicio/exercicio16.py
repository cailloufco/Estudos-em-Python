'''
 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
print(' ax2 + bx + c = O' )
valor_de_a = int(input('Digite o valor de "a": '))
valor_de_b = int(input('Digite o valor de "b": '))
valor_de_c = int(input('Digite o valor de "c": '))

delta = (valor_de_b) ** 2 - 4 * valor_de_a * valor_de_c

if delta < 0 :
    print('A equação não possui raizes reais')
elif valor_de_a == 0:
    print('A equação não é de segundo grau')
elif delta == 0:
    print(f'A equação tem somente uma raiz real sendo ela:\n----->{-((valor_de_b)/(2*valor_de_a))}')
elif delta > 0:
    print(f'''A equação tem duas raizes reais:
    Primeira raiz = {(-valor_de_b + (delta)**1/2)/2*valor_de_a}''')
    print(f'Segunda raiz = {(-valor_de_b - (delta**1/2)/2*valor_de_a)}')