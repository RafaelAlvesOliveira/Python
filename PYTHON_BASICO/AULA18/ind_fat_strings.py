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

# Qualquer índice pode ser acessado, basta colocar o número do
# índice que queremos chamar entre colchetes dentro do print
# podem ser usados índices negativos para acesso, mas na contagem
# deve se mencionar o -1, no caso de ser negativo

print(texto[2])
print(texto[8])

