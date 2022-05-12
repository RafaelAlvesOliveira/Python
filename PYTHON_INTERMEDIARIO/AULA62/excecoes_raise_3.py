"""
Levantamento de exceções em Python (raise)
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise


# Usando 'raise' eu consigo logar a exceção
# num arquivo ou base de dados. E relanço
# a mesma exceção que recebi.

try:
    print(divide(2, 0))
except:
    print('erro')

# Se quiser logar a exceção que ocorreu nessa função,
# porém eu quero relançar para que outro desenvolvedor
# ou eu mesmo posteriormente possa capturar a exceção.
# E não quero modificar o comportamento da linguagem
# por si só.
