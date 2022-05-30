carrinho = []

carrinho.append(('Produto 1', 30.50))
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))

# produto, preco = carrinho[0]
# print(produto, preco)
# Exemplo de desempacotamento

total = sum([float(y) for x, y in carrinho])
# print(carrinho)
print(total)

# x e y desempacota cada linha
# de produto inseridas no carrinho

