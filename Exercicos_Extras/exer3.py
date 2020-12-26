dados = []


nome = input("Digite seu nome:")
dados.append(nome)
sobrenome = input("Digite seu sobrenome: ")
dados.append(sobrenome)
idade = int(input("Agora sua idade: "))
dados.append(idade)

for item in dados:
    print(item)