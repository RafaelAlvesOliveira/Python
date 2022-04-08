"""
For / Else em Python
"""

variavel = ['Rafael', 'Luiz', 'Otávio', 'Maria', 'Joãozinho', 'Josefa', 'Mateus']


for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')

# Assim que aparecer uma palavra que começa com a letra
# indicada ele encerra o laço com o comando 'break'.
