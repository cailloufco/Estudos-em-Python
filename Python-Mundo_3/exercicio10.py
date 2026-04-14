# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso mostre:
''' 
A) Quantos numeros foram digitados
B) A lista de valores , ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista
'''
lista = []
contador = 0
cinco_existe = False
while True:
    n_escolhido = int(input(f'Escolha o seu {contador+1} número: '))
    contador += 1
    lista.append(n_escolhido)
    continuar = input('Você deseja contiunar escolhendo? ( S / N ): ').upper()
    if continuar != 'S':
        break
for i in lista:
    if i == 5:
        cinco_existe = True
if cinco_existe == True:
    cinco_existe = 'cinco existe na lista'
else:
    cinco_existe = 'não existe o numero cinco na lista'

print(f'\nA quantidade de numeros digitados foi {len(lista)}\nA lista ordenada de maneira decrescente é: {' '.join(map(str , sorted(lista , reverse=True)))}\nE {cinco_existe}')