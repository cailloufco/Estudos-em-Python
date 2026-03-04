#Faça um programa que leia o peso de cinco pessoas. No final , mostre qual foi o maior e o menor peso lidos.

lista_de_pesos = []

for contagem in range (1 , 6):
    lista_de_pesos.append(int(input(f'{contagem} - Digite o peso de CINCO pessoas em KG: ')))

lista_de_pesos.sort()

print(f'o menor peso foi {min(lista_de_pesos)} e o maior foi {max(lista_de_pesos)}')




