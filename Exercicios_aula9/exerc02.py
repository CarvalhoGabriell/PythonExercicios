
num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))

if (num1 > num2):
    print("O numero {} é o maior".format(num1))
elif (num2 > num1):
    print("O numero {} é o maior".format(num2))
else:
    print("Os numeros são iguais")