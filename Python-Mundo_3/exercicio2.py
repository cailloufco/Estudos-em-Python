# Crie uma tupla preechida com os 20 primeiros colcados da tabela do Campeonato Brasileiro de Futebol ,  na ordem de colocação. Depois mostre:
'''
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense
'''
times = ('Sao Paulo', 'Palmeiras', 'Fluminense', 'Bahia', 'RB Bragantino' , 'Flamengo' , 'Coritiba' , 'Atletico Paranaense' , 'Gremio' , 'Corinthias' , 'Mirassol' , 'Chapecoense-sc', 'Atletico-MG' , 'Santos', 'Vasco da Gama' , 'Vitoria' , 'Botafogo' , 'Remo' , 'Internacional', 'Cruzeiro')

print(f'os CINCO primeiros colocados são : {times[:5]}')
print(f'os ultimos QUATRO colocados são: {times[-4:]}')
print(f'os times em ORDEM ALFABETICO são : {sorted(times)}')
print(f'O Corinthias está na posição : {times.index('Corinthias')+1} do placar do Brasileirão')