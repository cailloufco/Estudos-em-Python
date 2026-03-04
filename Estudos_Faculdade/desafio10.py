# Obtenha o HP total do jogador e um valor de dano 
# Se o valor de dano corresponder a 50% do HP total aplique um DMG extra de -20
# imprima o HP final do jogador

hp_jogador = int(input('Digite o HP total do seu personagem: '))
dano_sofrido = int(input('Digite o DANO recebido ao seu personagem: '))

if dano_sofrido == hp_jogador/2:
    print(f'HP RESTANTE = {hp_jogador-(dano_sofrido+20)}')
else:
    print(f'HP RESTANTE = {hp_jogador}')

hp_jogador = hp_jogador - dano_sofrido
if hp_jogador <= 0:
    print('Morreu.......')