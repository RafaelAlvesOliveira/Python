"""
Funções decoradoras e decoradores
"""


from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)


demora()

# Essa função é apenas para demonstrar a aplicação
# da função decoradora aplicada ao tempo de execução
# de uma função. Para essa situação só se calcula o
# tempo de 5 segundos, é o tempo que ela 'dorme'.

