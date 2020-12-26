
numbers = []
qnt_num = 0
while qnt_num < 10:
    numeros = int(input("Informe um numero: "))
    if numeros not in numbers:
        numbers.append(numeros)
        qnt_num += 1
    else:
        print("Numeros repetidos nao vao para a lista")

print("Foram digitados {} numeros".format(qnt_num))