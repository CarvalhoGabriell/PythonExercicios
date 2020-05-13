num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))
num3 = int(input("Agora informe o ultimo: "))


if num1 < num2 and num1 < num3 :  ## NUMERO 1 É O MENOR
    print(num1)
    if num2 < num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 < num1 and num2 < num3): ## NUMERO 2 É O MENOR
    print(num2)
    if (num1 < num3):
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
elif (num3 < num2 and num3 < num1): ## NUMERO 3 É O MENOR
    print(num3)
    if (num2 < num1):
        print(num2)
        print(num1)
    else:
        print(num1)
        print(num2)
else:
    if(num1 == num2 == num3):
        print("Os três números são iguais")