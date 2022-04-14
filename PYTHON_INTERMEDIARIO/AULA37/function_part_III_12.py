"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


# 'kwargs' são argumentos com palavras chaves
# argumentos nomeados são armazenados do 'kwargs'

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


# Se for necessário acessar algum argumento nomeado é só
# colocar em 'print' e depois de 'kwargs' o índice que
# se quer acessar.


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Rafael', sobrenome='Alves', idade=31)
