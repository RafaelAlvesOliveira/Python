"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""


# No momento que um padrão é definido para
# um determinado objeto, todos após devem ter o mesmo padrão.
# Após chamar uma função com argumento nomeado, o interpretador
# não permitirá que os outros argumentos sejam sem nomear.

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


# Para que a variável retorne algum valor deve
# ter a palavra 'return' e o argumento que deve ser retornado.
# Um ou mais argumentos podem ser retornados.

var = func(1, 2, 3, 4, 5, nome='Rafael', a6='5')
print(var)

# se a função for atribuída a uma variável, ela executa normalmente,
# porém a variável por si só não terá nenhum valor, pois a função está
# retornando 'none'.
