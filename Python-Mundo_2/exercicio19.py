# Crie um jogo onde o computador vai "pensar" em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar , mostrando no FINAL quantos palpites foram necessários para vencer.
from random import randint
contagem_de_palpites = 0
num_sorteado = randint(0 , 10)
palpite = None

print('Tente adivinhar o qual foi número escolhido aleatoriamente ( 0 à 10 )!')

while not(palpite == num_sorteado):
    contagem_de_palpites += 1
    palpite = int(input('escolha um numero de 0 à 10 : '))
    if palpite == num_sorteado:
        print(f'Parabens , você acertou! Total de tentativas: {contagem_de_palpites} ')
    elif palpite > num_sorteado:
        print(f'O numero sorteado é menor que {palpite}')
    elif palpite < num_sorteado:
        print(f'O numero sorteado é maior que {palpite}')