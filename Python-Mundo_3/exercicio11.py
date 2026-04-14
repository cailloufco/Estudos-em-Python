# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso , crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados , respectivamente.
# Ao final , mostre o conteúdo das três listas geradas.

lista_geral = []
while True:
    numero = int(input('Escolha um número para adiciona-lo a lista: '))
    lista_geral.append(numero)
    continuar = input('Você deseja continuar adicionando números? ( S / N ): ').upper()
    if continuar == 'S':
        continue
    else:
        break
lista_impar = []
lista_par = []

for i in lista_geral:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'\nA lista geral de todos os numeros foi {' '.join(map(str , lista_geral))}\nA lista dos impares foi {' '.join(map(str , lista_impar))}\nA lista dos pares foi {' '.join(map(str , lista_par))}')