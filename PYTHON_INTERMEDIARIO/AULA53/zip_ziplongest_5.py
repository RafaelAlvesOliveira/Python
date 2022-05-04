"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""
from itertools import count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Porto Velho', 'Senhor do Bonfim']
estados = ['SP', 'MG', 'BA', 'RO']

cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

# Não usar dois geradores em simultâneo, pois eles
# vão entrar em conflito. Altera função 'zip_longest'
# para 'zip'
