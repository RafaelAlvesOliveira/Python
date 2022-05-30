"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""

# O comando 'zip' une duas listas em uma.


# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Porto Velho']

# Código
estados = ['SP', 'MG', 'BA', 'RO']

cidades_estados = zip(cidades, estados)
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))



