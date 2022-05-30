"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Porto Velho']

# Código
estados = ['SP', 'MG', 'BA', 'RO']

cidades_estados = zip(estados, cidades)
print(list(cidades_estados))
# print(dict(cidades_estados))
# A lista poderia ser transformada em um dicionário

