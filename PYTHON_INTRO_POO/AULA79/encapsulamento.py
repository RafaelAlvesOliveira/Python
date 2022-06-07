"""
    Encapsulamento - Python Orientado a Objetos
"""

"""
    Conceito de encapsulamento em outras linguagens
    
    Na programação orientada a objetos clássica, haverão modificadores de 
    acesso, métodos e atributos públicos que utiliza a palavras 'public', 
    'protected' e 'private'.
    
    Publics: são métodos e atributos que podem ser acessados dentro e fora
    da classse.
    Protected: são atributos que podem ser acessados apenas dentro da classe
    ou das filhas da classe.
    Private: aquele atributo ou método só está disponível dentro da classe.
"""

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Rafael')
bd.inserir_cliente(2, 'Otávio')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()

# print(bd.dados)

