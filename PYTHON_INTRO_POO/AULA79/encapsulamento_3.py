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
    
    _protected
    __privado
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Rafael')
bd.inserir_cliente(2, 'Otávio')
bd.__dados = 'Outra coisa'
# Isso irá fazer com que a classe pare de funcionar
bd.lista_clientes()

"""
    Por conveção do próprio Python, sempre que uma
    variável tiver um ou dois underlines, recomanda-se
    fortemente que não seja acessada.
"""
