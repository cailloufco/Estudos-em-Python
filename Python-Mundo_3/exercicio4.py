# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla .No final, mostre:
'''
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares.
'''
valores = (int(input('Digite o primeiro valor: ')) , int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
numero_nove = 0

for i in valores:
    if i == 9:
        numero_nove += 1

print('Os números pares são: ')
for i in valores:
    if i % 2 == 0:
        print(i , end=' ')
print()
if 3 in valores:
    print(f'O primeiro numero 3 da lista está na posição/index {valores.index(3)}')
else:
    print('Na lista não tem o número 3')
if numero_nove > 0:
    print(f'O número 9 aparece {numero_nove} vezes')
else:
    print('Na lista não tem o número 9')