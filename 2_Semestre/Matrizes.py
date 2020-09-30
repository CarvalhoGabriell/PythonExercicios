matriz1 = []
for i in range(7):  #linhas
    linha = []
    for j in range(2): #colunas
        linha.append(int(input("Informe um numero:")))
    matriz1.append(linha)
cont = 0
for lista in matriz1:
    for elemento in lista:
        print(elemento, end='  ')
        if elemento >=20:
            cont += 1
    print()
print(f"Quantidade de numeros maiores que 20: {cont}")