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
    def __init__(self):
        self.atributo = 'inicial'
    # Esse atributo só serve para salvar os valores
    # usados no Getter e Setter

    @property
    # A property indica para o python que essa função é um atributo,
    # e não como um método
    def nome(self):
        return self.atributo

    @nome.setter
    # O nome da função não interfere por ser igual ao da outra função.
    # O parâmetro nome, não é igual ao nome que é o método, são coisas
    # distintas.
    def nome(self, nome):
        self.atributo = nome


p1 = Pessoa()
p1.nome = 'João'
print(p1.atributo)
print(p1.nome)


