
nome = input("Infome seu nome: ")
print(" {}, Seja bem vindo ao estacionamento: SEJA SEMPRE BEM VINDO".format(nome))
horaEntrada = int(input("Por favor informe quantos minutos você demorou: "))

print("_______________________ MENU DE OPÇOES DE VEÍCULO _______________________\n"
      "[1] --- Para Carros \n"
      "[2] --- Para Motos \n"
      "\n"
      "------------------------- FIM !!! -------------------------")


veiculo = int(input("Qual é o tipo do seu veículo? "))
if (veiculo != 1 and veiculo != 2):
    print("Opção de veículo inválida, informe uma opção de acordo com o menu.")
else:
    print("Estamos verificando suas informações..............\n")

if(horaEntrada <= 15):

    print("Durante esse período de tempo o estacionamento é de graça tanto para moto tanto para carro")
else:
        if(veiculo == 1):
            if(horaEntrada >= 16 and horaEntrada <= 180):
                print("Durante esse período de tempo o estacionamento o valor total a pagar é de R$ 20,00 reais")
            elif(horaEntrada > 180):
                tempo = (horaEntrada - 180) * 0.15
                valor_extraC = tempo + 20
                print("Durante esse período de tempo o estacionamento o valor total a pagar é de R$ {} reais".format(valor_extraC))

        elif(veiculo == 2):
            if(horaEntrada >= 16 and horaEntrada <= 180):
                print("Durante esse período de tempo o estacionamento o valor total é de R$ 17,00 reais")
            elif(horaEntrada > 180):
                tempo = (horaEntrada - 180) * 0.10
                valor_extraM = tempo + 17
                print("Durante esse período de tempo o estacionamento o valor total é de R$ {} reais".format(valor_extraM))
        else:
            print("Fim da consulta de preços!")
