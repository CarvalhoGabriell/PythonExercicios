list_perguntas = ["Telefonou para a vítima? \n", "Esteve no local do crime? \n", "Mora perto da vítima? \n",
                  "Devia para a vítima? \n", "Já trabalhou com a vítima? "]


def perguntas(perguntaas_list):
    nivel_culpa = 0
    for i in range(len(perguntaas_list)):
        resp_atual = ""
        while resp_atual != "SIM" or resp_atual != "NAO":
            print("Respostas válidas, apenas com <SIM> ou <NAO>.")
            print(perguntaas_list[i])
            resp_atual = input("").upper()
            if resp_atual == "SIM" or resp_atual == "NAO":
                break
    if resp_atual == "SIM":
        nivel_culpa += 1
    return nivel_culpa


resp_perguntas = perguntas(list_perguntas)

# verificar suspeito
print("<>" * 10, "RESULTADO DO INTERROGATORIO POLICIAL", "<>" * 10)
if resp_perguntas <= 1:
    print("VOCE É INOCENTE")
elif resp_perguntas == 2:
    print("VOCE É SUSPEITA NA INVESTIGACAO")
elif resp_perguntas == 3 or 4:
    print("VOCE FOI CUMPLICE NO CRIME")
elif resp_perguntas == 5:
    print("ENCONTRAMOS O ASSASINO!!!")
else:
    print("Alguma coisa deu erro.....")

# count = 0
# for resposta in respostas :
# if resposta == "SIM":
# count += 1
