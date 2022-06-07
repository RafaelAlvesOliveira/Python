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
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd._dados = 'Um outro valor qualquer'
print(bd._dados)


"""
    Segundo a filosofia do Python foi criado, uma convenção de 
    que se um atributo tiver um _ (underline) antes do início do
    nome. Recomenda-se que não acesse esse atributo. Um sinal de 
    _ (underline) indica que o atributo é privado, mas de uma
    maneira mais sútil. Mesmo que o atributo esteja oculto, ainda
    assim pode ser acessado. Em alguns casos isso é chamado de 
    _protected.
"""
