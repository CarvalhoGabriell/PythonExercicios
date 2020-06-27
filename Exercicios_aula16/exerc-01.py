
num_mult3 = 0
num_mult2 = 0
cont = 0
while (cont <= 7):
    cont += 1
    num = int(input("Digite aqui um numero: "))


    if(num % 2 == 0):
        print(num, " Esse numero é multiplo de 2.")
        num_mult2 = num_mult2 + 1

    elif(num % 3 == 0):
        print(num, " Esse numero é multiplo de 3.")
        num_mult3 = num_mult3 + 1
    else:
        print("Esse numero nao é multiplo de nenhum dos numeros")

print("Os numeros multiplos de 2 são ",num_mult2, "\n")
print("Os numeros multiplos de 3 são ",num_mult3, "\n")