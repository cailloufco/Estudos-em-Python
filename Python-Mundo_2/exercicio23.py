# Melhore o EXERCICIO22 , perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse quer mostar 0 termos.

primeiro_termo_pa = int(input('Digite o primeiro termo da PA'))
termo = primeiro_termo_pa
razao_pa = int(input('Digite a razão da Progressão'))
total = 10
contador = 1
mais = None
while contador <= total:
    print(f'{termo}' , end= ' → ')
    termo += razao_pa
    contador += 1
    if contador > total:
        mais = int(input('\nVocê deseja ver mais alguns termos? Se sim digite a quantidade de termos adicionais ( DIGITE 0 PARA SAIR ): '))
        total += mais
        contador = 1
        
    if mais == 0:
        break
print('Acabou...')