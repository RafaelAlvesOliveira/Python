"""
Contador Duplo
Minha resposta
"""

# variavel = [0,1,2,3,4,5,6,7,8,9]

contador = 10
acumulador = 0

while contador <= 10:

    if contador == 0 and acumulador == 10:
        break

    print(contador, acumulador)
    acumulador += 1
    contador -= 1

print('Pronto!')
