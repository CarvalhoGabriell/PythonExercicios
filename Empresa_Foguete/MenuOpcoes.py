# Criando as listas janela e corredor
janela = [0] * 2
corredor = [0] * 2
print(len(janela))
print("Janela\n", janela, "\n\nCorredor\n", corredor)
condicao = False
onibus_lotado = False
while not condicao:
    # ------
    # Menu
    # ------
    escolha = int(input("\n━━━━━━━━━━━━━━━━━━◇◆◇━━━━━━━━━━━━━━━━━━\n"
                        "              Menu de opções\n"
                        "\n"
                        "1 - Vender passagem\n"
                        "2 - Cancelar compra\n"
                        "3 - Mostrar mapa de ocupação\n"
                        "4 - Sair\n"
                        "Escolha uma opção: "))
    # Vender passagem
    if escolha == 1:
        # while - iniciando
        onibus_lotado = False
        while not onibus_lotado:
            if all(janela[poltrona] == 1 and corredor[poltrona] == 1 for poltrona in range(len(janela)) and range(len(corredor))):
                print("\nÔnibus lotado")
                onibus_lotado = True
            # Escolha do cliente entre janela ou corredor
            else:
                pergunta = input("\nOlá, você deseja janela ou corredor?\n")
            # Janela
                if pergunta == "janela":
                    if all(janela[poltrona] == 1 for poltrona in range(len(janela))):
                        onibus_lotado = True
                        print("\nPoltronas da Janela\n", janela)
                        print("As poltronas da janela já estão ocuapda por favor escolha corredor ou sair.")
                    else:
                        poltrona = int(
                            input("\nQual o número da poltrona que você deseja? (1-24)\n"))
                        # Verificando poltrona - janela
                        if poltrona >= 3 or poltrona <= 0:
                            print("Poltrona não existe, insira um valor válido")
                        elif janela[poltrona - 1] == 0:
                            print("\nVenda realizada com sucesso!\n")
                            janela[poltrona - 1] = 1
                            print("Janela:\n", janela, "\nCorredor:\n", corredor)
                        elif janela[poltrona - 1] == 1:
                            print("\nPoltrona ocupada. Venda não realizada!\n")
                # Corredor
                if pergunta == "corredor":
                    if all(corredor[poltrona] == 1 for poltrona in range(len(janela))):
                        onibus_lotado = True
                        print("\nPoltronas do Corredor\n", corredor)
                        print("As poltronas do corredor já estão ocuapda por favor escolha corredor ou sair.")
                    else:
                        poltrona = int(
                            input("\nQual o número da poltrona que você deseja? (1-24)\n"))
                        # Verificando poltrona - janela
                        if poltrona >= 3 or poltrona <= 0:
                            print("Poltrona não existe, insira um valor válido")
                        elif corredor[poltrona - 1] == 0:
                            print("\nVenda realizada com sucesso!\n")
                            corredor[poltrona - 1] = 1
                            print("Janela:\n", janela, "\nCorredor:\n", corredor)
                        elif corredor[poltrona - 1] == 1:
                            print("\nPoltrona ocupada. Venda não realizada!\n")
                # while - concluindo
                if (pergunta == "janela" or pergunta == "corredor"):
                    pergunta = input("\nDeseja efetuar outra compra?\n")
                    if pergunta == "sim":
                        onibus_lotado = False
                    else:
                        onibus_lotado = True
    # Cancelar passagem
    elif escolha == 2:
        print("Cancelamento da passagem\n"
              "Janela: ", janela, "\nCorredor: ", corredor)
        poltrona = int(input("\nInforme o número da sua poltrona: "))
        # Verificar existência da poltrona
        if poltrona >= 25 or poltrona <= 0:
            print("\nPoltrona não existe, insira um valor válido")
        else:
            lugar = input("\nQual local da sua poltrona, janela ou corredor?\n")
            if lugar == "janela":
                # Janela
                if janela[poltrona - 1] == 1:
                    print("\nCompra cancelada com sucesso!\n")
                    janela[poltrona - 1] = 0  # atualizando valor da poltrona
                    print("Janela\n", janela,
                          "\nCorredor\n", corredor)
                elif janela[poltrona - 1] == 0:
                    print("\nPoltrona livre. Compra não cancelada!\n")
            elif lugar == "corredor":
                # Corredor
                if corredor[poltrona - 1] == 1:
                    print("\nCompra cancelada com sucesso!\n")
                    corredor[poltrona - 1] = 0  # atualizando valor da poltrona
                    print("Janela\n", janela,
                          "\nCorredor\n", corredor)
                elif corredor[poltrona - 1] == 0:
                    print("\nPoltrona livre. Compra não cancelada!\n")
    # Mapa de ocupação
    elif escolha == 3:
        print("\nMapa da ocupação\n"
              "\nJanela")
        # Mapa - janela
        for poltrona in range(len(janela)):
            if janela[poltrona] == 1:
                print(poltrona + 1, " - Ocupada")
            elif janela[poltrona] == 0:
                print(poltrona + 1, " - Livre")
        print("\nCorredor\n")
        # Mapa - corredor
        for poltrona in range(len(corredor)):
            if corredor[poltrona] == 1:
                print("{} - Ocupada".format(poltrona + 1))
            elif corredor[poltrona] == 0:
                print("{} - Livre".format(poltrona + 1))
                # Sair
    elif escolha == 4:
        condicao = True
        print("\nFinalizando acesso...\n")
    # Valores inválidos
    elif escolha > 4 or escolha < 1:
        print("O valor inserido é inválido.\nPor favor, insira um valor que o sistema aceite")