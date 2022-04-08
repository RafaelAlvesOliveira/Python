# Iterar sobre uma 'string' é "passar" por cada um dos elementos da
# "string", todos os elementos primitivos têm índices.

#   Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1



