#Refaça o desafio da tabuada , mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for
numeroEscolhidoPorUsuario = int(input('Escolhe um número para ver sua tabuada: '))
for i in range(0 , 11):
    print(f'{i} X {numeroEscolhidoPorUsuario} = {i*numeroEscolhidoPorUsuario}')