from map_dados import produtos, pessoas, lista


# Os elementos que maiores do que 5 ficaram
# os que forem menores serão retirados.
nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

# Apesar de a função 'map' e a 'filter' serem parecidas
# a diferença é que a filter retorna verdadeiro ou falso
# para a expressão informada.

