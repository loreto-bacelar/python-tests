name = input("Informe seu nome: ")
height = float(input("Informe a altura: "))
mass = float(input("Informe a massa: "))

imc = mass / (height ** 2)

print(f'{name} tem {height:.2f} m de altura, {mass:.3f} kg e seu imc é {imc:.2f}')