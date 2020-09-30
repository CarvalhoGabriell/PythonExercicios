
inventario_prod = dict()
# descr_produt = []
# nomes_loja = []
lojas = dict()
lojas_preco = []
cont = 0

cond = False
while not cond:
    escolha = int(input("\n━━━━━━━━━━━━━━━━━━◇◆◇━━━━━━━━━━━━━━━━━━\n"
                    "              Menu de opções\n"
                    "\n"
                    "1 - Cadastrar Lojas\n"
                    "2 - Cadastrar Produtos\n"
                    "3 - Listar Produtos por Loja\n"
                    "4 - Sair\n"
                    "Escolha uma opção: "))


    if escolha == 1:
        while True:
            if len(lojas) > 0:
                print("Já foram cadastrados os Dados, opção invalida")
            else:
                for num in range(6):
                    lojas['cod'] = int(input("Informe um codigo: "))
                    if lojas['cod'] <= 0:
                        break
                    print("Codigo invalido, Digite um codigo valido")
                    if lojas['cod'] in lojas:
                        break
                    print("Desculpe essa loja ja existe, informe outra")

                    lojas['nome'] = input("Coloque o nome: ")

                    print("Cadastardo com sucesso")

    elif escolha == 2:
        if len(inventario_prod) > 0:
            print("Já foram cadastrados os Dados, opção invalida")
        elif len(lojas) < 1:
            print("Voce não pode cadastrar prdutos antes de cadastrar um loja..")
        else:
           for num in range(5):
                inventario_prod['codProd'] = int(input("Digite um codigo valido: "))
                inventario_prod['desc'] = input("Digite uma descrição: ")
                inventario_prod['preco'] = float(input("Informe o valor do produto: "))
                lojas_preco.append(inventario_prod['preco'])
                if inventario_prod['codProd'] <= 0:
                    print("Codigo invalido")
                if inventario_prod['codProd'] in inventario_prod:
                    print("Desculpe esse produto ja existe")
    elif escolha == 3:
        print("Listar produtos nas lojas")
        # for i in range(len(lojas)):
        #     for linha in range(len(precos_das_lojas)):
        #         for coluna in range(len(precos_das_lojas)):
        #             precos_das_lojas[linha][coluna] = lojas[i]
    elif escolha == 4:
        print("Saindo  do Menu")
        cond = True
        exit()
    else:
        print("Numero invalido, por favor digite uma opção do menu")
        cond = True

