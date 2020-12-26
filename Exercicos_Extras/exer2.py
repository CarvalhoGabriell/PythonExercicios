lista_numeros = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]


def maioMenorNumero(lista):
    maior = 0
    menor = 0
    for num in range(len(lista)):
        if lista[num] > maior:
            maior = lista[num]
        elif lista[num] < menor:
            menor = lista[num]

    return maior,menor

print(maioMenorNumero(lista_numeros))

################################################


def numerosPares (lista):
    numPar = 0
    for num in range(len(lista)):
        if lista[num] % 2 == 0:
            print("Esse numero", lista[num], "é par")
        # else:
        #     print("Esse numero NAO é impar")

print(numerosPares(lista_numeros))


##########################################

def mediaNum(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

print(mediaNum(lista_numeros))

################################################


def somaNegativos(lista):
    soma_negat = 0
    for numeros in range(len(lista)):
        if lista[numeros] < 0:
            soma_negat += lista[numeros]

    return soma_negat

print(somaNegativos(lista_numeros))
