# Faça um programa que mostre a tabuada de vários números, um de cada vez , para cada valor digitado pelo usuário. o programa será interrompido qunado o número solicitado for negativo.

while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    if numero <= 0:
        print('Programa encerrado...')
        break

    print('='*40)
    for i in range(11):
        print(f'{i} X {numero} = {i * numero}')
    print('='*40)