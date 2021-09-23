nota_1 = int(input("Informe a Numero 1: "))
nota_2 = int(input("Informe a Numero 2: "))
nota_3 = int(input("Informe a Numero 3: "))

if (nota_1 < nota_2 and nota_2 < nota_3 and nota_1 < nota_3) :
    print("crescente")
else:
    print("não está em ordem crescente")