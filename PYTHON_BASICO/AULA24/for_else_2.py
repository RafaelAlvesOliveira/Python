"""
For / Else em Python
"""

variavel = ['Rafael', 'Luiz', 'Otávio', 'Maria', 'Joãozinho']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')


# a função 'lower' serve para transformar uma letra maiúscula
# em minúscula.
