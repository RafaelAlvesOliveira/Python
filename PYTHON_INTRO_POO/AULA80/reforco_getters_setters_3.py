"""
    Reforço de Setters e Getters - Python Orientado a objetos
"""


# 'Setter' = configurando um valor (=)
# Setter é uma palavra americana para 'set',
# ou seja, configurar um valor. Quando for informado
# que o atributo é igual a algo. O Setter é uma
# função que vai configurar o valor de uma determinada
# coisa. O Getter é uma função, e a única coisa que faz
# é retorna o valor do que foi configurado no Setter.
# Getter pode ser declarado sozinho, sem o Setter, mas o
# contrário não é possível.

# 'Getter' = obter um valor (.)
# Getter é uma palavra americana para 'get', ou seja,
# obter um valor. Getter lê, e Setter configura.

# Método é uma função na classe, que pode acessar o
# self().


class Pessoa:
    def __init__(self, nome):
        # O _nome é quem sustenta o valor
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Setter foi executado')
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Desconhecido'


p1 = Pessoa('Rafael')
print(p1.nome)
print(p1.sobrenome)

# Nunca chamar as funções 'Getters' ou 'Setters' dentro
# delas mesmas, pois isso irá gerar uma recursão. É um
# método que se utiliza para fazer a função se autoinvocar.

