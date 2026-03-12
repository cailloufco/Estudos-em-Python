'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso'''

escolha_usuario = input('Em qual turno você estuda? M-Matutino ou V-Vespertino ou N- Noturno')
if escolha_usuario == 'M':
    print('Bom Dia!')
elif escolha_usuario == 'V':
    print('Boa Tarde!')
elif escolha_usuario == 'N':
    print('Boa Noite!')
else:
    print('Valor inexistente')