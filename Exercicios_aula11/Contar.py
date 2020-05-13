num1 = int(input("Digite qualquer numero: "))
num2 = int(input("Digite outro numero: "))
somar = 0
if (num1>num2):
    aux = num1
    num1 = num2
    num2 = aux

while (num1<num2):
    num1 += 1
    if (num1 != num2 ):
        somar = somar + num1
        print(num1)
print("A soma dos numeros digitados é: ",somar)