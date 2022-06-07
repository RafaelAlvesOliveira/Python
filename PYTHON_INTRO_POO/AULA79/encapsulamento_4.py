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
# Foi criado esse atributo dados, e ele foi acessado.
print(bd.__dados)
print(bd._BaseDeDados__dados)
# bd.lista_clientes()

"""
    Quando se usa dois underlines, está sendo avisado
    que esse atributo não pode ser acessado de forma 
    alguma. Mesmo nessa situação acima em que se reatribui 
    um valor ao banco e se usa print para acessá-lo, não há 
    problema. O interpretador do python consegue diferenciar
    as duas classes. Para se acessar o atributo real, é 
    necessário colocar o nome da variável e depois ponto 
    _BaseDeDados__dados.
"""
