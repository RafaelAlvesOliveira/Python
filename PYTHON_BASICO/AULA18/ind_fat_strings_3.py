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

nova_string = texto[:6]
print(nova_string)
# Se quiser começar do primeiro caractere, não precisa colocar
# número nenhum, antes dos dois pontos (:), mas precisa colocar
# o valor que termina. Implicitamente o interpretador do python
# entende ser zero.

