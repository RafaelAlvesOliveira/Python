from map_dados import produtos, pessoas, lista

precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)

# O comando 'for' é usado para iterar sobre os preços
# e se usa o "map" para acessar o dicionário, mais
# precisamente o “item” preço.
