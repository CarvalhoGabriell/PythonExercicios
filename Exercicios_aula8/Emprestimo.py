nome = input("Digite seu nome: ")
salario = float(input("Olá {} Digite aqui seu salário bruto: ".format(nome)))
valorPrest = float(input("Digite o valor da prestação do empréstimo: "))
limite = float(salario * 0.3)

if (salario <= 0):
        print("Por favor não será aceito empréstimos com salário igual zero.")
if (valorPrest <= 0):
        print("Opção de prestação inválido, digite outro valor maior que zero.")

if (valorPrest >= limite ):
    print("Empréstimo não aplicado, conforme sua renda.")
else :
    print("O empréstimo foi aceito e será processado.")
