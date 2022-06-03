"""
Classes - Python Orientado a objetos
"""


class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

        # variavel = 'Valor'
        # print(variavel)
        # Essa variável só é válida dentro do método '__init__'.
        # Só está disponível nesse escopo.

    # def outro_metodo(self):
    #     print(self.nome)
        # Se quiser usar qualquer uma das variáveis que tem a palavra
        # self dentro desse método, pois ela está disponível para todos
        # os métodos dentro da classe.

# Programação Orientada a Objetos é um paradigma de programação
# em que se retrata coisas do mundo real, como objetos dentro
# de um programa. Um método é uma função que pertence apenas a
# essa classe, essa função recebe argumentos e retorna os
# parâmetros.

# Quando se cria um objeto utiliza-se o molde, sendo a classe em
# si, sempre que ele é chamado o interpretador do python verifica
# o que o usuário quer fazer. A classe precisa saber qual a
# instância que chama, senão todas terão o mesmo valor.
# Quando se cria uma classe automaticamente está referir-se a que
# foi criada como instância dessa classe, que é 'p1', por exemplo. A palavra
# 'self' se refere a instância 'p1'

# Para todo método que for criado, deve-se passar primeiramente o
#  parâmetro 'self', por convenção é usado esse termo. Esse parâmetro já é
# enviado automaticamente,


# Apesar dos parâmetros 'self.nome' ter o mesmo nome da variável, eles são
# distintos, um recebe o valor do outro. O parâmetro 'self.nome' recebe o
# valor incluído na variável 'p1' no arquivo 'classes_poo_1.py'.

