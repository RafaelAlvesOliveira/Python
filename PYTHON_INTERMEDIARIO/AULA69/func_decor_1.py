"""
Funções decoradoras e decoradores
"""


def master():
    def slave():
        print('Oi')
    return slave
    # slave()


# master()
variavel = master()
variavel()
print(type(variavel))

# Essa situação mostra uma função que é invocad dentro
# de outra função, mas para conseguir invocar a função
# 'slave' é necessário invocar ela no escopo da
# função 'master'. Tem a opção de usar o 'return',
# que retorna a função 'slave' sem essa ser executada.

