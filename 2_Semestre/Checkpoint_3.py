produtos_cadastrados = []
descriçao_produto = []
estoque = []
senha = ''
contagem = 4
condição = False

while not condição:
    while contagem > 1:
        # ---------
        # Menu
        # ---------
        escolha = int(input("\n\n•*´¨`*~ஜ◦•◦✿◦•◦ೋஜ~*´¨`*•.¸¸.•*\n"
                            "             MENU\n"
                            "1 - Cadastrar produto\n"
                            "2 - Alterar produto\n"
                            "3 - Excluir produto\n"
                            "4 - Listar estoque de peças\n"
                            "5 - Comprar produto\n"
                            "6 - Vender produto\n"
                            "7 - Sair\n"
                            "•*´¨`*~ஜ◦•◦✿◦•◦ೋஜ~*´¨`*•.¸¸.•*\n"
                            ": "))


        def solicita_codigo():
            codigo = int(input("\nCódigo do produto: "))
            return codigo


        def validar_cadastro_codigo():
            if codigoProduto in produtos_cadastrados:
                return True
            else:
                return False

        def produto_estoque_negativo():
            if len(produtos_cadastrados) < 1:
                print("Infelizmente, ainda não há nenhum produto armazenado! Por favor, cadastre um produto")



        # Cadastrar produto
        if escolha == 1:
            codigoProduto = solicita_codigo()

            # Validando cadastrado existente
            validaçao = validar_cadastro_codigo()

            if validaçao == False:
                descriçaoProduto = input("Descrição do produto: ")
                quantidadeProduto = int(
                    input("Quantidade do produto em estoque: "))

                # Validando código
                if codigoProduto < 0 or quantidadeProduto < 1:
                    print("\nValor inválido")
                else:
                    # atualizando dados do código
                    produtos_cadastrados.append(codigoProduto)
                    # atualizando dados da descrição
                    descriçao_produto.append(descriçaoProduto)
                    # atualizando dados do estoque
                    estoque.append(quantidadeProduto)
                    print("\nCadastro realizado com sucesso!")

            else:
                print("\nProduto já cadastrado!\n")


        elif escolha == 2 or escolha == 3:
            if len(produtos_cadastrados) < 1:
                print("Infelizmente, ainda não há nenhum produto armazenado! Por favor, cadastre um produto")
            else:
                lista_guarda_senha = [senha]

                if lista_guarda_senha == ['']:


                    if escolha == 2:
                        # Acesso permitido
                        senha = input("\nSenha: ")
                        if senha == "yN1825*a":
                            codigoProduto = solicita_codigo()

                            # Validando código cadastrado
                            validaçao = validar_cadastro_codigo()

                            if validaçao == True:
                                for i in range(len(produtos_cadastrados)):
                                    if codigoProduto == produtos_cadastrados[i]:
                                        print("\nDESCRIÇÃO: ", descriçao_produto[i],
                                              "\nQUANTIDADE EM ESTOQUE: ", estoque[i])

                                        alterar = input("O que vc deseja alterar? (Digite a letra correspondente)\n"
                                                        "a) Descrição\n"
                                                        "b) Estoque\n")

                                        # Alterando descrição
                                        if alterar == "a":
                                            alteracao = input("\nAlteração\n"
                                                              ": ")
                                            descriçao_produto[i] = alteracao

                                        # Alterando estoque
                                        elif alterar == "b":
                                            alteracao = int(input("\nAlteração\n"
                                                              ": "))
                                            estoque[i] = alteracao
                                        else:
                                            print("O valor inserido é inválido!")
                            else:
                                print("\nProduto não cadastrado!\n")
                        else:
                            print("\nSenha incorreta\n")
                            contagem -= 1
                            senha = ''

                    elif escolha == 3:
                        senha = input("\nSenha: ")
                        # Acesso permitido
                        if senha == "yN1825*a":
                            codigoProduto = solicita_codigo()
                            validaçao = validar_cadastro_codigo()

                            if validaçao == True:
                                for i in range(len(produtos_cadastrados)):
                                    if codigoProduto == produtos_cadastrados[i]:
                                        print("\nDESCRIÇÃO: ", descriçao_produto[i])
                                        print("\nESTOQUE: ", estoque[i])

                                        excluir = input("\nDeseja excluir o produto?\n")
                                        if excluir == "sim":
                                            del produtos_cadastrados[i]
                                            del descriçao_produto[i]
                                            del estoque[i]
                                            print("Produto excluído com sucesso!")
                                        elif excluir == "não":
                                            print("Produto não excluído")
                            else:
                                print("\nProduto não cadastrado!\n")
                        else:
                            print("\nSenha incorreta")
                            contagem -= 1
                            senha = ''

                else:

                    if lista_guarda_senha == ['yN1825*a']:
                        if escolha == 2:
                            codigoProduto = solicita_codigo()

                            # Validando código cadastrado
                            validaçao = validar_cadastro_codigo()

                            if validaçao == True:
                                for i in range(len(produtos_cadastrados)):
                                    if codigoProduto == produtos_cadastrados[i]:
                                        print("\nDESCRIÇÃO: ", descriçao_produto[i],
                                              "\nQUANTIDADE EM ESTOQUE: ", estoque[i])

                                        alterar = input("O que vc deseja alterar? (Digite a letra correspondente)\n"
                                                        "a) Descrição\n"
                                                        "b) Estoque\n")

                                        # Alterando descrição
                                        if alterar == "a":
                                            alteracao = input("\nAlteração\n"
                                                              ": ")
                                            descriçao_produto[i] = alteracao

                                        # Alterando estoque
                                        elif alterar == "b":
                                            alteracao = input("\nAlteração\n"
                                                              ": ")
                                            estoque[i] = alteracao
                                        else:
                                            print("O valor inserido é inválido!")
                            else:
                                print("\nProduto não cadastrado!\n")

                        elif escolha == 3:
                            codigoProduto = solicita_codigo()
                            validaçao = validar_cadastro_codigo()

                            if validaçao == True:

                                for i in range(len(produtos_cadastrados)):
                                    if codigoProduto == produtos_cadastrados[i]:
                                        print("\nDESCRIÇÃO: ", descriçao_produto[i])
                                        print("\nESTOQUE: ", estoque[i])

                                        excluir = input("\nDeseja excluir o produto?\n")
                                        if excluir == "sim":
                                            for i in range(len(produtos_cadastrados)):
                                                if codigoProduto == produtos_cadastrados[i]:
                                                    del produtos_cadastrados[i]
                                                    del descriçao_produto[i]
                                                    del estoque[i]
                                            print("Produto excluído com sucesso!")
                                        elif excluir == "não":
                                            print("Produto não excluído")

                            else:
                                print("\nProduto não cadastrado!\n")

                    else:
                        print("\nSenha incorreta\n")
                        contagem -= 1
                        senha = ''

        # Listar estoque de peças
        elif escolha == 4:

            ordem = sorted(produtos_cadastrados)

            for i in range(len(ordem)):

                for j in range(len(descriçao_produto)):

                    for z in range(len(estoque)):
                            print("CÓDIGO:", ordem[i])
                            print("ESTOQUE: ", estoque[i])
                            print("DESCRIÇÃO: ", descriçao_produto[i])




                    # print("DESCRIÇÃO:", descriçao_produto[j])
                      #  print("QUANTIDADE EM ESTOQUE:", estoque[i], "\n")

            print("\nTotal de produtos cadastrados: ", len(produtos_cadastrados))

            soma_itens_estoque = 0
            for i in range(len(estoque)):
                estoque[i] = int(estoque[i])
                soma_itens_estoque = soma_itens_estoque + estoque[i]
            print("Quantidade de itens em estoque: ", soma_itens_estoque)

            mínimo = 100
            produtos_estoque_abaixo_permitido = []
            for i in range(len(estoque)):
                if estoque[i] < mínimo:
                    produtos_estoque_abaixo_permitido.append(estoque[i])
            print("Produtos com estoque abaixo do mínimo permitido (100 unidades): ",
                  len(produtos_estoque_abaixo_permitido), "\n")


        # Comprar produto
        elif escolha == 5:
            if len(produtos_cadastrados) < 1:
                print("Infelizmente, ainda não há nenhum produto armazenado! Por favor, cadastre um produto")
            else:
                codigoProduto = solicita_codigo()
                validaçao = validar_cadastro_codigo()

                if validaçao == True:
                    for i in range(len(produtos_cadastrados)):
                        if codigoProduto == produtos_cadastrados[i]:
                            print("\nDescrição: ", descriçao_produto[i])
                            print("Quantidade em estoque: ", estoque[i])

                            qtd_produtos_comprar = int(input("\nQuantidade de produtos que irá comprar: "))
                            if qtd_produtos_comprar <= 0:
                                print("\nValor inválido!")
                            else:
                                soma = 0
                                estoque[i] = qtd_produtos_comprar + estoque[i]
                else:
                    print("\nProduto não cadastrado!")


        # Vender produto
        elif escolha == 6:
            if len(produtos_cadastrados) < 1:
                print("Infelizmente, ainda não há nenhum produto armazenado! Por favor, cadastre um produto")
            else:
                codigoProduto = solicita_codigo()
                validaçao = validar_cadastro_codigo()

                if validaçao == True:
                    for i in range(len(produtos_cadastrados)):
                        if codigoProduto == produtos_cadastrados[i]:
                            print("\nDescrição: ", descriçao_produto[i])
                            print("Quantidade em estoque: ", estoque[i])

                            qtd_produtos_vender = int(input("\nQuantidade de produtos que irá vender:"))
                            subtracao = 0
                            if estoque[i] < qtd_produtos_vender:
                                print("\nValor digitado é maior que a quantidade disponível")

                            elif qtd_produtos_vender < 0:
                                print("\nValor inválido!")

                            else:
                                estoque[i] = estoque[i] - qtd_produtos_vender
                else:
                    print("\nProduto não cadastrado!")

        # Sair
        elif escolha == 7:
            print("\nFinalizando acesso...\n")
            condição = True
            exit()

    else:
        print("\nVocê errou a senha 3 vezes")
        print("Seu acesso foi bloqueado! Por favor, procure o administrador\n")
        condição = True