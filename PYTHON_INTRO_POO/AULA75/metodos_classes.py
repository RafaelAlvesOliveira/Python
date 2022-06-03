"""
    Métodos de classes - Python Orientado a Objetos
"""


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


p1 = Pessoa('Rafael', 31)
print(Pessoa.ano_atual)
p1.get_ano_nascimento()


# Apesar do atributo 'ano_atual' estar disponível para todas
# as instâncias dessa classe, ele é um atributo da classe em si.
# Já os atributos 'get_ano_nascimento', '__init__' são atributos
# relacionados com a instância 'self'.

