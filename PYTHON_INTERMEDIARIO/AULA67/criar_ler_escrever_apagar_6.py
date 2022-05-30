"""
Criar, ler, escrever e apagar arquivos
"""

# https://docs.python.org/3/library/functions.html#open

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Rafael',
        'idade': 31,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

# print(d1)

# Se quiser fazer a conversão desse dicionário para 'json',
# deve ser feita da seguinte maneira. O comando 'indent' serve
# para identar o código e ajuda na visualização das informações.

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

# print(d1_json)

