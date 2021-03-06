"""
    Métodos estáticos - Python Orientado a Objetos
"""

from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

# Os métodos estáticos também recebe um decorador
# e ele não precisa nem da instância, nem da classe.
# Ele funciona como se fosse uma função fora da classe,
# mas por questão de organização precisa estar dentro
# da minha classe.


# p1 = Pessoa.por_ano_nascimento('Rafael', 1990)
p1 = Pessoa('Rafael', 31)
print(p1)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())

