# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece  a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path.
# try:
#     import sys
#     sys.path.append('/home')
# except ModuleNotFoundError:
#     ...
import AULA154_M
from AULA154_M import variavel_modulo, soma

print(AULA154_M.variavel_modulo)
print(variavel_modulo)
print(soma(2,3))
print(AULA154_M.soma(2,3))
# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')