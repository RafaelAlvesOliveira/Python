# Exercício que foi resolvido na aula 39

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'Primeiro valor {int_primeiro_valor} é maior que o segundo valor {int_segundo_valor}')
elif int_primeiro_valor < int_segundo_valor:
    print(f'Segundo valor {int_segundo_valor} é maior que o primeiro valor {int_primeiro_valor}')
else:
    print(f'Primeiro valor {int_primeiro_valor} é igual ao segundo valor {int_segundo_valor}')

print("Fim")