"""
Levantamento de exceções em Python (raise)
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        return False


print(divide(2, 1))
print(divide(2, 0))


# O objetivo é criar um log todas as vezes que
# as funções forem usadas de forma incorreta.
