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
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

        # poderia ser criada uma cadeia, e seria usado o nome da classe

        # super().__init__()

    # Isso seria uma sobreposição do construtor de Pessoa
    # Há duas soluções para essa situação, chamar o construtor
    # de Pessoa, ou reescrever o código. A melhor opçõa é sempre
    # chamar o método.
