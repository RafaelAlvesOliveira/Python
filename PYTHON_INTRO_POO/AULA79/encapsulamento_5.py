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
    
    _privado/protected (public _)
    Pode ser que em alguns lugares informem que esse objeto sejá protected,
    mas não é, pois é um atributo público que tem um _ (underline) no nome.
    Pois pode ser acessado e editado fora da classe.
    __privado (_NOMECLASSE__nomeatributo)
    Pode ser acessado com o nome da classe, e pode ser modificado; ele pode
    ser acessado de dessa maneiras (_NOMECLASSE__nomeatributo) e pode 
    modificá-lo dessa maneira fora da classe (_NOMECLASSE__nomeatributo).
    É praticamente impossível sobrescrever as informações dentro da classe.
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    # Pode se criar um property, para fazer a liberação
    # dos __dados. Quando se usa esse decorador, é para
    # se obter um dado. Um método da classe está se
    # parecendo com uma propriedade devido ao decorador
    # que está sendo usado. O python não irá permitir que
    # dados se configurado na classe, corrigindo é por
    # não ter criado um 'Setter' para essa variável.

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
bd.dados = 'Outro valor'
# Será levantada uma exceção informando que este atributo
# não pode ser configurado.
print(bd.dados)

