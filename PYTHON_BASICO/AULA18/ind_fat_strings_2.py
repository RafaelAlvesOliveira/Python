"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc ...
Essas funções poder ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
 https://docs.python.org/3/library/stdtypes.html (tipos built-in)
 https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos
#       [012345678]
texto = 'Python S2'
#       [987654321]
# negativos

nova_string = texto[2:6]
print(nova_string)
# Quando se quer fatiar uma 'string', colocasse o colchete e dentro
# dele, colocasse de qual índice se quer iniciar e em, qual se quer
# terminar.
