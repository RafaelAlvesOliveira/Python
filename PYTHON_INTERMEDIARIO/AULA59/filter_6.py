from map_dados import produtos, pessoas, lista


def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


# Função para mostrar quem é maior de idade.

nova_lista = filter(filtra, pessoas)

for idade in nova_lista:
    print(idade)
