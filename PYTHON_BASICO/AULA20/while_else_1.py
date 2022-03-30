"""
While/Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
# o 'break' só será acionado quando o valor for maior que 5

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print('Isso será executado.')
