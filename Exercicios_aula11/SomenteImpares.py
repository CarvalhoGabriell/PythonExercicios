num_inicial = int(input("Digite qualquer numero: "))
num_final = int(input("Digite outro numero: "))
count = 0

if (num_inicial>num_final):
    aux = num_inicial
    num_inicial = num_final
    num_final = aux


num_inicial = num_inicial + 1
while (num_inicial < num_final):
    if num_inicial % 2 != 0: # Contar apenas os numeros impres
        print(num_inicial)
        count = count + 1 # contar a quantidade de numeros impares
    num_inicial = num_inicial + 1

print("A quantidade de numeros impares é: ", count)
print("FIM")