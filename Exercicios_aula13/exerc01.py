numero = int(input("Informe um numero: "))

cont1 = 1
cont2 = 1
cont3 = 1
cont4 = 3
while cont4 <= numero:
    cont3 = cont1 + cont2
    cont1 = cont2
    cont2 = cont3
    cont4 += 1


print("O valor correspondente é {} ".format(cont3))
