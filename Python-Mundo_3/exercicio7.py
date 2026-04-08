# Faça um programa que leia 5 valores númericos e guarde-os em uma lista
# No final , mostre qual foi o maior e o menos valor digitado e as suas respectivas posiçoes na lista

valores_num = []

for numero in range(5):
    numero = float(input(f'Digite um valor númerico!: {numero}º '))
    valores_num.append(numero)
menor_indice = []
maior_indice = []

for indice , valor  in enumerate(valores_num):
    if valor == min(valores_num):
        menor_indice.append(indice)
    if valor == max(valores_num):
        maior_indice.append(indice)
        
print(f'Os valores digitados foram: {' , '.join(map(str , valores_num))}\nO maior valor foi {max(valores_num)} na posição {' '.join(map(str , maior_indice))}\nO menor valor foi {min(valores_num)} na posição {' '.join(map(str , menor_indice))}')