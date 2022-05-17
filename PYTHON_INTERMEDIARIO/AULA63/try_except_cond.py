"""
Try e except como condicional
"""


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is not None:
        print(numero * 5)
    else:
        print('Isso não é um número.')

# Função para converter número de 'string' para 'int' ou
# 'float'. A validação no bloco 'while' é invertida, pois,
# testa se uma determinada condição não for verdadeira.
