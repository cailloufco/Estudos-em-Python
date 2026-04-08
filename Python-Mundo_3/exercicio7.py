# Faça um programa que leia 5 valores númericos e guarde-os em uma lista
# No final , mostre qual foi o maior e o menos valor digitado e as suas respectivas posiçoes na lista

valores_num = []

for numero in range(5):
    numero = float(input(f'Digite um valor númerico!: {numero}º '))
    valores_num.append(numero)

print(f'Os valores digitador foram {' , '.join(map(str , valores_num))}\nO maior valor listado foi {max(valores_num)} , na posição {valores_num.index(max(valores_num))}\nO menor valor listado foi {min(valores_num)} , na posição {valores_num.index(min(valores_num))}')