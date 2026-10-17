import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

# cálculo para o primeiro dígito
i = 10
total = 0

for n in cpf:
    total += i * int(n);
    i -= 1

digito = (total * 10) % 11

primeiro_digito = 0 if digito > 9 else digito

#cálculo para o segundo dígito
i = 11
total = 0
dez_digitos = cpf + str(primeiro_digito)

for n in dez_digitos:
    total += i * int(n)
    i -= 1

digito = (total * 10) % 11
segundo_digito = 0 if digito > 9 else digito

nove_digitos_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:]

cpf_gerado = nove_digitos_formatado + "-" + str(primeiro_digito) + str(segundo_digito)

print(cpf_gerado)

print(40 * '-')