
nome = input("Informe seu nome: ")
destino = input("Seja bem vindo {}, escolha uma das opçoões para onde deseja voar: "   "(norte, nordeste ou centro oeste)".format(nome)).upper()

if (destino == "NORTE"):
        opcao = input("Digite sua opção de passagem: "   "(ida, ida e volta)")
        if (opcao == "ida"):
            print("O total a pagar referente a passagem é de R$ 280,00 reais")
            print("Obrigado por comprar conosco, volte sempre!!")
        if (opcao == "ida e volta"):
            print("O total a pagar referente a passagem é de R$ 400,00 reais")
            print("Obrigado por comprar conosco, volte sempre!!")
elif (destino == "NORDESTE"):
        opcao = input("Digite sua opção de passagem: "   "(ida ou ida e volta)")
        if (opcao == "ida"):
            print("O total a pagar referente a passagem é de R$ 380,00 reais")
            print("Obrigado por comprar conosco, volte sempre!!")
        if (opcao == "ida e volta"):
            print("O total a pagar referente a passagem é de R$ 628,00 reais")
            print("Obrigado por comprar conosco, volte sempre!!")
elif (destino == "CENTRO OESTE"):
        opcao = input("Digite sua opção de passagem: "   "(ida ou ida e volta)")
        if (opcao == "ida"):
            print("O total a pagar referente a passagem é de R$ 620,00 reais")
            print("Obrigado por comprar conosco, volte sempre!!")
        if (opcao == "ida e volta"):
            print("O total a pagar referente a passagem é de R$ 1100,00 reais")
            print("Obrigado por comprar conosco, volte sempre!!")
else:
    if (destino != "NORTE" or destino != "NORDESTE" or destino != "CENTRO OESTE"):
        print(" Olá {} ,Opção de destino inválido. Infelizmente nós não voamos para esse trecho ainda, escolha um válido".format(nome))
        print("####################FIm da compra!!########################")
