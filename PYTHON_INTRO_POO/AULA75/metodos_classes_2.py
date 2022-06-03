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

# Esse é um método 'Factory' que gera outro objeto. Que crie
# uma pessoa com base no seu ano de nascimento, e é um método
# que não está relacionado com a instância da clase, mas com
# a classe em si. Quando se cria um método de classe, o mesmo
# é referente a classe em si, e nesse caso se pode criar variáveis
# que existiram apenas dentro desse método.

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# A função foi 'decorada' e, foi usado um método de classe
# 'cls', e nesse caso não precisa usar o 'self'. Esse método
# retorna a própria classe com nome e idade, contudo baseado
# nos parâmetros informados.


# p1 = Pessoa.por_ano_nascimento('Rafael', 1990)
p1 = Pessoa('Rafael', 31)
print(p1)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()




