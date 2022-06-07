"""
    Atributos de Classe - Python Orientado a objetos
"""


class A:
    vc = 123


a1 = A()
a2 = A()

# O interpretador busca a informação na instância, se essa classe
# existe, e se a mesma existir o valor será exibido na tela.
# Se ela não existir na instância, ele irá procurar na classe.

a1.vc = 321
# Quando isso é feito, não se altera o valor da variável da classe,
# mas sim criando um atributo direto na minha instância.

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print()

print(a1.vc)
print(a2.vc)
print(A.vc)
