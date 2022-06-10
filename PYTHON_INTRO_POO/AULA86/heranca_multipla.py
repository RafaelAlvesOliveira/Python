"""
    Herança Múltipla — Python Orientado a Objetos
"""


class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')


class D(B, C):
    pass


# Essa é uma demonstração de herança múltipla,
# pois a classe D herda a classe B e C. Ao ter
# herança múltipla, o interpretador seleciona
# da esquerda para a direita.

d = D()
d.falar()

# Se o interpretador encontrar o método em B, ele
# simplesmente executa, caso não encontre ele vai
# procurar em C, e se não encontrar em C vai procurar
# em A, visto C ter herdado os métodos de A.

