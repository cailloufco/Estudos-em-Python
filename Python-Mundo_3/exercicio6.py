# Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
# Depois disso, você deve mostrar , para cada palavra quais são usas vogais.

palavras = ('caneta','tesoura','jogador')

for palavra in palavras:
    vogais = []
    print(palavra, end=' = ')
    for letra in palavra:
        if letra in 'aeiou':
            vogais.append(letra)
    
    print(', '.join(vogais))
