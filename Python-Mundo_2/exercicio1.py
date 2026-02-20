#Escreva um programa para aprovar um empresitmo bancario para a compra de uma casa. O progrmaa vai perguntar o valor da casa , o salario do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo será negado

print('Aprovar emprestimo \n' )

valorDaCasa = float(input('Qual o valor da casa em reais? '))
salarioDoComprador = float(input('Qual seu salário?' ))
quantiaDeAnos = int(input('Em quantos anos deseja pagar a casa? '))

PrestacaoMensal = valorDaCasa / (quantiaDeAnos * 12)
Limite = salarioDoComprador*(30/100)

print(f'\n\nA prestação mensal seria : {PrestacaoMensal:.2f}$ \nNão podendo exceder o limite de: {Limite:.2f}$\n\n')

def resultadoDoEmprestimo(Limite , PrestacaoMensal):
    if Limite >= PrestacaoMensal:
        print('Emprestimo aprovado')
    else:
        print('Empestimo negado')
resultadoDoEmprestimo(Limite , PrestacaoMensal)