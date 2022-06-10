class Pessoa:
    # Super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        # O método falar é herdado por ambas as classes filhas.
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):
    # Subclasse
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')
    # O método comprar é exclusivo da classe Cliente


# A classe Cliente é especializada, os métodos genéricos
# estão na classe Pessoa.


class Aluno(Pessoa):
    # Subclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')
    # O método estudar é exclusivo da classe Aluno

# As duas classes herdam as instâncias da classe Pessoa.
# Não é interessante se repetir no código
