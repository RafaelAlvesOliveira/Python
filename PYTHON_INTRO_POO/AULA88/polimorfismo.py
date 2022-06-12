"""
    Polimorfismo é o princípio que permite que classes derivadas de uma mesma
    superclasse tenham métodos (de mesma assinatura), mas comportamentos
    diferentes.
    Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


# No polimorfismo temos uma classe herdando de uma
# superclasse que sobrescreve o método fala, ela tem
# a mesma assinatura, mas tem comportamento diferente.

b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro assunto')

# O python só suporta esse tipo de polimorfismo que é o
# de sobreposição. Também tem o polimorfismo de sobrecarga,
# mas o python não suporta.

# Sempre que houver uma classe abstrata com o método abstrato
# que force que o mesmo seja sobrescrito nas classes filhas,
# haverá um polimorfismo.
