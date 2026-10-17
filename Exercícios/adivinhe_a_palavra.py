palavra_secreta = 'tales'
letras_acertadas = ''
cont_tentativas = 0

while True:
    palpite = input("Informe uma letra para a palavra secreta: ")
    dica = ''
    if len(palpite) != 1:
        palpite = input("Digite apenas uma letra: ")
        continue
    if palpite in palavra_secreta:
        letras_acertadas += palpite

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            dica += letra
        else:
            dica += '*'
    print("A palavra é:",dica)
    
    cont_tentativas += 1
    
    if dica == palavra_secreta:
        print(f"\nParabéns! Você acertou a palavra secreta em {cont_tentativas} tentativas!")
        break;
