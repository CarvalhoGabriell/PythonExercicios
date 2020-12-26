
# dicionario = {'nome': 'Gabriel', 'idade': 20, 'cidade': 'SP'}
# print("Nome: ",dicionario['nome'])
# print("Idade: ",dicionario['idade'])
# print("Cidade ",dicionario['cidade'])

dados = dict(nome = input("Digite seu nome: "),
             idade = input("Digite sua idade: "),
             cidade = input("Informe sua idade: "))

for chave, valor in dados.items():
    print(chave, "::", valor)