from math import sqrt

nome = input("Qual é o seu nome? ")
print("Olá {},seja bem vindo(a) ao nosso MENU, a seguir mostraremos nooso MENU de opções".format(nome))

print("---------------- MENU DE OPÇÕES -----------------")
print("[1] -- PARA SOMAR")
print("[2] -- PARA FAZER UMA RAIZ QUADRADA")

opcao = int(input("Qual das opções você deseja fazer: "))

if (opcao == 1):
    num1 = int(input("Informe um numero: "))
    num2 = int(input("Informe um numero: "))
    result = num1 + num2
    print("O resultado da soma é = {}".format(result))
elif (opcao == 2):
    numero = int(input("Informe um numero: "))
    raiz = (numero**(1/2))
    print("O resultado da raiz quadrada é = {}".format(raiz))
else:
    if(opcao != 1 or opcao != 2):
        print("--------------------- Opção inválida, operação finalizada!------------------------")



