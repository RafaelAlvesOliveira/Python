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
p1.get_ano_nascimento()


# Cada instância vai ter o seu próprio ano de nascimento
# baseado nessas variáveis. O método de classe é um atributo
# similar ao atributo de classe 'ano_atual', ele é referente
# a classe e não a instância.

