from map_dados import produtos, pessoas, lista


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


idades = map(aumenta_idade, pessoas)
# idades = map(lambda p: p['idade'] * 1.20, pessoas)

for pessoa in idades:
    print(pessoa)

# As idades foram aumentadas em 20%.
