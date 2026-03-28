# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços , na sequência.
# No final , mostre uma listagem de preços , organizando os dados em forma tabular.

itens = {
    'produtos':['Arroz', 'Feijão','Café','Refrigerante','Salgadinho'],
    'valores':[4.99 , 5.99 , 9.99 , 5.69 , 3.59]
}
print('-'*20)
print('LISTAGEM DE PRODUTOS')
print('-'*20)
for p , v in zip(itens['produtos'],itens['valores']):
    print(p,': $',v , end='\n')
print('-'*20)