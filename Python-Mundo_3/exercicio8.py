# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro , ele não será adicionado.
# No final , serão exibidos todos os valores únicos digitados , em ordem crescente
lista_numeros = []
while True:
    try:
        n_loop = int(input('Quantas números você deseja digitar?'))
    except:
        print('Valor digitado é inválido! Tente novamente\n')
        continue
    for i in range(n_loop):
        i = int(input(f'Digite o seu {i+1}º valor: '))
        if i in lista_numeros:
            print(f'Numero digitado ({i}) já existe na lista , então foi ignorado')
        else:
            lista_numeros.append(i)
    print('Os numeros adicionados à lista foram: ',' , '.join(map(str , lista_numeros)))