"""
For in em Python
Iterando strings com for
Função range (start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''

# 'continue' = pula para a próxima iteração
# 'break' = encerra o laço, ou seja, para de executá-lo

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# o argumento 'continue' serve para interroper o laço, nesse
# caso a letra 't' não aparecerá.
