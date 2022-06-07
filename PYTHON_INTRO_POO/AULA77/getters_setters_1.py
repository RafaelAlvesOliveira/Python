"""
    @property - Getters e Setters
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # O método 'Getter' obtém um valor, e o 'Setter' configura um valor
    # 'Getter' é chamado antes da função, por convenção é necessário
    # colocar um _ ('underline') antes do nome da variável

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    # O 'Setter' vai configurar o preço, sendo assim, a variável preco
    # vai passar primeiro por ele, para depois ser enviada para função.
    # É incluído outro decorador com o nome da propriedade, é criado outro
    # método com o mesmo nome do anterior. É necessário checar se o 'valor'
    # é uma instância de 'str'.


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 'R$ 15')
p2.desconto(10)
print(p2.preco)
