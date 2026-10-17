lista = []

while True:
    print("Selecione uma das opções abaixo:")
    op = input("[i]nserir\t [a]pagar\t [l]istar: ")

    if op == 'i':
        print("\033[H\033[2J", end="") #limpar a tela sem criar processos extras
        item = input("Item para adicionar: ")
        lista.append(item)
    
    elif op == 'a':
        if len(lista) == 0:
            print('A lista está vazia. Não há nada para apagar!')
        
        else:
            indice_str = input("Escolha o índice para apagar: ")
            
            try:
                indice = int(indice_str)
                del lista[indice]
        
            except:
                print("Erro: índice inválido ou inexistente!")
    
    elif op == 'l':
        print("\033[H\033[2J", end="")
         
        if len(lista) == 0:
             print('A lista está vazia. Não há nada para listar!')
        
        for i, item in enumerate(lista):
            print(i, item)
    # else:
    #     continue
     

