"""
    Classes Abstratas - Python orientado a objetos
"""

# Uma classe abstrata pode ter métodos concretos e métodos abstratos

# Métodos concretos, são métodos normais em que se escreve o código e ele
# funciona perfeitamente na cadeia herança. Ele será herdado por outras
# classes e funcionará perfeitamente.

# Métodos abstratos, um método que não tem corpo, é simplesmente criado e
# não tem código nele. E informa que ele é abstrato para que as outras
# classes filhas herdem esse método, e sejam obrigadas a criar esse método
# dentro de si.

# Para criar uma clase abstrata em python será necessário importar duas no
# mínimo

from abc import ABC, abstractmethod


# Abstratic base class
# Decorador abstractmethod

# Com esses dois itens importados já é possível criar classes abstratas

# Para que essa classe não possa ser instanciada, e só servir como base
# para outras classes. Para fazer isso é necessário ter um método abstrato,
# esse método abstrato é um método que eu quero forçar que outras classes
# escrevam ele. As classes filhas da classe A precisam ter determinado
# método.
class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando... B...')


# Aparece um aviso no interpretador do Python dizendo que não poderá
# instanciar a classe B, enquanto ela não tiver o mesmo método que a
# classe A. Asssim que o método falar() da classe A for sobrescrito,
# poderá ser usado normalmente.

# Quando se têm um método abstrato na classe, não é possível instanciar
# ela novamente.

a = A()
# a = B()
a.falar()

# Na aula sobre herança, foi criada uma classe chamada pessoa que era
# algo abstrato. Foi feita a especialização em outras classes como cliente
# ou como um aluno, contudo a classe pessoa não deve ser instanciada.
# A classe pessoa deve ser algo abstrato, e force as outras classes que
# herdem dela a fazer algo específico.
