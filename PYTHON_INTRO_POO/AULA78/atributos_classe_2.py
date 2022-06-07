"""
    Atributos de Classe - Python Orientado a objetos
"""


class A:
    vc = 123  # variável de classe

    def __init__(self):
        self.vc = 321  # variável de instância
    # Sempre que, for usar uma variável de classe utilizando uma instância
    # precisa ter ciência dessa situação. Sempre que for alterar uma variável
    # de classe para ela ser afetada em todas as instâncias dessa classe, é
    # melhor utilize a classe e não uma instância para fazer isso.


a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
print(A.vc)
