#Crie um programa que leia a idade de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

pessoas = []
try:
    for _ in range(7):
        pessoas.append(int(input('Digite a idade de 7 pessoas: ')))
except:
    print('Digite uma idade válida!')
pessoasDeMaior = []
pessoasDeMenor = []
for idadePessoaAnalisada in pessoas:
    if idadePessoaAnalisada <= 0:
        print('Uma das idades está invalida!!!!')
        exit()
    elif idadePessoaAnalisada >= 18:
        pessoasDeMaior.append(idadePessoaAnalisada)
    else:
        pessoasDeMenor.append(idadePessoaAnalisada)
print(f'Das SETE pessoas há {len(pessoasDeMaior)} com maior idade , e tem {len(pessoasDeMenor)} com menor idade')