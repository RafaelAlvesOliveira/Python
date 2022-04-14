"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


# No momento que um padrão é definido para
# um determinado objeto, todos após devem ter o mesmo padrão.
# Após chamar uma função com argumento nomeado, o interpretador
# não permitirá que os outros argumentos sejam sem nomear.

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)


func(1, 2, 3, 4, 5, nome='Rafael', a6='5')

# A função por padrão retorna um valor 'None' ou nenhum
# por padrão

