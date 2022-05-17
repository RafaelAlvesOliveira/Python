
import math

PI = math.pi


# O Python não usa constante, então para criar
# uma variável que não irá mudar de valor é
# necessário usar letras maiscúlas na variável.


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

# Para um determinado módulo não ser importa é
# necessário nomear o módulo como feito abaixo.
# Se '__name__' for igual a '__main__' ele
# executa o que estiver abaixo, caso contrário
# executará o que estiver fora desse bloco.


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

# print(__name__)

# Se executar esse módulo diretamente, o nome
# do módulo é 'main'.

