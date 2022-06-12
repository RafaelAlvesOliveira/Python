"""
    Sobrecarga de operadores — Python Orientado a Objetos

    No Python, o comportamento dos operadores é definido por métodos especiais.
    Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
"""

# Sobrecarga é o comporatamento de um operador

print(2 + 2)
print('2' + '2')
print('################')


# O interpretado do python sabe o que fazer nessas situações.

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    # Esse método é usado para apresentar os valores
    # na classe Retangulo

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    # Esse método está criando um objeto na minha classe.

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


# O python nos fornece métodos especiais, justamente para fazer
# a sobrecarga de operadores.

r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2
print(r1 == r2)
print(r1 == r3)
print('################')
print(r3 > r1)
print(r3 < r1)
print('################')
print(r3)

# Nesse caso o interpretador nãoi sabe como fazer essa conta,
# visto ter criado uma classe que cria retângulos.
