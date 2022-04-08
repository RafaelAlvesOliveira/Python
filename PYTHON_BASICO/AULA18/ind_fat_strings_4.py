"""
Manipulando 'strings'
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

nova_string = texto[7:]
print(nova_string)

# Se não for colocado o valor final, ele fatiará
# do índice indicado até o último caracter.

nova_string1 = texto[-9:-3]
print(nova_string1)
# Pode se usar índices negativos.
