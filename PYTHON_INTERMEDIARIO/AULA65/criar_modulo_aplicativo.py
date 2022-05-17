
import criar_modulos_calc
# print(__name__)

# A variável '__name__' vai retornar o nome do
# módulo, apenas se o módulo estiver sendo
# importado por outro módulo.

print(criar_modulos_calc.PI)

lista = [2, 4]
print(criar_modulos_calc.multiplica(lista))

# Não se usa a extensão do arquivo ao fazer a
# importação do mesmo em outro.


# print(criar_modulos_calc.PI)

# Todos os prints que foram feitos no outro
# arquivo, foram executados nesse. Só por
# ter importado o arquivo criar_modoulos_calc.py
# o interpretador já executa tudo o que consta
# no arquivo.

