# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção ( sem usar o sort() )
# No final , mostre a lista ordenada na tela

lista = []
inserido = False

for numero in range(5):
    numero = int(input(f'Digite o {numero+1}º valor: '))
    inserido = False
        
    for indice , num_lista in enumerate(lista):
        if numero < num_lista:
            lista.insert(indice , numero)
            inserido = True
            break
    if (not inserido):
        lista.append(numero)
print(lista)