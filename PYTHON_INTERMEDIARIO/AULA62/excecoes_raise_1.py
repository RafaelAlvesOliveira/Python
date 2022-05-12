"""
Levantamento de exceções em Python (raise)
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        return False


try:
    print(divide(2, 0))
except:
    print('erro')

# O primeiro 'try' na função já fez o tratamento
# do erro, assim o segundo 'try' é ignorado.
# O comportamento do python sendo modificado.


