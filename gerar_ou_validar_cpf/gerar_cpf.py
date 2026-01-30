import random

multiplicador = 0
soma = 0
    
primeiros_9_digitos_cpf = ''
for i in range(9):
    primeiros_9_digitos_cpf += str(random.randint(0, 9))

for digito_1 in primeiros_9_digitos_cpf:
    multiplicacao = int(digito_1) * multiplicador
    soma += multiplicacao
    multiplicador -= 1

digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

primeiros_10_digitos_cpf = primeiros_9_digitos_cpf + str(digito_1)

multiplicador = 11
soma = 0

for digito_2 in primeiros_10_digitos_cpf:
    multiplicacao = int(digito_2) * multiplicador
    soma += multiplicacao
    multiplicador -= 1

digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{primeiros_9_digitos_cpf}{digito_1}{digito_2}'

print(f'CPF: {cpf_gerado}')