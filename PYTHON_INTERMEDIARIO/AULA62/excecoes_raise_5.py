"""
Levantamento de exceções em Python (raise)
"""


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1/n2

print(divide(2, 1))
print(divide(2, 0))

# Nesse caso fiz a minha própria exceção, informando
# que o valor de n2 não pode ser 0.

