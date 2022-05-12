"""
Levantamento de exceções em Python (raise)
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print('Log: ', erro)
        raise


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)

# Aparecem os dois erros no prompt do python.
# No primeiro o erro foi logado, e no segundo
# o erro foi relançado como exceção, sendo
# possível capturar ela posteriormente.
