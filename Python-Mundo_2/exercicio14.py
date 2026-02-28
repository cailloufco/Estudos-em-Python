#Faça um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços

frase = input('Digite uma frase qualquer e direi se ela é um palindromo! :').lower()

if (frase.replace(' ','')) == (frase[::-1].replace(' ','')):
    print('Sua frase é um palindromo')
else:
    print('Sua frase não é um palindromo')