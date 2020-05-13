janela = [0]*24
print(janela, "JANELA")
corredor = [0]*24
print(corredor, "CORREDOR")
condicao = False
while not condicao:
    #----
    #Menu
    #----
    escolha = int(input("\n\n------------ Menu ------------"
                        "\n1 - Vender passagem"
                        "\n2 - Cancelar compra"
                        "\n3 - Mostrar mapa de ocupação"
                        "\n4 - Sair"
                        "\n\nEscolha uma opção: "))
    if escolha == 1:
        lugar = input("O que você deseja janela ou corredor? ")
    #Janela
        if lugar == "janela":
            poltrona = int(input("Escolha uma poltrona disponível (1-24)\n"))
            if poltrona >= 25 or poltrona <= 0:
                print("Poltrona não existe")
            elif janela[poltrona - 1] == 0:
                print("Poltrona disponível. \nVenda realizada com sucesso!")
                janela[poltrona - 1] = 1
                print(janela)
            elif janela[poltrona] == 1:
                print("Poltrona ocupada. Venda não realizada!")
            #poltrona ocupada
            else:
                print("Escolha outro assento, o mesmo já está ocupado")
    #Corredor
        elif lugar == "corredor":
            poltrona = int(input("Escolha uma poltrona disponível (1-24)\n"))
            if poltrona >= 25 or poltrona <= 0:
                print("Poltrona não existe")
            elif corredor[poltrona - 1] == 0:
                print("Poltrona disponível. \nVenda realizada com sucesso!")
                corredor[poltrona - 1] = 1
                print(corredor)
            elif corredor[poltrona] == 1:
                print("Poltrona ocupada. Venda não realizada!")
            #poltrona ocupada
            else:
                print("Escolha outro assento, o mesmo já está ocupado")
        #valor inválido
        else:
            print("Opção inválido")
    #Opção de cancelar
    elif escolha == 2:
        lugar = input("O que você deseja cancelar: \"janela\" ou \"corredor\"?")
        # Janela
        if lugar == "janela":
            poltrona = int(input("Escolha uma poltrona a ser cancelada (1-24)\n"))
            if poltrona >= 25 or poltrona <= 0:
                print("Poltrona não existe")
            elif janela[poltrona - 1] == 1:
                print("Cancelamento realizado com sucesso!")
                janela[poltrona - 1] = 0
                print(janela)
            elif janela[poltrona] == 0:
                print("Poltrona livre, compra não cancelada!")
        # Corredor
        elif lugar == "corredor":
            poltrona = int(input("Escolha uma poltrona a ser cancelada (1-24)\n"))
            if poltrona >= 25 or poltrona <= 0:
                print("Poltrona não existe")
            elif corredor[poltrona - 1] == 1:
                print("Cancelamento realizado com sucesso.")
                corredor[poltrona - 1] = 0
                print(corredor)
            elif corredor[poltrona] == 0:
                print("Poltrona livre, compra não cancelada!")

    #Mostrar mapa da ocupação
    elif escolha == 3:
        print("Janela\n\n")
        for poltrona in range(len(janela)):
            if janela[poltrona] == 1:
                print("{}- OCUPADO".format(poltrona + 1))
            elif janela[poltrona] == 0:
                print("{}- LIVRE".format(poltrona + 1))
        print("Corredor\n\n")
        for poltrona in range(len(corredor)):
            if corredor[poltrona] == 1:
                print("{}- OCUPADO".format(poltrona + 1))
            elif corredor[poltrona] == 0:
                print("{}- LIVRE".format(poltrona + 1))

    elif escolha == 4:
        print("Finalizando...")
        condicao = True
    else:
        print("\nOpção inválida")

