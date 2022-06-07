"""
    Atributos de Classe - Python Orientado a objetos
"""


class A:
    vc = 123


a1 = A()
a2 = A()

A.vc = 321
# Nessa situação ele inverte a ordem dos números na classe.

print(a1.vc)
print(a2.vc)
print(A.vc)
