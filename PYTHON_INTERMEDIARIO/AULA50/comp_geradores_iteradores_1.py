#  lists, tuples, str -> Sequences -> Iterável
nome = 'Rafael Alves'
iterador = iter(nome)

# Isso é o que o comando 'for' faz automaticamente,
# sem ser necessário repetir o processo várias vezes.

try:
    print(next(iterador))  # R
    print(next(iterador))  # A
    print(next(iterador))  # F
    print(next(iterador))  # A
    print(next(iterador))  # E
    print(next(iterador))  # L
    # print(next(iterador))  #
    # print(next(iterador))  # A
    # print(next(iterador))  # L
    # print(next(iterador))  # V
    # print(next(iterador))  # E
    # print(next(iterador))  # S
except:
    pass

print('Cadê os valores?')
for valor in iterador:
    print(valor)

# Esse comportamento é idêntico tanto para geradores
# como para iteradores, apartir do momento que consumiu
# os valores dele, está consumido. Não tem o que fazer.
# Após consumido não é possível recuperar esses valores.
