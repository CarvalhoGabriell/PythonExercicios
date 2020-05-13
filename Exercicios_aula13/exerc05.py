num = int(input("Digite um numero: "))

cont = 0
while num > 0:
    numPrimo = num % 2
    print(numPrimo)
    if(numPrimo != 0):
        print("Correto este ",numPrimo," é um numero primo")
    else:
        print("Esse numero nao é im")