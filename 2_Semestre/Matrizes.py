numeros = []
numeros1 = []
for i in range(7):
    num = int(input("Digite um numero: "))
    numeros.append(num)
    for j in range(2):
        num2 = int(input("Informe outro numero:"))
        numeros1.append(num2)

for lista in numeros:
    print("\n")
    for elemento in lista:
        print(elemento)