"""
Manipulando ‘strings’
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc ...
Essas funções poder ser usadas diretamente em cada tipo.

Pode conferir tudo isso em:
 https://docs.python.org/3/library/stdtypes.html (tipos built-in)
 https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos
#       [012345678]
texto = 'Python S2'
#       [987654321]
# negativos

nova_string = texto[0:6:2]
print(nova_string)
# Pode se fatiar e se fazer indicação de um valor de passos
# que podem ser usados, como no exemplo acima.
# Nesse caso o último valor indica o número de caracteres
# que devem ser pulados até chegar ao último caracter informado.

