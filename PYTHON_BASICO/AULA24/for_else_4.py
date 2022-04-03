"""
For / Else em Python
"""

variavel = ['Rafael', 'Luiz', 'Otávio', 'Maria', 'Joãozinho', 'Josefa', 'Mateus']


for valor in variavel:
    if valor.lower().startswith('j'):
        # pass
        continue
    print(valor)
else:
    print('Não existe uma palavra que começa com J.')

# Se não houver a função "continue", for a função "pass" ele
# executará todos os nomes e o 'else' também.
