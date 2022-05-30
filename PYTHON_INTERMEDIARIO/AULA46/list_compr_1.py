tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)
print(ex5['valor2'])
