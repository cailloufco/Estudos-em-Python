#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra para conferir se é vogal ou consoante: ')
if letra in 'aeiou':
    print('vogais')
else:
    print('consoante')