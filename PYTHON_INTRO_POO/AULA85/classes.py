class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        # O interpretador entende que o super é o método dessa
        # classe, visto ele seguir a hierarquia da herança.
        print('Estou em cliente.')


class ClienteVIP(Cliente):
    def falar(self):
        Pessoa.falar(self)
        # Nesse caso está sendo chamada a classe específica.

        Cliente.falar(self)
        # Esse é o falar da classe cliente.

        # super().falar()
        # A palavra super referir-se a classe Pessoa, para que o
        # método da superclasse seja executado primeiro, e depois
        # vai chamar o da classe ClienteVIP.
        print('Outra coisa qualquer.')

    # Está é uma sobreposição ou sobrescrever um método

# ClienteVIP herda da classe Pessoa e de Cliente
# É possível sobrepor qualquer membro da classe
# atributos de classe, atributos de instância e métodos.
