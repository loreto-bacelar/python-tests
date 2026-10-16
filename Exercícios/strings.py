nome = input("Informe seu nome: ")
idade = (input("Informe a idade: "))
print(30 * '-')

if not(nome and idade):
    print("Você deve preencher todos os campos!")
else:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if (' ' in nome):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

print(30 * '-')