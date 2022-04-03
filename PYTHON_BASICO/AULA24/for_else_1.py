"""
For / Else em Python
"""

variavel = ['Rafael', 'Luiz', 'Otávio', 'Maria', 'Joãozinho']

for valor in variavel:
    if valor.startswith('J'):
        print(f'Começa com J {valor}')
    else:
        print(f'Não começa com J {valor}')

# A função 'starswith' serve para fazer uma verificação
# para saber se uma determinada 'string' começa com à
# letra indicada
