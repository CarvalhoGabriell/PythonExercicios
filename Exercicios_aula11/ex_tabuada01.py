# MODELO 1

continuar = 1
while continuar == 1:
    tabuada = int(input("Digite um numero para gerar sua tabuada: "))
    print("Abaixo a tabuada de", tabuada)
    multiplicador = 0

    while multiplicador <= 10:
        print("{} X {} = {}".format(tabuada, multiplicador, tabuada*multiplicador))
        multiplicador += 1
    print("Deseja continuar?")
    print("Digite 1 para continuar ou 2 para sair.")
    continuar =int(input("Digite sua opção: "))
print("FIM da execução da tabuada, Obrigado!!")


# # MODELO 2
#
# tabuada = 0
# while tabuada <= 10:
#     print("5 X ", tabuada, " = ", 5 * tabuada)
#     tabuada = tabuada + 1
# print("############################### FIM DA TABUADA DO {} ############################\n".format(tabuada))