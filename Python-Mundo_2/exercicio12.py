#Desenvolva um programa que leia o primeiro termo e a rezão de uma PA. No final , mostre os 10 primeiros termos dessa prograssão.
primeiroTermo = int(input('Digite o primeiro termo de uma PA: '))
razaoDaProgressao = int(input('Digite a razão da PA: ')) 
print('Os dez primeiros termos dessa razão são:')

for _ in range(0 , 10):
    print(f'{primeiroTermo}')
    primeiroTermo = primeiroTermo + razaoDaProgressao