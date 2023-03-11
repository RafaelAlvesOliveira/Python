import importlib

import AULA156_M

print(AULA156_M.variavel)

for i in range(10):
    # print(i)
    importlib.reload(AULA156_M)
    print(i)
    # import  AULA156_M

print('Fim')