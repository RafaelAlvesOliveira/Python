"""
Dicionários em Python
"""

clientes = {
    'cliente1': {
        'nome': 'Rafael',
        'sobrenome': 'Alves',
    },
    'cliente2': {
        'nome': 'Joaquim',
        'sobrenome': 'Moura',
    },
    'cliente3': {
        'nome': 'João',
        'sobrenome': 'Martins',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# O comando \t serve para identar as informações
# exibidas no segundo 'for'.
