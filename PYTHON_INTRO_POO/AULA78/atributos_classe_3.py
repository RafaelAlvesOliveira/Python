"""
    Atributos de Classe - Python Orientado a objetos
"""


class A:
    vc = 123  # variável de classe

    def __init__(self):
        pass


a1 = A()
a2 = A()

A.vc = 'Alterado'
# Nesse caso, o valor é alterado em todas as instâncias da classe.  

print(a1.vc)
print(a2.vc)
print(A.vc)
