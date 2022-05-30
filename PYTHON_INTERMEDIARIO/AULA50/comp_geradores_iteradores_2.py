#  lists, tuples, str -> Sequences -> Iterável
nome = 'Rafael Alves'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o FOR')

for letra in gerador:
    print(letra)

print('Olha o outgro FOR')

for letra in gerador:
    print(letra)

print(next(gerador))

# Geradores e iteradores são feitos para ser
# consumidos os valores, acabando os valores
# a função se encerra.
