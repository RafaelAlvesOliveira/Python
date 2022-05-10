from map_dados import produtos, pessoas, lista


def filtra(pessoa):
    if pessoa['idade'] < 18:
        return True

# Função para mostrar quem é menor de idade.

nova_lista = filter(filtra, pessoas)


for idade in nova_lista:
    print(idade)
