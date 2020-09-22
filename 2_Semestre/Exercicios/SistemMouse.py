def mouses():
    mouse_esferas =[]
    mouse_limpeza =[]
    mouse_cabo = []
    mouse_quebrado = []
    continuar = True
    esfera = 0
    limpeza = 0
    cabo_conector = 0
    quebrado_inutiliz = 0

    print("Para encerrar digite 0 na identificação!")
    while continuar == True:
        identificacao = int(input("Digite o número de identificação do mouse: "));
        if (identificacao == 0):  # FINALIZA
            continuar = False
        else:
            print("", "-" * 30, "\n           Mouse", "\n", "-" * 30,
                  "\n1 -> necessita da esfera"
                  "\n2 -> necessita de limpeza"
                  "\n3 -> necessita troca do cabo ou conector"
                  "\n4 -> quebrado ou inutilizado")
            entrada = int(input("Informe o que o mouse apresenta: "))
            while entrada < 0 or entrada > 4 or entrada == None:
                entrada = int(input("Resposta Inválida. Digite novamente!: "))
            if entrada == 1:
                mouse_esferas.append(identificacao)
                esfera += 1
            elif entrada == 2:
                mouse_limpeza.append(identificacao)
                limpeza += 1
            elif entrada == 3:
                mouse_cabo.append(identificacao)
                cabo_conector += 1
            elif entrada == 4:
                mouse_quebrado.append(identificacao)
                quebrado_inutiliz += 1

    total = esfera + limpeza + cabo_conector + quebrado_inutiliz
    if (total != 0):
        print("\nQuantidade de mouses: ", total, "\n\nSituação\t\t\t\t\t\t\t\t\t\t\tQuantidade\t\t\t\tPercentual")
        print("\n1 - Necessita da esfera\t\t\t\t\t\t\t\t", esfera, "\t\t\t\t\t\t", esfera * 100 / total, "%")
        print("2 - Necessita da limpeza\t\t\t\t\t\t\t", limpeza, "\t\t\t\t\t\t", limpeza * 100 / total, "%")
        print("3 - Necessita de troca do cabo ou conector\t\t\t", cabo_conector, "\t\t\t\t\t\t",
              cabo_conector * 100 / total, "%")
        print("4 - Quebrado ou inutilizado\t\t\t\t\t\t\t", quebrado_inutiliz, "\t\t\t\t\t\t",
              quebrado_inutiliz * 100 / total, "%")

    print("\nPrograma encerrado!")


mouses()