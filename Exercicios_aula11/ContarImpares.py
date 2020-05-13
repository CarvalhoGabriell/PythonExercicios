num1 = int(input("Digite qualquer numero: "))
num2 = int(input("Digite outro numero: "))

cont = 0
if (num1>num2):
    aux = num1
    num1 = num2
    num2 = aux

while (num1<num2):
    num1 += 1
    if(num1%2 != 0 and num1!=num2):
        cont += 1
        print(num1)
print("A quantidade de numeros impares ente os numeros é: ",cont)