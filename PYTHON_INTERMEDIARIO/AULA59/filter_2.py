from map_dados import produtos, pessoas, lista

nova_lista = filter(lambda p: p['preco'] > 50, produtos)

for produto in nova_lista:
    print(produto)

# A função 'filter' é usada para mostrar apenas os
# itens que tenham valor maior do que 50.

