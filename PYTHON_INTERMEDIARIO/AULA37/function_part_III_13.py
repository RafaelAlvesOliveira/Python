"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""


# 'kwargs' são argumentos com palavras chaves
# argumentos nomeados são armazenados do 'kwargs'

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


# É muito melhor usar 'get' quando não se têm certeza
# de que a chave existe, do que utilizar da maneira acima.
# Pois, apresentará um erro.
# Desde o momento que a palavra-chave volta a existir, ou
# tiver certeza que haverá essa palavra-chave na lista,
# não será necessário usar 'get'.

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Rafael', sobrenome='Alves', idade=31)
