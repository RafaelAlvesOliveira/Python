from map_dados import produtos, pessoas, lista


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

# A função 'map' mapeia uma função que passa
# em cada elemento do iterável
