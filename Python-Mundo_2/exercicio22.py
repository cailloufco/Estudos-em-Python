# Refaça o EXERCICIO12 , lendo o primeiro termo e a razão de uma PA , mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

primeiro_termo_PA = int(input('Digite o primeiro termo da PA: '))
razao_da_PA = int(input('Digite a razão a PA: '))
contador = 1
progressao = 0
print(f'VALOR INICIAL DA PA = {primeiro_termo_PA}')
while not(contador == 11):
    print(f'{contador}° TERMO DA PA = {primeiro_termo_PA + razao_da_PA}')
    contador += 1
    primeiro_termo_PA = primeiro_termo_PA + razao_da_PA