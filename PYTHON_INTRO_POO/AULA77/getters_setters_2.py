"""
    @property - Getters e Setters
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A', '@')  # Trocar a letra A para @
        # self._nome = valor.title() # Deixa apenas a primeira letra como maiúscula
        # self._nome = valor.lower() # Deixa todas as letras em minúsculo.

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

# Os 'getters' e 'setters' são uma proteção, e podem ser
# usados para validação

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$ 15')
p2.desconto(10)
print(p2.nome, p2.preco)
