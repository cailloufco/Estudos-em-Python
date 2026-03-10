# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usúario digitar o valor 999 , que é a condição de parada. No final, mostre quantos npumeros foram digitados e qual foi a soma entre eles ( desconsiderando o flag ).

contador_de_numeros = 0
num_digitado = None
soma = 0

while True:
    num_digitado = int(input('Digite vários números ( QUANDO QUISER PARAR DIGITE 999 ): '))
    if num_digitado == 999:
        print('Saindo.....')
        break
    contador_de_numeros +=1
    soma += num_digitado 
print(f'Você digitou {contador_de_numeros} números\nSomatoria dos mesmos é igual a {soma}  ( 999 é desconsiderado ).')