from map_dados import produtos, pessoas, lista

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)

# A função 'map' mapeia apenas os valores
# no campo nome. Está a passar uma função
# na lista
