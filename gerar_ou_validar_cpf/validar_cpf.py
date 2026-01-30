import re

while True:
    multiplicador = 10
    soma = 0

    cpf = input('Digite o CPF: ')

    cpf = re.sub(
        r'[^0-9]',
        '',
        cpf
    )

    if len(cpf) != 11:
        print('Digite um CPF válido\n')
        continue

    if cpf == cpf[0] * len(cpf):
        print('Todos os dígitos do CPF não podem ser iguais!\n')
        continue

    else:
        print('Digite um CPF válido\n')

    break
    
primeiros_9_digitos_cpf = cpf[:9]

for digito_1 in primeiros_9_digitos_cpf:
    multiplicacao = int(digito_1) * multiplicador
    soma += multiplicacao
    multiplicador -= 1

digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print (f'\nDigito 1: {digito_1}')


primeiros_10_digitos_cpf = primeiros_9_digitos_cpf + str(digito_1)

multiplicador = 11
soma = 0

for digito_2 in primeiros_10_digitos_cpf:
    multiplicacao = int(digito_2) * multiplicador
    soma += multiplicacao
    multiplicador -= 1

digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print (f'\nDigito 2: {digito_2}')

cpf_calculo = f'{primeiros_9_digitos_cpf}{digito_1}{digito_2}'

if cpf == cpf_calculo:
    print(f'\nO CPF {cpf} é valido!')
else:
    print('\nO CPF não é válido!')