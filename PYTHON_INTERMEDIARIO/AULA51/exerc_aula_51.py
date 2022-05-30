carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = 0
for produto in carrinho:
    total += produto[1]
print(total)


# Primeira possível solução para o problema,
# mas é ineficiente.

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))


# Segunda maneira de se fazer a soma dos
# valores

