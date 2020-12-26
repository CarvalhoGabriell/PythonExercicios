
nota_1 = int(input("Informe a nota 1: "))
nota_2 = int(input("Informe a nota 2: "))

media = (nota_1 + nota_2)/2

if media >= 6:
    print("Aprovado.Sua Média foi de {}".format(media))
else:
    print("REPROVADO.Sua Média foi de {}".format(media))

"""
num1 = float(input("Informe um numero: "))
num2 = float(input("Informe outro numero: "))
sinal = input("Agora informe o sinal da operação desejada [+ , - , X , / , **]: ").upper()

if sinal == "+":
    print("VOCE ESCOLHEU SOMAR...")
    soma = num1 + num2
    print(soma)
elif sinal == "-":
    print("VOCE ESCOLHEU SUBTRAIR...")
    subtracao = num1 - num2
    print(subtracao)
elif sinal == "X" or sinal == "*":
    print("VOCE ESCOLHEU MULTIPLICAR...")
    multi = num1 * num2
    print(multi)
elif sinal == "/":
    print("VOCE ESCOLHEU DIVIDIR...")
    if num2 == 0:
        print("NAO É POSSIVEL DIVIDIR POR ZERO!!!")
    divsao = num1 / num2
    print(divsao)
elif sinal == "**":
    print("VOCE ESCOLHEU EXPONENCIAÇÃO...")
    expo = num1 ** num2
    print(expo)
else:
    print("ESSE SINAL É INVALIDO")
"""