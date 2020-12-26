dados = {}

resp = "SIM"
while resp == "SIM":
    dados[input("Digite o seu nome: ")] = [
        int(input("Informe sua idade: ")),
        input("Informe sua cidade <DIGITE SOMENTE A SIGLA>: ").upper()]
    resp = input("Digite <SIM> para continuar no Menu ").upper()

for chave, valor in dados.items():
    print("-------------- Dados do usuario ------------\n")
    print("Nome: ", chave)
    print("Idade: ", valor[0])
    print("Cidade: ", valor[1])
