#crie um algoritmo que peça ao usuario tres notas e imprima a media das tres notas
try:
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    nota3 = float(input('Terceira nota: '))
except:
    print('Digite uma nota valida!')
    exit()
mediaDoAluno = (nota1 + nota2 + nota3)/3
print('A media do aluno foi:' , mediaDoAluno)